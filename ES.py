
from experta.fact import Fact, Field


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
    Type = Field(str, mandatory=True, default='')
    Action = Field(str, mandatory=True, default='')
    DegreeOfRoastiness = Field(int, mandatory=True, default=0)
    AlreadyTurnedOver = Field(bool, mandatory=True, default=False)
    PartyReady = Field(bool, mandatory=True, default=False)
    DoneOnOneSide = Field(bool, mandatory=True, default=False)
    DoneOnBothSides = Field(bool, mandatory=True, default=False)
    BothSideReady = Field(bool, mandatory=True, default=False)
    Time = Field(int, mandatory=True, default=0)
    DoneAToTheMajority = Field(bool, mandatory=True, default=False)
    NumberOfPeople = Field(int, mandatory=True, default=0)
