'''
Za Wikipedią:

programowanie proceduralne – paradygmat programowania zalecający
dzielenie kodu na procedury, czyli fragmenty wykonujące ściśle określone
operacje. Procedury nie powinny korzystać ze zmiennych globalnych (w miarę
możliwości), lecz pobierać i przekazywać wszystkie dane (czy też wskaźniki
do nich) jako parametry wywołania.

Czyli to co robiliśmy do tej pory. Definiujemy jakieś funkcje, które przyjmują
dane i w jakiś sposób je przetwarzają. Zwróćcie uwagę, że dane i procedury
(funkcje) nie są ze sobą ściśle powiązane. Obiekt data, który przekazujemy do
funkcji triple() moze być na przykład liczbą, ale może być też łańcuchem
znaków. Dla każdego z nich zadziała.
'''


def triple(data):
    '''
    Returns value * 3
    '''
    return data * 3


def is_even(data):
    '''
    Checks if data is even number
    '''
    return False if data % 2 else True


if __name__ == '__main__':
    data = int(input('A number, please?'))
    tripled_data = triple(data)
    is_even = is_even(tripled_data)
    print(
        f'Processed data, {tripled_data} is {"even" if is_even else "uneven"}')
