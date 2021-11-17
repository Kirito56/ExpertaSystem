from experta.engine import KnowledgeEngine
from experta.rule import Rule
from experta.deffacts import DefFacts
from experta.conditionalelement import AND, OR
from exception import FactNotFoundError

from ES import Kebab


class DefFact(KnowledgeEngine):
    @DefFacts()
    def init_kebab(self):
        yield Kebab(Type='Pork',
                    Action='Wait',
                    DegreeOfRoastiness=2,
                    AlreadyTurnedOver=False,
                    PartyReady=True,
                    DoneOnOneSide=True,
                    DoneOnBothSides=False,
                    BothSideReady=False,
                    Time=15,
                    DoneAToTheMajority=False,
                    NumberOfPeople=2)
        yield Kebab(Type='Ostrich',
                    Action='Wait',
                    DegreeOfRoastiness=2,
                    AlreadyTurnedOver=False,
                    PartyReady=True,
                    DoneOnOneSide=True,
                    DoneOnBothSides=False,
                    BothSideReady=False,
                    Time=10,
                    DoneAToTheMajority=False,
                    NumberOfPeople=2)
        yield Kebab(Type='Kangaroo',
                    Action='Wait',
                    DegreeOfRoastiness=2,
                    AlreadyTurnedOver=False,
                    PartyReady=True,
                    DoneOnOneSide=True,
                    DoneOnBothSides=False,
                    BothSideReady=False,
                    Time=10,
                    DoneAToTheMajority=False,
                    NumberOfPeople=2)
        yield Kebab(Type='Kangaroo',
                    Action='Wait',
                    DegreeOfRoastiness=2,
                    AlreadyTurnedOver=False,
                    PartyReady=True,
                    DoneOnOneSide=True,
                    DoneOnBothSides=False,
                    BothSideReady=False,
                    Time=15,
                    DoneAToTheMajority=False,
                    NumberOfPeople=2)
        yield Kebab(Type='Chicken',
                    Action='Wait',
                    DegreeOfRoastiness=2,
                    AlreadyTurnedOver=False,
                    PartyReady=True,
                    DoneOnOneSide=True,
                    DoneOnBothSides=False,
                    BothSideReady=False,
                    Time=10,
                    DoneAToTheMajority=False,
                    NumberOfPeople=2)
        yield Kebab(Type='Chicken',
                    Action='Wait',
                    DegreeOfRoastiness=2,
                    AlreadyTurnedOver=False,
                    PartyReady=True,
                    DoneOnOneSide=True,
                    DoneOnBothSides=False,
                    BothSideReady=False,
                    Time=15,
                    DoneAToTheMajority=False,
                    NumberOfPeople=2)

    @Rule(Kebab(Type='Pork'))
    def FindPorkMeat(self):
        """
        Правило знайти факт де тип м'яса - Свинина

        :return: Found
        :rtype: str
        """
        print('Found')
        return self.facts

    @Rule(Kebab(Type='Pork', Time=15, Action='Wait'))
    def EditAction(self):
        """
        Edit Fact where type Pork, time 15, action wait
        """
        fact_id = int(input(f'{self.facts}\nChange\tfact\tand\tenter\tfact_id:\n'))
        return self.declare(self.modify(self.facts[fact_id], Action='Rotate')), print(self.facts)
