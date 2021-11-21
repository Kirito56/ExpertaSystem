import os
from os import access, path
import random

from typing import Type
from experta import factlist
from experta.engine import KnowledgeEngine
from experta.fact import Fact
from experta.operator import CONTAINS
from experta.rule import Rule
from experta.deffacts import DefFacts
from experta.conditionalelement import AND, OR, TEST
from experta.shortcuts import MATCH
from exception import FactNotFoundError

from ES import Kebab


class DefFact(KnowledgeEngine):
    @DefFacts()
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
            yield Kebab(Type=Type,
                        Action=Action,DegreeOfRoastiness=DegreeOfRoastiness, 
                        AlreadyTurnedOver=AlreadyTurnedOver,PartyReady=PartyReady,
                        DoneOnOneSide=DoneOnOneSide,DoneOnBothSides=DoneOnBothSides,
                        BothSideReady=BothSideReady,Time=Time,
                        DoneAToTheMajority=DoneAToTheMajority,
                        NumberOfPeople=NumberOfPeople)
            Kebab.write_to_file(i,Type,Action,DegreeOfRoastiness,AlreadyTurnedOver,PartyReady,DoneOnOneSide,
            DoneOnBothSides, BothSideReady, Time, DoneAToTheMajority, NumberOfPeople)
            i += 1

    @Rule(Kebab(Type='Свинина', Time=15, Action='Чекати'))
    def _chain_start(self) -> str:
        """
        Початок ланцюга

        :return: Found
        :rtype: str
        """
        self.facts.retract(0)
        return print('Правило Найти Свинину Яка Жариться 15хв і дія Чекати')
                
            

    @Rule(Kebab(Type='Свинина', Time=0, Action='Перевернути', AlreadyTurnedOver=True))
    def _chain_cont(self) -> str:
        """
        Продовження ланцюга\n
        :return: Modified Fact
        """
        return print('Found')


    @Rule(Kebab(NumberOfPeople=MATCH.NumberOfPeople))
    def _rule_with_using_match(self, NumberOfPeople) -> str:
        if 'Іра' in NumberOfPeople:
            return print('Іра найдена')

    @Rule(Kebab(Time=MATCH.Time), TEST(lambda Time: Time<15))
    def _rule_with_using_test(self,  Time):
        return print(f'Час < 15: {Time}')

    @Rule(Kebab(PartyReady=False))
    def _rule_chain_1(self):
        rul = self.facts.changes
        return rul

                
        

    @Rule(Kebab(Action='Чекати'))
    def _rule_chain_cont_1(self):
        """
        
        """
        pass
                