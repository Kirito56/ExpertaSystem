from experta import (KnowledgeEngine, Field, Fact, Rule, DefFacts,
                     L, P, AS, OR, AND, EXISTS, NOT, FORALL)
from ES import Kebab


class Asserts(KnowledgeEngine):
    def init_kebab(self):
        self.declare(Kebab(Type='Pork',
                           Action='Wait',
                           DegreeOfRoastiness=2,
                           AlreadyTurnedOver=False,
                           PartyReady=True,
                           DoneOnOneSide=True,
                           DoneOnBothSides=False,
                           BothSideReady=False,
                           Time=10,
                           DoneAToTheMajority=False,
                           NumberOfPeople=2))
        self.declare(Kebab(Type='Pork',
                           Action='Wait',
                           DegreeOfRoastiness=2,
                           AlreadyTurnedOver=False,
                           PartyReady=False,
                           DoneOnOneSide=True,
                           DoneOnBothSides=False,
                           BothSideReady=False,
                           Time=10,
                           DoneAToTheMajority=False,
                           NumberOfPeople=2))
