import random
from experta.engine import KnowledgeEngine
from experta.operator import CONTAINS
from experta.rule import Rule
from experta.conditionalelement import AND, OR, TEST
from experta.shortcuts import MATCH
from exception import FactNotFoundError

from ES import Kebab

class Asserts(KnowledgeEngine):
    def init_kebab(self):
        j = int(input('Введіть кількість фактів: '))
        for i in range(j):
            Type=random.choice(['Свинина', 'Курка', 'Страусятина', 'Кенгурятина'])
            Action=random.choice(['Чекати', 'Перевернути', 'Забрати'])
            DegreeOfRoastiness=random.choice(['Сире', 'Починає піджарюватись', 'Піджарилось', 'Приговлений', 'Згорівший'])
            AlreadyTurnedOver=random.choice([True, False])
            PartyReady=random.choice([True, False])
            DoneOnOneSide=random.choice([True, False])
            DoneOnBothSides=random.choice([True, False])
            BothSideReady=random.choice([True, False])
            Time=random.randint(0, 30)
            DoneAToTheMajority=random.choice([True, False])
            NumberOfPeople=random.choice([["Іра", "Яна", "Влада"], 
                        ["Володя", "Женя", "Влад"], ["Янасрав", "Вадім", "Олесь"]])
            self.declare(Kebab(Type=Type,
                        Action=Action,DegreeOfRoastiness=DegreeOfRoastiness, 
                        AlreadyTurnedOver=AlreadyTurnedOver,PartyReady=PartyReady,
                        DoneOnOneSide=DoneOnOneSide,DoneOnBothSides=DoneOnBothSides,
                        BothSideReady=BothSideReady,Time=Time,
                        DoneAToTheMajority=DoneAToTheMajority,
                        NumberOfPeople=NumberOfPeople))
            
    @Rule()
    def _chain_start(self) -> str:
        """
        Початок ланцюга

        :return: Found
        :rtype: str
        """
        self.facts.retract(0)
        facts = self.facts.changes
        return True
