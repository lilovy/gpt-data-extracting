from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import *


class Browser:
    def __init__(self):
        # firefox_options = webdriver.FirefoxOptions()
        # fire/fox_options.headless = True
        # firefox_options.add_argument('-private')
        self.__firefox_profile = webdriver.FirefoxProfile()    
        self.__firefox_profile.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0')
        self.__driver = webdriver.Firefox(firefox_profile=self.__firefox_profile) #options=firefox_options

    def wait_clickable_element(self) -> WebDriverWait:
        self.wait = WebDriverWait(self.__driver, 1)
        return self.wait

    def change_user_agent(self, user_agent: str):
        self.__firefox_profile = webdriver.FirefoxProfile()    
        self.__firefox_profile.set_preference("general.useragent.override", user_agent)
                                              
    def sending_link(self, url: str='https://login.live.com/'):
        self.__driver.get(url=url)
    
    def get_cookies_from_bing(self):
        cookies = self.__driver.get_cookies()
        return cookies
    
    def close_driver(self):
        self.__driver.quit()


class ElementText:    
    def __init__(self, element: str, text: str, wait: WebDriverWait, is_xpath: bool = False):
        self.element = element
        self.__text = text
        self.__is_xpath = is_xpath
        self.__wait = wait

    def action_element(self):
        try:
            if self.__is_xpath:
                self.__input_field = self.__wait.until(EC.element_to_be_clickable((By.XPATH, self.element)))
            else:
                self.__input_field = self.__wait.until(EC.element_to_be_clickable((By.ID, self.element)))
            self.__input_field.send_keys(self.__text)
        except:
            # print(f'Пропущен элемент: {self.element}')
            return


class ElementBtn: 
    def __init__(self, element: str, wait: WebDriverWait, is_xpath: bool = False):
        self.element = element
        self.__is_xpath = is_xpath
        self.__wait = wait
 
    def action_element(self):
        try:
            if self.__is_xpath:
                self.__btn = self.__wait.until(EC.element_to_be_clickable((By.XPATH, self.element)))
            else:
                self.__btn = self.__wait.until(EC.element_to_be_clickable((By.ID, self.element)))
            self.__btn.click()
        except:
            # print(f'Пропущен элемент: {self.element}')
            return

    def is_check_btn(self):
        try:
            if self.__wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/a'))):
                return True
        except:
            return False
    

browser = Browser()

browser.sending_link()
wait = browser.wait_clickable_element()


def get_dict_id_elements(user: str, password: str, add_user: str, add_password: str):
    dict_id_elements = {
        'i0116' : ['txt', user, False],
        '1idSIButton9' : ['btn', False],
        'i0118' : ['txt', password, False],
        '2idSIButton9' : ['btn', False],
        'iProofEmail' : ['txt', add_user, False],
        'iSelectProofAction' : ['btn', False],
        'iOttText' : ['txt', 'code', False],
        'iVerifyCodeAction' : ['btn', False],
        '1id__0' : ['btn', False],
        '2id__0' : ['btn', False],
        '1idBtn_Back' : ['btn', False],
        'idTxtBx_OTC_Password' : ['txt', 'code', False],
        '3idSIButton9' : ['btn', False],
        '2idBtn_Back' : ['btn', False],
        '/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/a[1]' : ['btn', True],
        '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/a' : ['btn', True],
        '/html/body/header/nav/ul/li[2]/a' : ['btn', True],
        }   
    return dict_id_elements


def create_list_object_element(dict_marked_elements: dict, wait: WebDriverWait) -> list[object]:
    list_element_object = []
    for element in dict_marked_elements:
        if dict_marked_elements[element][0] == 'btn':
            if element.find('idSIButton9') != -1 or element.find('idBtn_Back') != -1 or element.find('id__0') != -1:
                 el_btn = ElementBtn(element[1:], wait, dict_marked_elements[element][1])
            else:
                el_btn = ElementBtn(element, wait, dict_marked_elements[element][1])
            list_element_object.append(el_btn)

        elif dict_marked_elements[element][0] == 'txt':
            el_txt = ElementText(element, dict_marked_elements[element][1], wait, dict_marked_elements[element][2])
            list_element_object.append(el_txt)
    return list_element_object

def parser_bing(list_objects: list[object]):
        is_parser = True
        while is_parser:
            for object_el in tqdm(list_objects, total=len(list_objects)):
                if isinstance(object_el, ElementBtn):
                    if object_el.is_check_btn():
                        browser.sending_link('https://bing.com/chat')
                        is_parser = False
                        break
                object_el.action_element()
        cookie = browser.get_cookies_from_bing()
        browser.close_driver()
        return cookie

def get_cookie(email: str, password: str, second_email: str, second_password : str, wait: WebDriverWait):
    dict_elements = get_dict_id_elements(email, password, second_email, second_password)
    list_objects = create_list_object_element(dict_elements, wait)
    cookie = parser_bing(list_objects)
    return cookie
      

if __name__ == '__main__':
    email = 'ehleuveltomcbu@outlook.com'
    password = '3WkAQqPh1i'
    second_email = 'salugihi@rambler.ru'
    second_password = '9gNqXGwT4M'

    cookie = get_cookie(email, password, second_email, second_password, wait)
    print(cookie)




