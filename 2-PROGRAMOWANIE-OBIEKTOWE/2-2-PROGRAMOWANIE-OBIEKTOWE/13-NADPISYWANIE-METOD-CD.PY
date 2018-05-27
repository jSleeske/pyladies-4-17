'''
W poprzednich przykładach w klasie bazowej tylko definiowaliśmy
metodę (i podnosiliśmy wyjątek, czyniąc ją de facto abstrakcyjną).

Ale nie zawsze musi tak być!
Jeśli jesteśmy przekonani o tym, że część logiki będzie wspólna dla
pewnej metody we wszystkich klasach dziedziczących to możemy umieścić
ją po prostu w klasie bazowej i wykorzystywać dzięki wywołaniu z super().
'''


class Parent:
    def do_work(self):
        print('Some common logic')


class ChildA(Parent):
    def do_work(self):
        super().do_work()
        print('Some ChildA specific logic')


class ChildB(Parent):
    def do_work(self):
        print('Some ChildB specific logic')
        super().do_work()


child_a = ChildA()
child_b = ChildB()

child_a.do_work()
print('\n\n\n')
child_b.do_work()
