import os
from os import name
from re import T
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import db
from experta.rule import Rule

Model = declarative_base()
Session = sessionmaker()
Session.configure(bind=db)
session = Session()


class Rules(Model):
    __tablename__ = 'Rules'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    RuleId = Column(Integer, nullable=False)
    Name = Column(String)
    Description = Column(String)
    Output = Column(String)

    def __init__(self, RuleId, Name, Description, Output):
        self.RuleId = RuleId
        self.Name = Name
        self.Description = Description
        self.Output = Output

    @staticmethod
    def get_list() -> list:
        all_rules = session.query(Rules).all()
        return all_rules

    @staticmethod
    def to_dict_list(objs) -> list:
        result = []
        for o in objs:
            row = {}
            for c in o.__table__.columns:
                row[c.name] = getattr(o, c.name)
            result.append(row)
        return result

    @staticmethod
    def add_new(RuleId, Name, Description, Output) -> session:
        rule = Rules(
            RuleId=RuleId,
            Name=Name,
            Description=Description,
            Output=Output
        )
        session.add(rule)
        session.commit()

    def to_dict(self) -> dict:
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row

    @staticmethod
    def upd_by_id(rule_id, raw) -> object:
        obj = session.query(Rules).filter_by(RuleId=rule_id).first()
        for r in raw:
            if hasattr(obj, r):
                setattr(obj, r, raw[r])
        session.commit()
        return obj

    @staticmethod
    def get_by_id(rule_id) -> object:
        obj = session.query(Rules).filter_by(RuleId=rule_id).first()
        if not obj:
            raise 'Rules not found'
        return obj


if __name__ == "__main__":
    Model.metadata.create_all(db)
