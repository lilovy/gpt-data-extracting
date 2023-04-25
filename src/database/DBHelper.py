from sqlalchemy import create_engine, Column, Integer, String, inspect, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.future import select
from tqdm import *
import time


Base = declarative_base()

class DBHelper:
    def __init__(self, data_base_name: str):
        self.__engine = create_engine(f'sqlite:///{data_base_name}')
        self.__Session = sessionmaker(bind=self.__engine)
        self.__session = self.__Session()
        Base.metadata.create_all(self.__engine)

    def insert_raw_data(self, data: list):
        d = []
        with self.__Session() as session:
            for row in tqdm(data, total=len(data)):
                object_row = RawData(text=row)
                d.append(object_row)
            session.add_all(d)
            session.commit()

    def insert_result_data(self, data: list[tuple]):
        d = []
        with self.__Session() as session:
            for tuple_ in tqdm(data, total=len(data)):
                id = tuple_[0]
                dict_ = tuple_[1]
                values = dict_.get('simple_forms')
                # list_object_rows = []
                for value in values:
                    object_row = ResultData(text=value['simple_form'], tag=value['tag'], raw_data_id=id)
                    d.append(object_row)
                # d.extend(list_object_rows)  
                self.update_data_flag(id)
            session.add_all(d)
            session.commit()

    def insert_bad_request_data(self, data: list[tuple]):
        d = []
        with self.__Session() as session:
            # list_object_rows = []
            for tuple_ in tqdm(data, total=len(data)):
                id = tuple_[0]
                text = tuple_[1]
                object_row = BadRequestData(text=text, raw_data_id=id)
                d.append(object_row)
                # d.extend(list_object_rows)  
            session.add_all(d)
            session.commit()

    def delete_raw_data(self, id):
        data = self.__session.query(RawData).filter(RawData.id == id).first()
        self.__session.delete(data)
        self.__session.commit()

    def delete_result_data(self, id):
        data = self.__session.query(ResultData).filter(ResultData.id == id).first()
        self.__session.delete(data)
        self.__session.commit()

    def get_raw_data(self, num, used: bool = False) -> list[tuple]:
        data = self.__session.query(RawData).filter(RawData.used == used).limit(num).all()
        return [(d.id, d.text) for d in data]
    
    def update_data_flag(self, id: int):
        data_row = self.__session.query(RawData).filter(RawData.id == id).update({"used": True})
        self.__session.commit()


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
    raw_data_id = Column(Integer, ForeignKey('raw_data.id'))
    result_data = relationship('RawData', back_populates='data')

class BadRequestData(Base):
    __tablename__ = 'bad_request'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    used = Column(Boolean, default=False)
    raw_data_id = Column(Integer, ForeignKey('raw_data.id'))

