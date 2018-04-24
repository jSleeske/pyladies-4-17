'''
Działanie które przedstawianie jest czasami w opozycji do
dziedziczenia to agregacja. Dziedziczenie oznacza tworzenie
bardziej szczegółowych podtypów, to agrecja oznacza tworzenie
nowych podtypów z istniejących.

Spójrzy na ten przykład
'''

'''
class Person:
    def __init__(self, first_name, last_name, email, street,
                 local_number, postal_code, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        # Czy te informacje na pewno tutaj należą?
        # Jeśli tak to w jakiej formie?
        self.street = street
        self.local_number = local_number
        self.postal_code = postal_code
        self.city = city
        self.country = country
'''

'''
Pamiętajmy, że obiekty to logicznie spójne dane + metody,
które możne na nich wykonać. W powyższym przykładzie dane
adresowe z jednej strony na pewno są informacją o użytkowniku
natomiast logicznie można je odseparować i przekazać jako gotowy
obiekt.
'''


class Address:
    def __init__(self, street, local_number, postal_code, city, country):
        self.street = street
        self.local_number = local_number
        self.postal_code = postal_code
        self.city = city
        self.country = country

    def __str__(self):
        return (f'{self.local_number} {self.street}, '
                f'{self.postal_code} {self.city}, {self.country}')

    # Oraz cała inna logika związana z adresem, na przykład
    # sprawdzanie, czy w dane miejsce doręczamy przesyłki (Amazon)
    def is_location_supported(self):
        return self.country == 'USA'


class Person:
    def __init__(self, first_name, last_name, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address

    # 'Owijamy' w ładne funkcje logikę zawartą w klasie Address
    def get_address(self):
        return self.address

    def can_purchase(self):
        return self.address.is_location_supported()


if __name__ == '__main__':
    address = Address(
        street='Portland Place',
        local_number=47,
        postal_code='W1B 1JH',
        city='London',
        country='England'
    )

    person = Person(
        first_name='John',
        last_name='Smith',
        email='john.smith@mail.com',
        address=address,
    )

    print(person.get_address())
    can_purchase = person.can_purchase()
    if can_purchase:
        print('Shipment address supported, proceeding to payments...')
    else:
        print('Sorry, currently we do not ship to your location :(')
