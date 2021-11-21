import os
from os import access, path
import random

from typing import Type
from experta import factlist
from experta.engine import KnowledgeEngine
from experta.fact import Fact
from experta.fieldconstraint import L, P
from experta.operator import CONTAINS
from experta.rule import Rule
from experta.deffacts import DefFacts
from experta.conditionalelement import AND, EXISTS, FORALL, NOT, OR, TEST
from experta.shortcuts import AS, MATCH
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

    @Rule(Kebab(Type=~L('Свинина'), NumberOfPeople=MATCH.NumberOfPeople))
    def _rule_with_L(self, NumberOfPeople):
        output = f'{NumberOfPeople} has no kebab with Pork'
        return print(output)
    

    @Rule(AS.kebab << Kebab(
        BothSideReady=P(lambda x: x != True)
    ))
    def _rule_with_AS_P(self, kebab):
        for type in kebab.as_dict()['Type']:
            output = f'{kebab.as_dict()["Action"]} and Type is {type}'
            return print(output)

    @Rule(OR(Kebab(Type=~L('Свинина'), Action=MATCH.Action),Kebab(Type=~L('Кенгурятина'), Action=MATCH.Action))) 
    def _rule_with_or(self, Action):
        output = f'Дія: {Action}'
        return print(output)

    @Rule(OR(Kebab(AlreadyTurnedOver=~L(True), Action=MATCH.Action),
    Kebab(BothSideReady=~L(False), Time=P(lambda i: i > 15), Action=MATCH.Action)))
    def _rule_with_or_l_p(self, Action):
        output = f'Дія: {Action}'
        return print(output)     

    @Rule(OR(
        AND(
            Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, DoneAToTheMajority=~L(True)),
            Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, DoneAToTheMajority=~L(False), DoneOnBothSides=~L(False))
        ),
        Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, NumberOfPeople=P(lambda x: 'Іра' in x))))
    def _rule_with_or_and(self, DegreeOfRoastiness):
        output = f'Ступінь піджаристості: {DegreeOfRoastiness}'  
        return print(output)          

    @Rule(
        EXISTS(Kebab(NumberOfPeople=P(lambda x: 'Іра' in x)))
    )
    def _rule_with_exists(self):
        output = f'Іра присутня на жарці шашлику'
        return print(output)
    
    @Rule(
        NOT(NOT(Kebab(NumberOfPeople=P(lambda x: 'Іра' in x))))
    )
    def _rule_with_not_not(self):
        output = f'Іра присутня на жарці шашлику'
        return print(output)

    @Rule(
        FORALL(
            Kebab(AlreadyTurnedOver=~L(False)),
            Kebab(DegreeOfRoastiness='Приготовлений')
        )
    )
    def _rule_with_forall(self):
        output = f'ForAllRule: All kebabs cooked'
        return print(output)
    
    @Rule(
        NOT(
            AND(
                Kebab(AlreadyTurnedOver=~L(False)),
                NOT(Kebab(DegreeOfRoastiness='Приготовлений'))
            )
        )
    )
    def _rule_with_forall1(self):
        output = f'ForAllRule: All kebabs cooked'
        return print(output)