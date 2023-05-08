from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mail_reader import EmailReader, MailCriteria
from time import sleep


# options = webdriver.FirefoxOptions()
# options.add_argument('--marionette-port=0')
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

class ParserBing:
    def __init__(self, user_agent: str):
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.headless = True
        # firefox_options.add_argument('-private')
        firefox_profile = webdriver.FirefoxProfile()    
        firefox_profile.set_preference("general.useragent.override", user_agent)
        # driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=firefox_profile, options=options)
        self.__driver = webdriver.Firefox(firefox_profile=firefox_profile, options=firefox_options)
        self.__wait = WebDriverWait(self.__driver, 10) # Можешь поменять с 10 на 5 и протестить, просто интернет у меня плохой

    def sending_link(self, url: str='https://bing.com'):
        self.__driver.get(url=url)

    def __click_element(self, element_id: str, xpath: bool = False):
        if xpath:
            btn = self.__wait.until(EC.element_to_be_clickable((By.XPATH, element_id)))
        else:
            btn = self.__wait.until(EC.element_to_be_clickable((By.ID, element_id)))
        btn.click()
        # print(f'Нажата кнопка: {element_id}')

    def __send_text(self, element_id: str, text: str, xpath: bool = False):
        if xpath:
            input_field = self.__wait.until(EC.element_to_be_clickable((By.XPATH, element_id)))
        else:
            input_field = self.__wait.until(EC.element_to_be_clickable((By.ID, element_id)))
        input_field.send_keys(text)
        # print(f'Введен текст: {element_id}')
        # print(f'Текст: {text}')


    def parser_bing(self, add_user: str, add_password: str, dict_id_elements: dict, not_error: bool = True): 
        try:
            for element in dict_id_elements:
                sleep(1)
                try:
                    if element == 'iOttText' or element == 'idTxtBx_OTC_Password':
                        self.__send_text(element, '')
                        # print('элемент обнаружен')
                        sleep(10)
                        code = get_code_from_rambler(add_user, add_password)
                        # print(code)
                        self.__send_text(element, code)
                    else:
                        if dict_id_elements[element][0] == 'btn':
                            if element.find('idSIButton9') != -1 or element.find('idBtn_Back') != -1:
                                self.__click_element(element[1:],  dict_id_elements[element][1])  
                            else:
                                self.__click_element(element,  dict_id_elements[element][1])
                                print(element)
                            
                        elif dict_id_elements[element][0] == 'txt':
                            print(element)
                            self.__send_text(element, dict_id_elements[element][1])
                except:
                    print(f'Пропуск элемента: {element}')
                    continue
            return not_error
        except:
            not_error = False
            return not_error
    
    def get_cookies_from_bing(self):
        cookies = self.__driver.get_cookies()
        return cookies
    
    def close_driver(self):
        self.__driver.quit()
    

def get_code_from_rambler(user: str, password: str):
     with EmailReader(
        client="imap.rambler.ru", 
        email_address=user, 
        password=password,
        ) as reader:

        body = reader.get_code_from_email(
            sender_email="account-security-noreply@accountprotection.microsoft.com",
            criteria=MailCriteria.UNSEEN
            )
        if body:
            return body
        else:
            return get_code_from_rambler(user, password)

def get_dict_id_elements(user: str, password: str, add_user: str, add_password: str):
    dict_id_elements = {
        'id_s' : ['btn', False],
        # 'bnp_btn_reject' : ['btn', False],
        'i0116' : ['txt', user],
        '1idSIButton9' : ['btn', False],
        'i0118' : ['txt', password],
        '2idSIButton9' : ['btn', False],
        'iProofEmail' : ['txt', add_user],
        'iSelectProofAction' : ['btn', False],
        'iOttText' : ['txt', 'code'],
        'iVerifyCodeAction' : ['btn', False],
        '1idBtn_Back' : ['btn', False],
        'idTxtBx_OTC_Password' : ['txt', 'code'],
        '3idSIButton9' : ['btn', False],
        '2idBtn_Back' : ['btn', False],
        }   
    return dict_id_elements

def get_cookie(user, password, add_user, add_password, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0'):
    not_error = True
    cookie = ['not cookie']
    dict_id_elements = get_dict_id_elements(user, password, add_user, add_password)
    browser = ParserBing(user_agent=user_agent)
    browser.sending_link()
    not_error = browser.parser_bing(add_user, add_password, dict_id_elements)
    print(not_error)
    if not_error:
        cookie = browser.get_cookies_from_bing()
    browser.sending_link('https://bing.com/chat')
    browser.close_driver()
    return cookie
    

if __name__ == '__main__':
    user = 'conclemnae@outlook.com'
    password = 'g2vMOUxhLn'
    add_user = 'spadgerthankpa1999@ro.ru'
    add_password = 'sdWj8ixDA'
    cookie = get_cookie(user, password, add_user, add_password)
    print(cookie)


