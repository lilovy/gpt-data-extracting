from sqlalchemy import create_engine, Column, Integer, String, inspect, ForeignKey, Boolean, Text, TIMESTAMP
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.future import select
from sqlalchemy import func
from tqdm import *
import time
from datetime import datetime
import json


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

    def add_bind_session(
        self, 
        email: str,
        password: str,
        second_email: str = None,
        second_password: str = None,
        cookie: str = None,
        ):
        with self.__Session() as session:
            obj = BingCookie(
                email=email,
                password=password,
                second_email=second_email,
                second_password=second_password,
                cookie=json.dumps(cookie),
                )
            session.add(obj)
            session.commit()

    def update_bing_cookie(
        self,
        email: str,
        cookie: str,
        ):
        update = self.__session.query(
            BingCookie
        ).filter(
            BingCookie.email == email
        ).update(
            {
                "cookie": json.dumps(cookie), 
                "timestamp": func.strftime("%s", datetime.utcnow()),
            }
        )
        self.__session.commit()

    def get_fresh_cookies(
        self,
        # email: str,
        ) -> list:
        query: BingCookie
        query = self.__session.query(
            BingCookie
        ).filter(
            # BingCookie.email == email,
            BingCookie.timestamp > (func.strftime("%s", datetime.utcnow()) - 1500)
        ).all()
        if query:
            cookies = [json.loads(q.cookie) for q in query if q.cookie]
            if len(cookies) > 0:
                return cookies
        return

    def get_fresh_cookie(
        self,
        email: str,
        ) -> list:
        query: BingCookie
        query = self.__session.query(
            BingCookie
        ).filter(
            BingCookie.email == email,
            BingCookie.timestamp > (func.strftime("%s", datetime.utcnow()) - 1500)
        ).all()
        if query:
            cookies = [json.loads(q.cookie) for q in query if q.cookie]
            if len(cookies) > 0:
                return cookies
        return

    def get_emails(
        self,
        ) -> list[str]:
        query = self.__session.query(BingCookie).all()
        if query:
            return [email.email for email in query]
        return

    def get_auth_data(
        self,
        email: str = None) -> list[dict]:
        if email:
            query = self.__session.query(
                BingCookie
            ).filter(
                BingCookie.email == email,
            ).all()
        else:
            query = self.__session.query(
                BingCookie
            ).all()
        if query:
            res = []
            for q in query:
                q: BingCookie
                dct = {
                    "email": q.email,
                    "password": q.password,
                    "second_email": q.second_email,
                    "second_password": q.second_password,
                }
                res.append(dct)
            return res
        return

    def get_stale_cookies(self) -> list[dict]:
        query = self.__session.query(
            BingCookie
        ).filter(
            BingCookie.timestamp < (func.strftime("%s", datetime.utcnow()) - 1500)
        ).all()
        stale = []
        for q in query:
            q: BingCookie
            d = {}
            d["email"] = q.email
            d["password"] = q.password
            d["second_email"] = q.second_email
            d["second_password"] = q.second_password
            if q.cookie:
                d["cookie"] = json.loads(q.cookie)
            stale.append(d)
        if len(stale) > 0:
            return stale
        return

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

class BingCookie(Base):
    __tablename__ = 'cookies_bing_session'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    second_email = Column(String)
    second_password = Column(String)
    cookie = Column(Text)
    timestamp = Column(Integer, default=func.strftime("%s", datetime.utcnow()))
