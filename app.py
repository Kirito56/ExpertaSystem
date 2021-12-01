from ES import Kebab
from DefFact import DefFact
from Asserts import Asserts


def start(engine: int,
          delfacts: bool = False,
          numoffact: bool = False,
          modify: bool = False,
          clear: bool = False,
          rules: bool = False):
    if engine == 1:
        e = DefFact()
        e.reset()
        e.init_kebab()
        if delfacts and numoffact:
            num = int(input('Виберіть вакт для видалення: '))
            import pathlib, os
            pathlib.Path.unlink(f'{os.getcwd()}/ES/ES{num}.json')
            e.retract(num)
        elif modify and numoffact:
            num = int(input('Виберіть факт щоб змінити на випадкове значення: '))
            import random
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
            e.declare(e.modify(e.facts[num], Type=Type,
                                Action=Action,
                                DegreeOfRoastiness=DegreeOfRoastiness,
                                AlreadyTurnedOver=AlreadyTurnedOver,
                                PartyReady=PartyReady,
                                DoneOnOneSide=DoneOnOneSide,
                                DoneOnBothSides=DoneOnBothSides, 
                                BothSideReady=BothSideReady, Time=Time, DoneAToTheMajority=DoneAToTheMajority,
                                NumberOfPeople=NumberOfPeople))
            Kebab.write_to_file(num,Type,Action,DegreeOfRoastiness,AlreadyTurnedOver,PartyReady,DoneOnOneSide,
            DoneOnBothSides, BothSideReady, Time, DoneAToTheMajority, NumberOfPeople)
        elif modify and numoffact and rules:
            num = int(input('Виберіть факт щоб змінити на випадкове значення: '))
            import random
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
            e.declare(e.modify(e.facts[num], Type=Type,
                                Action=Action,
                                DegreeOfRoastiness=DegreeOfRoastiness,
                                AlreadyTurnedOver=AlreadyTurnedOver,
                                PartyReady=PartyReady,
                                DoneOnOneSide=DoneOnOneSide,
                                DoneOnBothSides=DoneOnBothSides, 
                                BothSideReady=BothSideReady, Time=Time, DoneAToTheMajority=DoneAToTheMajority,
                                NumberOfPeople=NumberOfPeople))
            Kebab.write_to_file(num,Type,Action,DegreeOfRoastiness,AlreadyTurnedOver,PartyReady,DoneOnOneSide,
            DoneOnBothSides, BothSideReady, Time, DoneAToTheMajority, NumberOfPeople)
            e.run()
        elif clear:
            e.facts.clear()
        elif rules:
            e.run()
            e.avarage(0, 30)
            e.avarage3(0, 10, 30)
    elif engine == 2:
        e = Asserts()
        e.reset()
        e.init_kebab()
        if delfacts and numoffact:
            num = int(input('Виберіть вакт для видалення: '))
            import pathlib, os
            pathlib.Path.unlink(f'{os.getcwd()}/ES/ES{num}.json')
            e.retract(num)
        elif modify and numoffact:
            num = int(input('Виберіть факт щоб змінити на випадкове значення: '))
            import random
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
            e.declare(e.modify(e.facts[num], Type=Type,
                                Action=Action,
                                DegreeOfRoastiness=DegreeOfRoastiness,
                                AlreadyTurnedOver=AlreadyTurnedOver,
                                PartyReady=PartyReady,
                                DoneOnOneSide=DoneOnOneSide,
                                DoneOnBothSides=DoneOnBothSides, 
                                BothSideReady=BothSideReady, Time=Time, DoneAToTheMajority=DoneAToTheMajority,
                                NumberOfPeople=NumberOfPeople))
            Kebab.write_to_file(num,Type,Action,DegreeOfRoastiness,AlreadyTurnedOver,PartyReady,DoneOnOneSide,
            DoneOnBothSides, BothSideReady, Time, DoneAToTheMajority, NumberOfPeople)
        elif modify and numoffact and rules:
            num = int(input('Виберіть факт щоб змінити на випадкове значення: '))
            import random
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
            e.declare(e.modify(e.facts[num], Type=Type,
                                Action=Action,
                                DegreeOfRoastiness=DegreeOfRoastiness,
                                AlreadyTurnedOver=AlreadyTurnedOver,
                                PartyReady=PartyReady,
                                DoneOnOneSide=DoneOnOneSide,
                                DoneOnBothSides=DoneOnBothSides, 
                                BothSideReady=BothSideReady, Time=Time, DoneAToTheMajority=DoneAToTheMajority,
                                NumberOfPeople=NumberOfPeople))
            Kebab.write_to_file(num,Type,Action,DegreeOfRoastiness,AlreadyTurnedOver,PartyReady,DoneOnOneSide,
            DoneOnBothSides, BothSideReady, Time, DoneAToTheMajority, NumberOfPeople)
            e.run()
        elif clear:
            e.facts.clear()
        elif rules:
            e.run()
            e.avarage(0, 30)
            e.avarage3(0, 10, 30)


if __name__ == "__main__":
    engine = int(input(f'Engine:\n1.\tDefFacts\n2.\tAsserts\nВаш вибір:\t{int}\t-\t'))
    delete = bool(input(f'Delete\tFact:\nEmpty.\tNo\n1.\tYes\nВаш вибір:\t{int}\t-\t'))
    modify = bool(input(f'Modify:\nEmpty.\tNo\n1.\tYes\nВаш вибір:\t{int}\t-\t'))
    clear = bool(input(f'Clear:\nEmpty.\tNo\n1.\tYes\nВаш вибір:\t{int}\t-\t'))
    rules = bool(input(f'Rules:\nEmpty.\tNo\n1.\tYes\nВаш вибір:\t{int}\t-\t'))
    print(f'Engine:\t{engine}\nВидалення:\t{delete}\nРедагування:\t{modify}\nОчищення:\t{clear}\nПравила:\t{rules}')
    if delete or modify or clear or rules:
        numoffact = True
        start(engine, modify=modify, numoffact=numoffact, delfacts=delete, clear=clear, rules=rules)