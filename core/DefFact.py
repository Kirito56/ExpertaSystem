import os
from os import access, path
import random
from re import I

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
from core.exception import FactNotFoundError
from models.Kebab import Kebab as MKebab
from models.Rules import Rules

from ES import Kebab


class DefFact(KnowledgeEngine):
    @DefFacts()
    def init_kebab(self) -> MKebab.add_new:
        """Ініціалізація факту

        Yields:
            [type]: Створення факта
        
        """        
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
                        ["Володя", "Женя", "Влад"], ["Ярослав", "Вадім", "Олесь"]])
            yield Kebab(Type=Type,
                        Action=Action,DegreeOfRoastiness=DegreeOfRoastiness, 
                        AlreadyTurnedOver=AlreadyTurnedOver,PartyReady=PartyReady,
                        DoneOnOneSide=DoneOnOneSide,DoneOnBothSides=DoneOnBothSides,
                        BothSideReady=BothSideReady,Time=Time,
                        DoneAToTheMajority=DoneAToTheMajority,
                        NumberOfPeople=NumberOfPeople)
            MKebab.add_new(Type,Action,DegreeOfRoastiness,AlreadyTurnedOver,PartyReady,DoneOnOneSide,
            DoneOnBothSides, BothSideReady, Time, DoneAToTheMajority, NumberOfPeople)
            i += 1
        

    @Rule(Kebab(Type='Свинина', Time=15, Action='Чекати'))
    def _chain_start(self) -> Kebab.rules_output:
        """Правило 1

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        self.facts.retract(0)
        output = 'Знайдено'
        name = 'Правило 1'
        description = 'Шукає факт де вказано:\nТип = Свинина,\nЧас = 15,\nДія = Чекати'
        return Rules.add_new(RuleId=1,Name=name,Description=description,Output=output)
                
            

    @Rule(Kebab(Type='Свинина', Time=0, Action='Перевернути', AlreadyTurnedOver=True))
    def _chain_cont(self) -> Kebab.rules_output:
        """Правило 2

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = 'Found'
        name = 'Правило 2'
        description = 'Шукає факт де вказанo:\nTип = Свинина,\nЧас = 0,\nДія = перевернути,\nВже перевертали = Так'
        return Rules.add_new(RuleId=2,Name=name,Description=description,Output=output)


    @Rule(Kebab(NumberOfPeople=MATCH.NumberOfPeople))
    def _rule_with_using_match(self, NumberOfPeople) -> Kebab.rules_output:
        """Правило із функцією MATCH

        Args:
            NumberOfPeople (list): Список із іменами людей які присутні на жарці шашлику

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        if 'Іра' in NumberOfPeople:
            output = 'Іра найдена'
            name = 'Правило 3'
            description = 'Шукає факт де серед людей є Іра'
            return Rules.add_new(RuleId=3,Name=name,Description=description,Output=output)

    @Rule(Kebab(Time=MATCH.Time), TEST(lambda Time: Time<15))
    def _rule_with_using_test(self,  Time) -> Kebab.rules_output:
        """Правило із функцією MATCH та TEST

        Args:
            Time (int): Час який меньше чим зазначено в функції TEST

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'Час < 15: {Time}'
        name = 'Правило 4'
        description = 'Шукає факт де час меньше як зазначено в функції TEST'
        return Rules.add_new(RuleId=4,Name=name,Description=description,Output=output)


    @Rule(Kebab(Type=~L('Свинина'), NumberOfPeople=MATCH.NumberOfPeople))
    def _rule_with_L(self, NumberOfPeople) -> Kebab.rules_output:
        """Правило із використанням функції Не(L) та MATCH

        Args:
            NumberOfPeople (list): Список із іменами людей які присутні на жарці шашлику

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'{NumberOfPeople} has no kebab with Pork'
        name = 'Правило 5'
        description = 'Шукає факт де Тип не Свинина і Виводить людей'
        return Rules.add_new(RuleId=5,Name=name,Description=description,Output=output)
    

    @Rule(AS.kebab << Kebab(
        BothSideReady=P(lambda x: x != True)
    ))
    def _rule_with_AS_P(self, kebab) -> Kebab.rules_output:
        """Правило із використанням функції Створеня словника(AS) та P

        Args:
            kebab (dict): факт перетворений в словник

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        for type in kebab.as_dict()['Type']:
            output = f'{kebab.as_dict()["Action"]} and Type is {type}'
            name = 'Правило 6'
            description = 'Шукає факт де Друга сторона не готова'
            return Rules.add_new(RuleId=6,Name=name,Description=description,Output=output)

    @Rule(OR(Kebab(Type=~L('Свинина'), Action=MATCH.Action),Kebab(Type=~L('Кенгурятина'), Action=MATCH.Action))) 
    def _rule_with_or(self, Action) -> Kebab.rules_output:
        """Правило із використанням функції OR(АБО), L(НЕ), MATCH

        Args:
            Action ([type]): Дія яка відповідає факту не Свинина або не Кенгуру

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'Дія: {Action}'
        name = 'Правило 7'
        description = 'Шукає факт де Тип не свинина або де тип не Кенгуру'
        return Rules.add_new(RuleId=7,Name=name,Description=description,Output=output)

    @Rule(OR(Kebab(AlreadyTurnedOver=~L(True), Action=MATCH.Action),
    Kebab(BothSideReady=~L(False), Time=P(lambda i: i > 15), Action=MATCH.Action)))
    def _rule_with_or_l_p(self, Action) -> Kebab.rules_output:
        """Правило із використанням функції OR(АБО), L(НЕ), MATCH, P

        Args:
            Action ([type]): Дія яка відповідає факту Не перевертали, час більше 15, готово з однієї сторони

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'Дія: {Action}'
        name = 'Правило 8'
        description = 'Шукає факт де не перевертали або готово з другої сторони і функція де час меньше 15'
        return Rules.add_new(RuleId=8,Name=name,Description=description,Output=output)

    @Rule(OR(
        AND(
            Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, DoneAToTheMajority=~L(True)),
            Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, DoneAToTheMajority=~L(False), DoneOnBothSides=~L(False))
        ),
        Kebab(DegreeOfRoastiness=MATCH.DegreeOfRoastiness, NumberOfPeople=P(lambda x: 'Іра' in x))))
    def _rule_with_or_and(self, DegreeOfRoastiness) -> Kebab.rules_output:
        """Правило із використанням функції OR(АБО), AND(І), L(НЕ), MATCH, P

        Args:
            DegreeOfRoastiness ([type]): Ступінь піджаристості який відповідає факту (Готово/Не готово) по думці більшості, готово з однієї сторони

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'Ступінь піджаристості: {DegreeOfRoastiness}'  
        name = 'Правило 9'
        description = 'Шукає факт де не готово по думці більшості і готово по думці більшості або функція пошуку Іри серед людей'
        return Rules.add_new(RuleId=9,Name=name,Description=description,Output=output)           

    @Rule(
        EXISTS(Kebab(NumberOfPeople=P(lambda x: 'Іра' in x)))
    )
    def _rule_with_exists(self) -> Kebab.rules_output:
        """Правило із використанням функції EXIST(Присутнє)

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'Іра присутня на жарці шашлику'
        name = 'Правило 10'
        description = 'Шукає факт де серед людей є Іра (EXIST())'
        return Rules.add_new(RuleId=10,Name=name,Description=description,Output=output)
    
    @Rule(
        NOT(NOT(Kebab(NumberOfPeople=P(lambda x: 'Іра' in x))))
    )
    def _rule_with_not_not(self) -> Kebab.rules_output:
        """Правило із використанням функції EXIST(Присутнє) тільки замість EXIST - NOT(NOT())

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'Іра присутня на жарці шашлику'
        name = 'Правило 11'
        description = 'Шукає факт де серед людей є Іра (NOT(NOT()))'
        return Rules.add_new(RuleId=11,Name=name,Description=description,Output=output)

    @Rule(
        FORALL(
            Kebab(AlreadyTurnedOver=~L(False)),
            Kebab(DegreeOfRoastiness='Приготовлений')
        )
    )
    def _rule_with_forall(self) -> Kebab.rules_output:
        """Правило із використанням функції FORALL(Для всіх)

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'ForAllRule: All kebabs cooked'
        name = 'Правило 12'
        description = 'Шукає всі факти які були перевернуті та приготовлені (FORALL())'
        return Rules.add_new(RuleId=12,Name=name,Description=description,Output=output)
    
    @Rule(
        NOT(
            AND(
                Kebab(AlreadyTurnedOver=~L(False)),
                NOT(Kebab(DegreeOfRoastiness='Приготовлений'))
            )
        )
    )
    def _rule_with_forall1(self) -> Kebab.rules_output:
        """Правило із використанням функції FORALL(Для всіх) тільки замість FORALL - NOT(AND(NOT()))

        Returns:
            Kebab.rules_output: записує правило в файл з розширенням .json
        """        
        output = f'ForAllRule: All kebabs cooked'
        name = 'Правило 13'
        description = 'Шукає всі факти які були перевернуті та приготовлені (NOT(AND()))'
        return Rules.add_new(RuleId=13,Name=name,Description=description,Output=output)
    
    def avarage(self, s: int, end: int) -> int:
        """Рахує середнє значення по часу приготування

        Args:
            s (int): Початковий час
            end (int): Кінцевий час

        Returns:
            int: Середнє значення часу
        """        
        result = (s+end)/2
        return print(result)
    
    def avarage3(self, s: int, end: int, sum=None) -> avarage:
        """Рахує середнє значення по часу приготування тільки для 3

        Args:
            s (int): Початковий час
            end (int): Кінцевий час
            sum ([type], optional): [description]. Defaults to None.

        Returns:
            avarage: Рахує середнє значення по часу приготування
        """        
        if sum: return print((s+end+sum)/3)
        else: self.avarage(s, end)
            
