from sqlalchemy import create_engine, Column, Integer, String, inspect, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from tqdm import *
import time


Base = declarative_base()

class DBHelper:
    def __init__(self, data_base_name: str):
        self.__engine = create_engine(f'sqlite:///{data_base_name}')
        self.__Session = sessionmaker(bind=self.__engine)
        self.__session = self.__Session()
        Base.metadata.create_all(self.__engine)

    @timer
    def insert_raw_data(self, data: list, list_save_data: list):
        with self.__Session() as session:
            for row in tqdm(data, total=len(data)):
                object_row = RawData(text=row)
                list_save_data.append(object_row)
            session.add_all(list_save_data)
            session.commit()
 
    def insert_result_data(self, data: list, list_save_data: list):
          with self.__Session() as session:
            for tuple_ in tqdm(data, total=len(data)):
                dict_ = tuple_[1]
                values = dict_.get('simple_forms')
                list_object_rows = []
                for value in values:
                    object_row = ResultData(text=value['simple_form'], tag=value['tag'], row_id=tuple_[0])
                    list_object_rows.append(object_row)
                list_save_data.extend(list_object_rows)  
            session.add_all(list_save_data)
            session.commit()

    def insert_bad_request_data(self, data: list, list_save_data: list):
          with self.__Session() as session:
            for tuple_ in tqdm(data, total=len(data)):
                dict_ = tuple_[1]
                values = dict_.get('simple_forms')
                list_object_rows = []
                for value in values:
                    object_row = ResultData(text=value['simple_form'], tag=value['tag'], row_id=tuple_[0])
                    list_object_rows.append(object_row)
                list_save_data.extend(list_object_rows)  
            session.add_all(list_save_data)
            session.commit()

    def delete_raw_data(self, id):
        data = self.__session.query(RawData).filter(RawData.id == id).first()
        self.__session.delete(data)
        self.__session.commit()

    def delete_result_data(self, id):
        data = self.__session.query(ResultData).filter(ResultData.id == id).first()
        self.__session.delete(data)
        self.__session.commit()

    def get_raw_data(self):
        return self.__session.query(RawData).all()

    def get_result_data(self):
        return self.__session.query(ResultData).all()
    
class RawData(Base):
    __tablename__ = 'raw_data'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    used = Column(Boolean, default=False)
    data = relationship('ResultData', back_populates='result_data')

class ResultData(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    tag = Column(String)
    row_id = Column(Integer, ForeignKey('raw_data.id'))
    result_data = relationship('RawData', back_populates='data')

class BadRequestData(Base):
    __tablename__ = 'bad_request'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    used = Column(Boolean, default=False)
    row_id = Column(Integer, ForeignKey('raw_data.id'))

