import os
from re import I
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime as time

from core.config import db

Model = declarative_base()
Session = sessionmaker()
Session.configure(bind=db)
session = Session()

__version__ = '1.0'

class Kebab(Model):
    __tablename__ = 'Experta'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Type = Column(String(255))
    Action = Column(String(255))
    DegreeOfRoasting = Column(String(255))
    AlreadyTurnedOver = Column(Boolean, default=False)
    PartyReady = Column(Boolean, default=False)
    DoneOnOneSide = Column(Boolean, default=False)
    DoneOnBothSides = Column(Boolean, default=False)
    BothSideReady = Column(Boolean, default=False)
    Time = Column(Integer, default=0)
    DoneAToTheMajority = Column(Boolean, default=False)
    NumberOfPeople = Column(String(255), default='')
    Added = Column(DateTime, default=time.utcnow())

    def __init__(self, Type, Action, DegreeOfRoasting,
                 AlreadyTurnedOver, PartyReady, DoneOnOneSide, DoneOnBothSides,
                 BothSideReady, Time, DoneAToTheMajority, NumberOfPeople) -> None:
        self.Type = Type
        self.Action = Action
        self.DegreeOfRoasting = DegreeOfRoasting
        self.AlreadyTurnedOver = AlreadyTurnedOver
        self.PartyReady = PartyReady
        self.DoneOnOneSide = DoneOnOneSide
        self.DoneOnBothSides = DoneOnBothSides
        self.BothSideReady = BothSideReady
        self.Time = Time
        self.DoneAToTheMajority = DoneAToTheMajority
        self.NumberOfPeople = NumberOfPeople

    @staticmethod
    def get_list() -> list:
        all_kebabs = session.query(Kebab).all()
        return all_kebabs

    @staticmethod
    def list_to_str(data: list):
        data0 = f'{data[0]}'
        data0 = data0.replace('"', '')
        data1 = f'{data[1]}'
        data1 = data1.replace('"', '')
        data2 = f'{data[2]}'
        data2 = data2.replace('"', '')
        result = data0 + ',' + data1 + ',' + data2
        return result

    @staticmethod
    def to_dict_list(object: object):
        result = list()
        for o in object:
            row = dict()
            for c in o.__table__.columns:
                row[c.name] = getattr(o, c.name)
            result.append(row)
        return result

    @staticmethod
    def add_new(Type, Action, DegreeOfRoasting,
                AlreadyTurnedOver, PartyReady, DoneOnOneSide, DoneOnBothSides,
                BothSideReady, Time, DoneAToTheMajority, NumberOfPeople):
        es = Kebab(
            Type=Type,
            Action=Action,
            DegreeOfRoasting=DegreeOfRoasting,
            AlreadyTurnedOver=AlreadyTurnedOver,
            PartyReady=PartyReady,
            DoneOnOneSide=DoneOnOneSide,
            DoneOnBothSides=DoneOnBothSides,
            BothSideReady=BothSideReady,
            Time=Time,
            DoneAToTheMajority=DoneAToTheMajority,
            NumberOfPeople=Kebab.list_to_str(NumberOfPeople)
        )
        session.add(es)
        return session.commit()
        

    @staticmethod
    def upd_by_id(kebab_id, raw):
        obj = session.query(Kebab).filter_by(id=kebab_id).first()
        for key in raw:
            if hasattr(obj, key):
                setattr(obj, key, getattr(obj, key))
        session.commit()
        return obj

    def get_by_attr(self, raw):
        for r in raw:
            if hasattr(self, r):
                obj = session.query(self).filter_by(r=raw[r]).first()
                return obj

    @staticmethod
    def get_by_id(kebab_id):
        obj = session.query(Kebab).filter_by(id=kebab_id).first()
        if not obj:
            raise 'Kebab not found'
        return obj

    @staticmethod
    def del_by_id(kebab_id):
        """[summary]

        Args:
            kebab_id ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            session.delete(Kebab.get_by_id(kebab_id))
            session.commit()
        except:
            kebab_id = None
        return kebab_id

    def to_dict(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row


if __name__ == "__main__":
    Model.metadata.create_all(db)
