from datetime import datetime as time
import os
from re import I

from sqlalchemy.sql.sqltypes import Time

from experta.fact import Fact, Field
from models.Kebab import Kebab
from models.Rules import Rules
__version__ = '1.0'

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
    
    id = Field(int, mandatory=True, default=0)
    Type = Field(str, mandatory=True, default='')
    Action = Field(str, mandatory=True, default='')
    DegreeOfRoastiness = Field(str, mandatory=True, default='')
    AlreadyTurnedOver = Field(bool, mandatory=True, default=False)
    PartyReady = Field(bool, mandatory=True, default=False)
    DoneOnOneSide = Field(bool, mandatory=True, default=False)
    DoneOnBothSides = Field(bool, mandatory=True, default=False)
    BothSideReady = Field(bool, mandatory=True, default=False)
    Time = Field(int, mandatory=True, default=0)
    DoneAToTheMajority = Field(bool, mandatory=True, default=False)
    NumberOfPeople = Field(list, mandatory=True, default=[])

    @staticmethod
    def to_json(F: Kebab, R: Rules, rule=None):
        if os.path.exists(f'{os.getcwd()}/{str("outputs.json")}'):
            with open(f'{os.getcwd()}/{str("outputs.json")}', mode='w', encoding='UTF-8') as json:
                def to_dict():
                    fact = F.get_list()
                    rule = R.get_list()
                    id=list()
                    Type=list()
                    Action=list()
                    DegreeOfRoastiness=list()
                    AlreadyTurnedOver=list()
                    PartyReady=list()
                    DoneOnOneSide=list()
                    DoneOnBothSides=list()
                    BothSideReady=list()
                    Time=list()
                    DoneAToTheMajority=list()
                    NumberOfPeople=list()
                    Added=list()
                    RuleId=list()
                    Name=list()
                    Description=list()
                    Output=list()
                    AddedR=list()
                    def true_or_false(obj):
                        if obj:
                            return "Так"
                        else:
                            return "Ні"
                    def time_to_str(obj):
                        new_obj = str(f"{obj}").replace('datetime.datetime(', '[')
                        new_obj = new_obj.replace(')', ']')
                        return new_obj
                    for o in fact:
                        id.append(o.id)
                        Type.append(o.Type)
                        Action.append(o.Action)
                        DegreeOfRoastiness.append(o.DegreeOfRoasting)
                        AlreadyTurnedOver.append(true_or_false(o.AlreadyTurnedOver))
                        PartyReady.append(true_or_false(o.PartyReady))
                        DoneOnOneSide.append(true_or_false(o.DoneOnOneSide))
                        DoneOnBothSides.append(true_or_false(o.DoneOnBothSides))
                        BothSideReady.append(true_or_false(o.BothSideReady))
                        Time.append(o.Time)
                        DoneAToTheMajority.append(true_or_false(o.DoneAToTheMajority))
                        Num = o.NumberOfPeople.split(',', 2)
                        NumberOfPeople.append(Num)
                        Added.append(time_to_str(o.Added))
                    for o in rule:
                        RuleId.append(o.RuleId)
                        Name.append(o.Name)
                        Description.append(o.Description)
                        Output.append('>>'+ o.Output)
                        AddedR.append(time_to_str(o.Added))
                    if rule:
                        out = ('{'+'"Facts": \n\t{\n\t\t' + f'"Id": {id}' + ',\n\t\t'+
                        f'"Type" : {Type}'.replace("'", '"') + ',\n\t\t' + f'"Action": {Action}'.replace("'", '"') + 
                        ',\n\t\t'+ f'"DegreeOfRoastiness": {DegreeOfRoastiness}'.replace("'", '"') +
                        ',\n\t\t' + f'"AlreadyTurnedOver": {AlreadyTurnedOver}'.replace("'", '"') +
                        ',\n\t\t' + f'"PartyReady": {PartyReady}'.replace("'", '"') + 
                        ',\n\t\t' + f'"DoneOnOneSide": {DoneOnOneSide}'.replace("'", '"') + 
                        ',\n\t\t' + f'"DoneOnBothSides": {DoneOnBothSides}'.replace("'", '"') +
                        ',\n\t\t' + f'"BothSideReady": {BothSideReady}'.replace("'", '"') +
                        ',\n\t\t' + f'"Time": {Time}' +
                        ',\n\t\t' + f'"NumberOfPeople": {NumberOfPeople}'.replace("'", '"') +
                        ',\n\t\t' + f'"Added": {Added}'.replace("'", '"') + 
                        '\n\t}' + ',\n\t' + '"Rules" :\n\t{\n\t\t' + f'"Id": {RuleId}' +
                        ',\n\t\t' + f'"Name": {Name}'.replace("'", '"') + 
                        ',\n\t\t' + f'"Description": {Description}'.replace("'", '"') +
                        ',\n\t\t' + f'"Output": {Output}'.replace("'", '"') +
                        ',\n\t\t' + f'"Added": {AddedR}'.replace("'", '"') +
                        '\n\t}' + '\n}')
                        return out
                    else:
                        out = ('{'+'"Facts": \n\t{\n\t\t' + f'"Id": {id}' + ',\n\t\t'+
                        f'"Type" : {Type}'.replace("'", '"') + ',\n\t\t' + f'"Action": {Action}'.replace("'", '"') + 
                        ',\n\t\t'+ f'"DegreeOfRoastiness": {DegreeOfRoastiness}'.replace("'", '"') +
                        ',\n\t\t' + f'"AlreadyTurnedOver": {AlreadyTurnedOver}'.replace("'", '"') +
                        ',\n\t\t' + f'"PartyReady": {PartyReady}'.replace("'", '"') + 
                        ',\n\t\t' + f'"DoneOnOneSide": {DoneOnOneSide}'.replace("'", '"') + 
                        ',\n\t\t' + f'"DoneOnBothSides": {DoneOnBothSides}'.replace("'", '"') +
                        ',\n\t\t' + f'"BothSideReady": {BothSideReady}'.replace("'", '"') +
                        ',\n\t\t' + f'"Time": {Time}' +
                        ',\n\t\t' + f'"NumberOfPeople": {NumberOfPeople}'.replace("'", '"') +
                        ',\n\t\t' + f'"Added": {Added}'.replace("'", '"') + 
                        '\n\t}' + ',\n\t' + '"Rules" :\n\t{\n\t\t' + f'"Id": "{None}"' +
                        ',\n\t\t' + f'"Name": "{None}"'.replace("'", '"') + 
                        ',\n\t\t' + f'"Description": "{None}"'.replace("'", '"') +
                        ',\n\t\t' + f'"Output": "{None}"'.replace("'", '"') +
                        ',\n\t\t' + f'"Added": "{None}"'.replace("'", '"') +
                        '\n\t}' + '\n}')
                        return out
                json.write(to_dict())
        else:
            with open(f'{os.getcwd()}/{str("outputs.json")}', mode='w', encoding='UTF-8') as json:
                def to_dict():
                    fact = F.get_list()
                    rule = R.get_list()
                    id=list()
                    Type=list()
                    Action=list()
                    DegreeOfRoastiness=list()
                    AlreadyTurnedOver=list()
                    PartyReady=list()
                    DoneOnOneSide=list()
                    DoneOnBothSides=list()
                    BothSideReady=list()
                    Time=list()
                    DoneAToTheMajority=list()
                    NumberOfPeople=list()
                    Added=list()
                    RuleId=list()
                    Name=list()
                    Description=list()
                    Output=list()
                    AddedR=list()
                    def true_or_false(obj):
                        if obj:
                            return "Так"
                        else:
                            return "Ні"
                    def time_to_str(obj):
                        new_obj = str(f"{obj}").replace('datetime.datetime(', '[')
                        new_obj = new_obj.replace(')', ']')
                        return new_obj
                    for o in fact:
                        id.append(o.id)
                        Type.append(o.Type)
                        Action.append(o.Action)
                        DegreeOfRoastiness.append(o.DegreeOfRoasting)
                        AlreadyTurnedOver.append(true_or_false(o.AlreadyTurnedOver))
                        PartyReady.append(true_or_false(o.PartyReady))
                        DoneOnOneSide.append(true_or_false(o.DoneOnOneSide))
                        DoneOnBothSides.append(true_or_false(o.DoneOnBothSides))
                        BothSideReady.append(true_or_false(o.BothSideReady))
                        Time.append(o.Time)
                        DoneAToTheMajority.append(true_or_false(o.DoneAToTheMajority))
                        Num = o.NumberOfPeople.split(',', 2)
                        NumberOfPeople.append(Num)
                        Added.append(time_to_str(o.Added))
                    for o in rule:
                        RuleId.append(o.RuleId)
                        Name.append(o.Name)
                        Description.append(o.Description)
                        # Outputs = o.Output.replace('frozenlist([', '')
                        # Outputs = Outputs.replace('])', '')
                        Output.append('>>'+ o.Output)
                        AddedR.append(time_to_str(o.Added))
                    if rule:
                        out = ('{'+'"Facts": \n\t{\n\t\t' + f'"Id": {id}' + ',\n\t\t'+
                        f'"Type" : {Type}'.replace("'", '"') + ',\n\t\t' + f'"Action": {Action}'.replace("'", '"') + 
                        ',\n\t\t'+ f'"DegreeOfRoastiness": {DegreeOfRoastiness}'.replace("'", '"') +
                        ',\n\t\t' + f'"AlreadyTurnedOver": {AlreadyTurnedOver}'.replace("'", '"') +
                        ',\n\t\t' + f'"PartyReady": {PartyReady}'.replace("'", '"') + 
                        ',\n\t\t' + f'"DoneOnOneSide": {DoneOnOneSide}'.replace("'", '"') + 
                        ',\n\t\t' + f'"DoneOnBothSides": {DoneOnBothSides}'.replace("'", '"') +
                        ',\n\t\t' + f'"BothSideReady": {BothSideReady}'.replace("'", '"') +
                        ',\n\t\t' + f'"Time": {Time}' +
                        ',\n\t\t' + f'"NumberOfPeople": {NumberOfPeople}'.replace("'", '"') +
                        ',\n\t\t' + f'"Added": {Added}'.replace("'", '"') + 
                        '\n\t}' + ',\n\t' + '"Rules" :\n\t{\n\t\t' + f'"Id": {RuleId}' +
                        ',\n\t\t' + f'"Name": {Name}'.replace("'", '"') + 
                        ',\n\t\t' + f'"Description": {Description}'.replace("'", '"') +
                        ',\n\t\t' + f'"Output": {Output}'.replace("'", '"') +
                        ',\n\t\t' + f'"Added": {AddedR}'.replace("'", '"') +
                        '\n\t}' + '\n}')
                        return out
                    else:
                        out = ('{'+'"Facts": \n\t{\n\t\t' + f'"Id": {id}' + ',\n\t\t'+
                        f'"Type" : {Type}'.replace("'", '"') + ',\n\t\t' + f'"Action": {Action}'.replace("'", '"') + 
                        ',\n\t\t'+ f'"DegreeOfRoastiness": {DegreeOfRoastiness}'.replace("'", '"') +
                        ',\n\t\t' + f'"AlreadyTurnedOver": {AlreadyTurnedOver}'.replace("'", '"') +
                        ',\n\t\t' + f'"PartyReady": {PartyReady}'.replace("'", '"') + 
                        ',\n\t\t' + f'"DoneOnOneSide": {DoneOnOneSide}'.replace("'", '"') + 
                        ',\n\t\t' + f'"DoneOnBothSides": {DoneOnBothSides}'.replace("'", '"') +
                        ',\n\t\t' + f'"BothSideReady": {BothSideReady}'.replace("'", '"') +
                        ',\n\t\t' + f'"Time": {Time}' +
                        ',\n\t\t' + f'"NumberOfPeople": {NumberOfPeople}'.replace("'", '"') +
                        ',\n\t\t' + f'"Added": {Added}'.replace("'", '"') + 
                        '\n\t}' + ',\n\t' + '"Rules" :\n\t{\n\t\t' + f'"Id": "{None}"' +
                        ',\n\t\t' + f'"Name": "{None}"'.replace("'", '"') + 
                        ',\n\t\t' + f'"Description": "{None}"'.replace("'", '"') +
                        ',\n\t\t' + f'"Output": "{None}"'.replace("'", '"') +
                        ',\n\t\t' + f'"Added": "{None}"'.replace("'", '"') +
                        '\n\t}' + '\n}')
                        return out
                json.write(to_dict())