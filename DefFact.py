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

    @Rule(Kebab(Type='Ostrich'))
    def FindPorkMeat(self) -> str:
        """
        Правило знайти факт де тип м'яса - Свинина

        :return: Found
        :rtype: str
        """
        return print('Ostrich Found')

    @Rule(Kebab(Type='Pork', Time=15, Action='Wait'))
    def EditAction(self) -> str:
        """
        Edit Fact where type Pork, time 15, action wait
        :return: Modified Fact
        :rtype: Fact
        """
        facts = len(self.facts)
        for i in range(facts):
            fact = self.facts[i+1]
            if fact.get('Type') == 'Pork' and fact.get('Time') == 15 and fact.get('Action') == 'Wait':
                self.declare(self.modify(self.facts[i+1], Time=0, Action='Rotate', AlreadyTurnedOver=True))
            i += 1
        return print(self.facts)
