import os, datetime
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
    DegreeOfRoastiness = Field(str, mandatory=True, default=0)
    AlreadyTurnedOver = Field(bool, mandatory=True, default=False)
    PartyReady = Field(bool, mandatory=True, default=False)
    DoneOnOneSide = Field(bool, mandatory=True, default=False)
    DoneOnBothSides = Field(bool, mandatory=True, default=False)
    BothSideReady = Field(bool, mandatory=True, default=False)
    Time = Field(int, mandatory=True, default=0)
    DoneAToTheMajority = Field(bool, mandatory=True, default=False)
    NumberOfPeople = Field(list, mandatory=True, default=0)

    @staticmethod
    def write_to_file(*types) -> str:
        """[summary]

        Returns:
            [type]: [description]
        """        
        text = ('{'+
        f'\n\t"Fact-id": {types[0]},\n\t"Type": "{types[1]}",\n\t"Action": "{types[2]}",\n\t"DegreeOfRoastiness": "{types[3]}",')
        field1 = (f'\n\t"AlreadyTurnedOver": true,')
        field2 = (f'\n\t"PartyReady": true,')
        field3 = (f'\n\t"DoneOnOneSide": true,')
        field4 = (f'\n\t"DoneOnBothSides": true,')
        field5 = (f'\n\t"BothSideReady": true,')
        field6 = (f'\n\t"DoneAToTheMajority": true,')
        if not types[4]:
            field1 = field1.replace('true', 'false')
        if not types[5]:
            field2 = field2.replace('true', 'false')
        if not types[6]:
            field3 = field3.replace('true', 'false')
        if not types[7]:
            field4 = field4.replace('true', 'false')
        if not types[8]:
            field5 = field5.replace('true', 'false')
        if not types[10]:
            field6 = field6.replace('true', 'false')
        fiend7 = (f'\n\t"Time": {types[9]},')
        fiend8 = (f'\n\t"NumberOfPeople": {types[11]},\n')
        fiend8 = fiend8.replace("'", '"')
        field9 = (f'\t"Added": "{datetime.datetime.utcnow().month}/{datetime.datetime.utcnow().day}/{datetime.datetime.utcnow().year} {datetime.datetime.utcnow().hour}:{datetime.datetime.utcnow().minute}:{datetime.datetime.utcnow().second}"' + '\n},\n')
        text = text + field1 + field2 +field3+ field4 + field5 + field6 + fiend7 + fiend8 +field9
        if os.path.exists(f'{os.getcwd()}/ES'):
            if os.path.exists(f'{os.getcwd()}/ES/ES.json'):
                with open(f'{os.getcwd()}/ES/ES.json', mode='a', encoding='UTF8') as file:
                    return file.write(text)
            else:
                with open(f'{os.getcwd()}/ES/ES.json', mode='w', encoding='UTF8') as file:
                    return file.write(text)
        else:
            os.mkdir(f'{os.getcwd()}/ES')
            with open(f'{os.getcwd()}/ES/ES.json', mode='w', encoding='UTF8') as file:
                return file.write(text)

    @staticmethod
    def rules_output(*rule) -> str:
        """[summary]

        Returns:
            [type]: [description]
        """
        name = rule[0]        
        output = rule[1]        
        description = rule[2]        
        if os.path.exists(f'{os.getcwd()}/ES/rules.json'):
            with open(f'{os.getcwd()}/ES/rules.json', mode='a',encoding='UTF-8') as file:
                l0 = '{\n'
                l1 = l0 + f'\t"{name}": ' + '{\n'
                l2 = l1 + f'\t\t"{description}": "{output}"' + '\n\t\t},\n'
                field9 = (f'\t"Added": "{datetime.datetime.utcnow().month}/{datetime.datetime.utcnow().day}/{datetime.datetime.utcnow().year} {datetime.datetime.utcnow().hour}:{datetime.datetime.utcnow().minute}:{datetime.datetime.utcnow().second}"' + '\n},\n')
                return file.write(l2+field9)
        else:
            with open(f'{os.getcwd()}/ES/rules.json', mode='w',encoding='UTF-8') as file:
                l0 = '{\n'
                l1 = l0 + f'\t"{name}": ' + '{\n'
                l2 = l1 + f'\t\t"{description}": "{output}"' + '\n\t\t},\n'
                field9 = (f'\t"Added": "{datetime.datetime.utcnow().month}/{datetime.datetime.utcnow().day}/{datetime.datetime.utcnow().year} {datetime.datetime.utcnow().hour}:{datetime.datetime.utcnow().minute}:{datetime.datetime.utcnow().second}"' + '\n},\n')
                return file.write(l2+field9)
