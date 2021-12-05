import datetime
import os

from experta.fact import Fact, Field

__version__ = '0.9'

class Kebab(Fact):
    """
    * Type - Тип м'яса
    * Action - Дія
    * DegreeOfRoasting - Ступінь піджаристості
    * AlreadyTurnedOver - Вже переверталось
    * PartyReady - Сторона готовв
    * DoneOnOneSide - Готово з однієї сторони
    * DoneOnBothSides - Готово з другої сторони
    * BothSideReady - Друга сторона готова
    * Time - Час
    * DoneAToTheMajority - Готово по думці більшості
    * NumberOfPeople - Кількість людей
    """
    
    Type = Field(str, mandatory=True, default='')
    Action = Field(str, mandatory=True, default='')
    DegreeOfRoastiness = Field(str, mandatory=True, default=0)
    AlreadyTurnedOver = Field(bool, mandatory=True, default=False)
    PartyReady = Field(bool, mandatory=True, default=False)
    DoneOnOneSide = Field(bool, mandatory=True, default=False)
    DoneOnBothSides = Field(bool, mandatory=True, default=False)
    BothSideReady = Field(bool, mandatory=True, default=False)
    Time = Field(int, mandatory=True, default=0)
    DoneAToTheMajority = Field(bool, mandatory=True, default=False)
    NumberOfPeople = Field(list, mandatory=True, default=0)

    @staticmethod
    def to_json(facts: list, rules: list):
        if os.path.exists(f'{os.getcwd()}/{str("outputs.json")}'):
            with open(f'{os.getcwd()}/{str("outputs.json")}', mode='w', encoding='UTF-8') as json:
                def to_dict():
                    out = dict(
                        facts=facts,
                        rules=rules
                    )
                    return out
                json.write(f'{to_dict()}')
        else:
            with open(f'{os.getcwd()}/{str("outputs.json")}', mode='w', encoding='UTF-8') as json:
                def to_dict():
                    out = dict(
                        facts=facts,
                        rules=rules
                    )
                    return out
                json.write(f'{to_dict()}')