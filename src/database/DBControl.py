from DBHelper import DBHelper

class DBControl:
    def __init__(self):
        self.__db = DBHelper('mydatabase.db')
    
    def save_data_in_db(self, data: list, list_save_data: list):
        self.__db.insert_raw_data(data, list_save_data)
    
    def save_result_data_in_db(self, text: str, tag: str):
        self.__db.insert_result_data(text, tag)

    def get_raw_data_from_bd(self):    
        data = self.__db.get_raw_data()
        list_data = []
        for text in data:
            list_data.append(text.text)
        return list_data
    
    def get_result_data_from_bd(self):    
        data = self.__db.get_result_data()
        list_data = []
        for text in data:
            list_data.append(text.text)
        return list_data

   
        