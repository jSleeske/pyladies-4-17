'''
Zapewne spotkaliście się już z takim zapisem:

>>> if __name__ == '__main__':
>>>     ...

Ma ono zazwyczaj bardzo specyficzną funkcję.
Żeby ją zrozumieć, musicie sobie przypomnieć,
co się dzieje kiedy uruchamiamy plik Pythonowy.

A co się dzieje?
Wykonywany jest kod!

W ustalonej kolejności?
Tak! Od góry do dołu!

A co z funkcjami?
'Wykonanie' kodu funkcji przy uruchomieniu
programu będzie polegało na tym, że funkcja
zostanie wczytana do pamięci i kod, który
znajdzie się poniżej w pliku będzie mógł z niej
korzystać.

Takie coś nie zadziała, bo w momencie wywołania
funkcji my_func nie będzie ona jeszcze wczytana
do pamięci!
>>> my_func()
>>> def my_func():
>>>     print('Hello!')

Takie coś już na szczęście zadziała!
>>> def my_func():
>>>     print('Hello!')
>>> my_func()

Ale to tak na marginesie.

Teraz załóżmy, że napisaliśmy kod, który oblicza średnia
długość życia gacka brunatnego (takiego nietoperza) na
podstawie średniej temperatury powietrza w Argentynie
w latach 1989-1993.

Umieściliśmy go w pliku program/kod_v1.py.

Kiedy odpalimy nasz program wszystko zadziała, i to jeszcze jak! ^^

Pewnego dnia przyszedł do nas jednak kolega-biolog
i mówi:
- Hej, słyszałem, że napisałeś fajną bilbioteczkę do wyliczania
  średniej długości życia gacków na podstawie średniej wartości
  temperatur w Argentynie w latach 89-93. Mógłbym z niej skorzystać?

Nie zastanwiając się długo, odpowiadasz, że nie ma problemu i jeszcze
tego samego dnia wysyłasz koledze kod.

Kolega dodaje sobie Twój folder do swojego projektu, po czym go
importuje, aliasując sobie kod_v1 jako bat_code, tak, żeby uniknąć
konfliktu nazw:

>>> from program import kod_v1 as bat_code  # noqa
>>> print(bat_code.calculate_average_bat_lifespan(temp=15))

Jakie jest jego zdziwienie, kiedy, zamiast móc korzystać od razu z
funkcji calculate_average_bat_lifespan musiał odczekać, aż wykona się
cały kod z pliku kod_v1!

W piątek po 23 (w końcu jest biologiem) pisze do Ciebie:
- Hej, mam problem. Zaimportowałem sobie kod z pliku kod_v1,
  ale zamiast móc korzystać tylko z funkcji calculate_average_bat_lifespan
  musiałem czekać aż wykona się cały kod w Twoim pliku. Dałoby się coś
  zrobić, tak, żeby przy importowaniu kodu jako modułu nie odpalała się całość?

Tutaj z pomocą przychodzi magiczny IF.
Przerzucasz cały kod, który nie powinien być wykonywany przy imporcie do niego
i jako kod_v2 wysyłasz koledze. Jest 1 w nocy...
'''

from program import kod_v2 as bat_code  # noqa
print(bat_code.calculate_average_bat_lifespan(temp=15))

'''
Tak! Sukces!
Jest 1:30 i wszystko jest tak jak powinno być!

Ale dlaczego właściwie?
I co to jest ta zmienna __name__?

Jak sama jej nazwa wskazuje (zawiera dwa podkreślniki na początku i na końcu)
jest to tak zwana zmienna magiczna. Każdy plik pythonowy będzie miał swoją
zmienną __main__ ze swoją specyficzną wartością. Taka prawidziwie magiczna,
zarezerwowana i ustawiana w momencie uruchomieniu kodu (poprzez bezpośrednie
uruchomienie pliku lub zaimportowanie go z innego pliku).
Może przyjąć dwie wartości:

1. wartość '__main__' jeśli plik zostanie wywołany bezpośrednio, np z konsoli:
    $ python program/kod_v2.py

2. wartość <nazwa_pliku_w którym się znajduje>, jeśli ten plik zostanie
zaimportowany z innego kawałka kodu:
    from program import kod_v2


Jak to sobie sprawdzić?
Uruchom plik test.py
Raz bezpośrednio, a raz odkomentowując poniższą linijkę
'''

# import test  # noqa
