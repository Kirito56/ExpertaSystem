from experta.engine import KnowledgeEngine
from experta.rule import Rule
from experta.deffacts import DefFacts
from experta.conditionalelement import AND

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
                    Time=10,
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
        return print('Found')

    @Rule(Kebab(Type='Chicken', Time=15),
          AND(Kebab(Type='Kangaroo', Time=15)))
    def ChickenLongFried(self):
        """
        Правило Курятина і Кенгурятина довго жариться

        :return: Rotate
        :rtype: str
        """
        return print('Rotate!')
