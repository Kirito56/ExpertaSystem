from typing import Type
from experta.engine import KnowledgeEngine
from experta.rule import Rule
from experta.deffacts import DefFacts
from experta.conditionalelement import AND, OR, TEST
from experta.shortcuts import MATCH
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
                    NumberOfPeople=['Anton', 'Georgyi'])
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
                    NumberOfPeople=[2])
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
                    NumberOfPeople=[2])
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
                    NumberOfPeople=[2])
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
                    NumberOfPeople=[2])
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
                    NumberOfPeople=[2])

    @Rule(Kebab(Type='Pork', Time=15, Action='Wait'))
    def _chain_start(self) -> str:
        """
        Початок ланцюга

        :return: Found
        :rtype: str
        """
        facts = len(self.facts)
        for i in range(facts):
            fact = self.facts[i+1]
            if fact.get('Type') == 'Pork' and fact.get('Time') == 15 and fact.get('Action') == 'Wait':
                self.declare(self.modify(self.facts[i+1], Time=0, Action='Rotate', AlreadyTurnedOver=True))
            i += 1
        return print('Pork Found')

    @Rule(Kebab(Type='Pork', Time=0, Action='Rotate', AlreadyTurnedOver=True))
    def _chain_cont(self) -> str:
        """
        Продовження ланцюга
        :return: Modified Fact
        :rtype: Fact
        """
        facts = len(self.facts)
        for i in range(facts):
            try:
                fact = self.facts[i+1]
                if fact.get('Type') == 'Pork' and fact.get('Time') == 0 and fact.get('Action') == 'Rotate':
                    return print(f'Fact:\t{i}\nType:{fact.get("Type")}\nAction:{fact.get("Action")}\nTime:{fact.get("Time")}')
            except KeyError:
                fact = self.facts[i+2]
                if fact.get('Type') == 'Pork' and fact.get('Time') == 0 and fact.get('Action') == 'Rotate':
                    return print(f'Fact:{i}\nType:{fact.get("Type")}\nAction:{fact.get("Action")}\nTime:{fact.get("Time")}')
            i += 1

    @Rule(Kebab(NumberOfPeople=MATCH.NumberOfPeople))
    def _rule_with_using_match(self, NumberOfPeople) -> str:
        if 'Anton' in NumberOfPeople:
            return print('Yes')

    @Rule(Kebab(Time=MATCH.Time), TEST(lambda Time: Time<15))
    def _rule_with_using_test(self,  Time):
        return print( Time)