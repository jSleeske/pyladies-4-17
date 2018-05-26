'''
Programowanie obiektowe (ang. object-oriented programming)
– paradygmat programowania, w którym programy definiuje się
za pomocą obiektów – elementów łączących stan (czyli dane,
nazywane najczęściej polami) i zachowanie (czyli procedury,
tu: metody). Obiektowy program komputerowy wyrażony jest jako
zbiór takich obiektów, komunikujących się pomiędzy sobą w celu
wykonywania zadań.
                                                [wikipedia.pl]

...czyli tworzymy pewne obiekty, które przechowują informacje o
danych jak i o funkcjach za pomocą których na tych danych można
operować. Istnieje powiązanie pomiędzy danymi i funkcjami!

Ale to w sumie nic nikomu nie mówi!
Zacznijmy więc od przykładu!


Na początku była klasa...
'''


class Person:
    pass


'''
Potem stworzona została instancja klasy Person - człowiek
'''
human = Person()

'''
Nadaliśmy mu imię!
'''
human.name = 'John'

'''
I nazwisko!
'''
human.surname = 'Kowalski'

'''
Potem powiedzieliśmy mu, że jest stary
'''
human.age = 70

'''
Na samym końcu go przedstawiliśmy
'''
print(f"Hi! My name is {human.name} {human.surname}",
      f"and I'm {human.age} years old."
      )

'''
A potem stwierdziliśmy, że w sumie to nie podoba nam się jego imię.
Więc je zmieniliśmy.
'''

human.name = 'Marcin'
print(f"Hi! My name is {human.name} {human.surname}",
      f"and I'm {human.age} years old."
      )
