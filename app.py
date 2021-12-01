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
            num = int(input('Fact Number: '))
            e.retract(numoffact)
        elif modify and numoffact:
            num = int(input('Fact Number: '))
            Type = str(input(f'Type\tof\tmeat:\n1.\tPork\t2.\tOstrich\t3.\tKangaroo\t4.\tChicken\nChoice:\t{str}\t-\t'))
            Action = str(input(f'Action:\n1.\tWait\t2.\tRotate\t3.\tTake\nChoice:\t{str}\t-\t'))
            DegreeOfRoastiness = int(input(f'Degree\tOf\tRoastiness:\n1.\tRoasted\t'
                                           f'2.\tCheese\t3.\tStarted\tRoasted\t4.\tBurned\nChoice:\t{int}\t-\t'))
            AlreadyTurnedOver = bool(input(f'Already\tTurned\tOver:\nEmpty.\tNo\t1.\tYes\nChoice:\t{bool}\t-\t'))
            args = dict(Type=Type, Action=Action, DegreeOfRoastiness=DegreeOfRoastiness,
                        AlreadyTurnedOver=AlreadyTurnedOver)
            e.declare(e.modify(e.facts[num], Type=args.get('Type'), Action=args.get('Action'),
                               DegreeOfRoastiness=args.get('DegreeOfRoastiness'),
                               AlreadyTurnedOver=args.get('AlreadyTurnedOver')))
            print(e.facts)
        elif modify and numoffact and rules:
            num = int(input('Fact Number: '))
            Type = str(input(f'Type\tof\tmeat:\n1.\tPork\t2.\tOstrich\t3.\tKangaroo\t4.\tChicken\nChoice:\t{str}\t-\t'))
            Action = str(input(f'Action:\n1.\tWait\t2.\tRotate\t3.\tTake\nChoice:\t{str}\t-\t'))
            DegreeOfRoastiness = int(input(f'Degree\tOf\tRoastiness:\n1.\tRoasted\t'
                                           f'2.\tCheese\t3.\tStarted\tRoasted\t4.\tBurned\nChoice:\t{int}\t-\t'))
            AlreadyTurnedOver = bool(input(f'Already\tTurned\tOver:\nEmpty.\tNo\t1.\tYes\nChoice:\t{bool}\t-\t'))
            args = dict(Type=Type, Action=Action, DegreeOfRoastiness=DegreeOfRoastiness,
                        AlreadyTurnedOver=AlreadyTurnedOver)
            e.declare(e.modify(e.facts[num], Type=args.get('Type'), Action=args.get('Action'),
                               DegreeOfRoastiness=args.get('DegreeOfRoastiness'),
                               AlreadyTurnedOver=args.get('AlreadyTurnedOver')))
            print(e.facts)
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
            num = int(input('Fact Number: '))
            e.retract(numoffact)
        elif modify and numoffact:
            num = int(input('Fact Number: '))
            Type = str(input(f'Type\tof\tmeat:\n1.\tPork\t2.\tOstrich\t3.\tKangaroo\t4.\tChicken\nChoice:\t{str}\t-\t'))
            Action = str(input(f'Action:\n1.\tWait\t2.\tRotate\t3.\tTake\nChoice:\t{str}\t-\t'))
            DegreeOfRoastiness = int(input(f'Degree\tOf\tRoastiness:\n1.\tRoasted\t'
                                           f'2.\tCheese\t3.\tStarted\tRoasted\t4.\tBurned\nChoice:\t{int}\t-\t'))
            AlreadyTurnedOver = bool(input(f'Already\tTurned\tOver:\nEmpty.\tNo\t1.\tYes\nChoice:\t{bool}\t-\t'))
            args = dict(Type=Type, Action=Action, DegreeOfRoastiness=DegreeOfRoastiness,
                        AlreadyTurnedOver=AlreadyTurnedOver)
            e.declare(e.modify(e.facts[num], Type=args.get('Type'), Action=args.get('Action'),
                               DegreeOfRoastiness=args.get('DegreeOfRoastiness'),
                               AlreadyTurnedOver=args.get('AlreadyTurnedOver')))
            print(e.facts)
        elif modify and numoffact and rules:
            num = int(input('Fact Number: '))
            Type = str(input(f'Type\tof\tmeat:\n1.\tPork\t2.\tOstrich\t3.\tKangaroo\t4.\tChicken\nChoice:\t{str}\t-\t'))
            Action = str(input(f'Action:\n1.\tWait\t2.\tRotate\t3.\tTake\nChoice:\t{str}\t-\t'))
            DegreeOfRoastiness = int(input(f'Degree\tOf\tRoastiness:\n1.\tRoasted\t'
                                           f'2.\tCheese\t3.\tStarted\tRoasted\t4.\tBurned\nChoice:\t{int}\t-\t'))
            AlreadyTurnedOver = bool(input(f'Already\tTurned\tOver:\nEmpty.\tNo\t1.\tYes\nChoice:\t{bool}\t-\t'))
            args = dict(Type=Type, Action=Action, DegreeOfRoastiness=DegreeOfRoastiness,
                        AlreadyTurnedOver=AlreadyTurnedOver)
            e.declare(e.modify(e.facts[num], Type=args.get('Type'), Action=args.get('Action'),
                               DegreeOfRoastiness=args.get('DegreeOfRoastiness'),
                               AlreadyTurnedOver=args.get('AlreadyTurnedOver')))
            print(e.facts)
            e.run()
        elif clear:
            e.facts.clear()
        elif rules:
            e.run()
            e.avarage(0, 30)
            e.avarage3(0, 10, 30)


if __name__ == "__main__":
    engine = int(input(f'Engine:\n1.\tDefFacts\n2.\tAsserts\nChoice:\t{int}\t-\t'))
    delete = bool(input(f'Delete\tFact:\nEmpty.\tNo\n1.\tYes\nChoice:\t{int}\t-\t'))
    modify = bool(input(f'Modify:\nEmpty.\tNo\n1.\tYes\nChoice:\t{int}\t-\t'))
    clear = bool(input(f'Clear:\nEmpty.\tNo\n1.\tYes\nChoice:\t{int}\t-\t'))
    rules = bool(input(f'Rules:\nEmpty.\tNo\n1.\tYes\nChoice:\t{int}\t-\t'))
    print(f'Engine:\t{engine}\nDelete:\t{delete}\nModify:\t{modify}\nClear:\t{clear}\nRules:\t{rules}')
    if delete or modify or clear or rules:
        numoffact = True
        start(engine, modify=modify, numoffact=numoffact, delfacts=delete, clear=clear, rules=rules)