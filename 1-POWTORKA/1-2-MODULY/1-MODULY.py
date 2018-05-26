'''
W czasach przed Pythonem 3.4 aby jakiś folder traktowany
był jako moduł przez Pythona niezbędne było stworzenie w nim
pustego pliku __init__.py

Obecnie nie jest to wymagane, natomiast w pliku __init__.py
możemy (i mogliśmy) umieszczać dodatkowy kod.

Wyobraźmy sobie, że stworzyliśmy moduł z narzędziami atematycznymi.
Wszystko jest tam poukładane - stałe matematyczne są w osobnym
pliku constants.py, a funkcje liczące pola powierzchni - w pliku
aerial.py

Zwróć uwagę, że w pliku __init__.py modułu maths importujemy
funkcje z pliku aerial.py

Dzięki takiemu zabiegowi możemy odwoływać się do nich w taki sposób:
'''
from maths import (  # noqa
    calculate_circle_area,
    calculate_rectangle_area,
    calculate_triangle_area
)


'''
A nie na przykład tak:
'''
from maths.areal import calculate_circle_area  # noqa


'''
Róznica nie jest gigantyczna, ale mimo wszystko jest krócej i trochę
czytelniej. Zakładamy, że użytkownicy naszej biblioteki częściej będą
korzystali z tych funkcji niż z na przykład stałych. W taki sposób możemy
im uprościć odnalezienie w naszym kodzie tego co potrzebują.
'''
