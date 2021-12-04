from re import I
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import db

Model = declarative_base()
Session = sessionmaker()
Session.configure(bind=db)
session = Session()


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
    def get_list():
        all_kebabs = Kebab.query.all()
        return all_kebabs

    @staticmethod
    def list_to_str(data: list):
        data0 = f'{data[0]}'
        data0 = data0.replace('"', '')
        data1 = f'{data[0]}'
        data1 = data0.replace('"', '')
        data2 = f'{data[0]}'
        data2 = data0.replace('"', '')
        result = data0 + ',' + data1 + ',' + data2
        return result

    @staticmethod
    def to_dict_list(objs):
        result = []
        for o in objs:
            row = {}
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
        session.commit()

    @staticmethod
    def upd_by_id(kebab_id, raw):
        obj = Kebab.query.filter_by(id=kebab_id).first()
        for r in raw:
            if hasattr(obj, r):
                setattr(obj, r, raw[r])
        session.commit()
        return obj

    def get_by_attr(self, raw):
        for r in raw:
            if hasattr(self, r):
                obj = self.query.filter_by(r=raw[r]).first()
                return obj

    @staticmethod
    def get_by_id(kebab_id):
        obj = Kebab.query.filter_by(id=kebab_id).first()
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
