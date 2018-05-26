'''
Plik __init__.py był wymagany w starszych wersjach Pythona,
jeśli dany folder miał być traktowany jak pythnonowy moduł.
Obecnie nie jest on niezbędny, natomiast można go wykorzystać
do 'wystawienia' w ładny sposób kluczowych funkcji naszego modułu
'''

from .areal import (calculate_circle_area, calculate_rectangle_area,  # noqa
                    calculate_triangle_area)
