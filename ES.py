from experta import (KnowledgeEngine, Field, Fact, Rule, DefFacts,
                     L, P, AS, OR, AND, EXISTS, NOT, FORALL)
class Kebab(Fact):
    """
    * Type - Тип м'яса
    * Action - Дія
    * DegreeOfRoasting - Ступінь піджаристості
    * AlreadyTurnedOver - Вже переверталось
    * PartyReady - Сторона готовв
    * DoneOnOneSide - Готово з однієї сторони
    * DoneOnBothSides - Готово з другої сторони
    * BothSideReady - Друга сторона готова
    * Time - Час
    * DoneAToTheMajority - Готово по думці більшості
    * NumberOfPeople - Кількість людей
    """
    Type = Field(str, mandatory=True)
    Action = Field(str, mandatory=True)
    DegreeOfRoastiness = Field(int, mandatory=True)
    AlreadyTurnedOver = Field(bool, mandatory=True)
    PartyReady = Field(bool, mandatory=True)
    DoneOnOneSide = Field(bool, mandatory=True)
    DoneOnBothSides = Field(bool, mandatory=True)
    BothSideReady = Field(bool, mandatory=True)
    Time = Field(int, mandatory=True)
    DoneAToTheMajority = Field(bool, mandatory=True)
    NumberOfPeople = Field(int, mandatory=True)