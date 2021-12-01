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
        """[summary]

        Returns:
            str: [description]
        """        
        self.facts.retract(0)
        output = 'Знайдено'
        name = 'Правило 1'
        description = 'Шукає факт де вказано:\nТип = Свинина,\nЧас = 15,\nДія = Чекати'
        return Kebab.rules_output(name,output,description,1)
                
            

    @Rule(Kebab(Type='Свинина', Time=0, Action='Перевернути', AlreadyTurnedOver=True))
    def _chain_cont(self) -> str:
        """[summary]

        Returns:
            str: [description]
        """        
        output = 'Found'
        name = 'Правило 2'
        description = 'Шукає факт де вказанo:\nTип = Свинина,\nЧас = 0,\nДія = перевернути,\nВже перевертали = Так'
        return Kebab.rules_output(name, output, description,2)


    @Rule(Kebab(NumberOfPeople=MATCH.NumberOfPeople))
    def _rule_with_using_match(self, NumberOfPeople) -> str:
        if 'Іра' in NumberOfPeople:
            output = 'Іра найдена'
            name = 'Правило 3'
            description = 'Шукає факт де серед людей є Іра'
            return Kebab.rules_output(name, output, description,3)

    @Rule(Kebab(Time=MATCH.Time), TEST(lambda Time: Time<15))
    def _rule_with_using_test(self,  Time):
        output = f'Час < 15: {Time}'
        name = 'Правило 4'
        description = 'Шукає факт де час меньше як зазначено в функції TEST'
        return Kebab.rules_output(name, output, description,4)


    @Rule(Kebab(Type=~L('Свинина'), NumberOfPeople=MATCH.NumberOfPeople))
    def _rule_with_L(self, NumberOfPeople):
        output = f'{NumberOfPeople} has no kebab with Pork'
        name = 'Правило 5'
        description = 'Шукає факт де Тип не Свинина і Виводить людей'
        return Kebab.rules_output(name, output, description,5)
    

    @Rule(AS.kebab << Kebab(
        BothSideReady=P(lambda x: x != True)
    ))
    def _rule_with_AS_P(self, kebab):
        for type in kebab.as_dict()['Type']:
            output = f'{kebab.as_dict()["Action"]} and Type is {type}'
            name = 'Правило 6'
            description = 'Шукає факт де Друга сторона не готова'
            return Kebab.rules_output(name, output, description,6)

    @Rule(OR(Kebab(Type=~L('Свинина'), Action=MATCH.Action),Kebab(Type=~L('Кенгурятина'), Action=MATCH.Action))) 
    def _rule_with_or(self, Action):
        output = f'Дія: {Action}'
        name = 'Правило 7'
        description = 'Шукає факт де Тип не свинина або де тип не Кенгуру'
        return Kebab.rules_output(name, output, description,7)

    @Rule(OR(Kebab(AlreadyTurnedOver=~L(True), Action=MATCH.Action),
    Kebab(BothSideReady=~L(False), Time=P(lambda i: i > 15), Action=MATCH.Action)))
    def _rule_with_or_l_p(self, Action):
        output = f'Дія: {Action}'
        name = 'Правило 8'
        description = 'Шукає факт де не перевертали або готово з другої сторони і функція де час меньше 15'
        return Kebab.rules_output(name, output, description,8) 

    @Rule(OR(
        AND(
            Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, DoneAToTheMajority=~L(True)),
            Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, DoneAToTheMajority=~L(False), DoneOnBothSides=~L(False))
        ),
        Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, NumberOfPeople=P(lambda x: 'Іра' in x))))
    def _rule_with_or_and(self, DegreeOfRoastiness):
        output = f'Ступінь піджаристості: {DegreeOfRoastiness}'  
        name = 'Правило 9'
        description = 'Шукає факт де не готово по думці більшості і готово по думці більшості або функція пошуку Іри серед людей'
        return Kebab.rules_output(name, output, description,9)           

    @Rule(
        EXISTS(Kebab(NumberOfPeople=P(lambda x: 'Іра' in x)))
    )
    def _rule_with_exists(self):
        output = f'Іра присутня на жарці шашлику'
        name = 'Правило 10'
        description = 'Шукає факт де серед людей є Іра (EXIST())'
        return Kebab.rules_output(name, output, description,9)
    
    @Rule(
        NOT(NOT(Kebab(NumberOfPeople=P(lambda x: 'Іра' in x))))
    )
    def _rule_with_not_not(self):
        output = f'Іра присутня на жарці шашлику'
        name = 'Правило 11'
        description = 'Шукає факт де серед людей є Іра (NOT(NOT()))'
        return Kebab.rules_output(name, output, description,9)

    @Rule(
        FORALL(
            Kebab(AlreadyTurnedOver=~L(False)),
            Kebab(DegreeOfRoastiness='Приготовлений')
        )
    )
    def _rule_with_forall(self):
        output = f'ForAllRule: All kebabs cooked'
        name = 'Правило 12'
        description = 'Шукає всі факти які були перевернуті та приготовлені (FORALL())'
        return Kebab.rules_output(name, output, description,9)
    
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
        name = 'Правило 13'
        description = 'Шукає всі факти які були перевернуті та приготовлені (NOT(AND()))'
        return Kebab.rules_output(name, output, description,9)
    
    def avarage(self, s, end):
        result = (s+end)/2
        return print(result)
    
    def avarage3(self, s, end, sum=None):
        if sum: return print((s+end+sum)/3)
        else: self.avarage(s, end)
