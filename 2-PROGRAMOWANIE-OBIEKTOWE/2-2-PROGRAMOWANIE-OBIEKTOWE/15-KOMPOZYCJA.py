'''
Kolejnym bardzo ważnym pojęciem jeśli chodzi o programowanie obiektowe jest
kompozycja. Polega na tym, ze zamiast dziedziczyć 'składamy' obiekt z innych.


>>> class User:
>>>     def __init__(self,
>>>                  first_name,
>>>                  last_name,
>>>                  birth_date,
>>>                  gender,
>>>                  twitter_handler,
>>>                  facebook_handler,
>>>                  street,
>>>                  locale_number,
>>>                  postcode,
>>>                  city,
>>>                  country):

>>>         self.first_name = first_name
>>>         self.last_name = last_name
>>>         self.birth_date = birth_date
>>>         self.gender = gender
>>>         self.twitter_handler = twitter
>>>         self.facebook_handler = facebook
>>>         self.street = street
>>>         self.locale_number = locale_number
>>>         self.postcode = postcode
>>>         self.city = city
>>>         self.country = country

>>>     def get_address(self):
>>>         return (f'{self.street} {self.locale_number},'
>>>             f' {self.postcode} {self.city}, {self.country}')

>>>     def post_on_social_profiles(self, msg):
>>>         self._post_on_facebook(msg)
>>>         self._post_on_twitter(msg)

>>>     def _post_on_facebook(self, msg):
>>>         print('Posting message in the name of'
>>>               f' Facebook user {self.facebook_handler}')

>>>     def _post_on_twitter(self, msg):
>>>         print('Posting message in the name of'
>>>               f' Twitter user {self.twitter_handler}')

Jak widać powyżej, nasz użytkownik jest bardzo zagracony, co więcej, jeśli
na przykład postanowimy dodać nowe serwisy społecznościowe, to sytuacja
się pogorszy - bardzo szybko i bardzo mocno.
Chociaż niewątpliwie, wszystkich tych danych i metod potrzebujemy, być może
da się je rozbić na mniejsze części i stworzyć z nich 'puzzle':
'''


class SocialProfile:
    def __init__(self, identifier):
        self.identifier = identifier

    def post_message(self, msg):
        raise NotImplementedError('Not implemented')


class Facebook(SocialProfile):
    def post_message(self, msg):
        print('Posting message in the name of'
              f' Facebook user {self.identifier}\n {msg}')


class Twitter(SocialProfile):
    def post_message(self, msg):
        print('Posting message in the name of'
              f' Twitter user {self.identifier}: \n {msg}')


class Social:
    def __init__(self, *args):
        self._social_profiles = list(args)

    def post_message(self, msg):
        for profile in self._social_profiles:
            if isinstance(profile, SocialProfile):
                '''
                isinstance zwraca True, jeśli klasa danego obiektu to
                SocialProfile lub klasa dziedzicząca z SocialProfile.
                Dzięki temu mamy pewność, że możemy na obiekcie profile wywołać
                metodę post_message() i nic nam się nie wykrzaczy ;)
                '''
                profile.post_message(msg)

    def add_social_profile(self, profile):
        self._social_profiles.append(profile)


class Address:
    def __init__(self,
                 street,
                 locale_number,
                 postcode,
                 city,
                 country):
        self.street = street
        self.locale_number = locale_number
        self.postcode = postcode
        self.city = city
        self.country = country

    def __str__(self):
        return (f'{self.street} {self.locale_number}, '
                f'{self.postcode} {self.city}, {self.country}')


class User:
    def __init__(self,
                 first_name,
                 last_name,
                 birth_date,
                 gender,
                 social,
                 address):

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.social = social
        self.address = address

    def get_address(self):
        return self.address

    def change_address(self, address):
        self.address = address

    def post_message(self, msg):
        self.social.post_message(msg)

    def add_social_profile(self, profile):
        self.social.add_social_profile(profile)


social = Social(
    Twitter('@john.doe'),
)

address = Address(
    street='Niestachowska',
    locale_number=55,
    postcode='60-655',
    city='Poznań',
    country='Polska',
)

user = User(
    'John',
    'Doe',
    '12-12-1990',
    'male',
    social=social,
    address=address,
)

print(user.get_address())

user.post_message(f'{user.first_name} just joined hornypotatoes.com!')

user.add_social_profile(Facebook('john.doe.552'))

user.post_message('Now we are just spamming!')


'''
Cały powyższy przykład jest nieco zagmatwany, ale po kolei:

Mamy nastepujące klasy:

- SocialProfile
    - Facebook
    - Twitter

- Social

- Address

- User


Klasa User składa się z podstawowych atrybutów użytkownika:
imienia, nazwisko, daty urodzenia, płci, obiektu adres, przechowującego
adres użytkownika, oraz obieku klasy Social przechowującego obiekty
dziedziczące po klasie SocialProfile.

Jak widać, użytkownik nadal udostępnia interfejs do zarządzania swoim profilem,
na przykład metody:
    change_address(),
    get_address(),
    post_message(),
    add_profile()
natomiast cała ich funkcja polega na wywołaniu odpowiedniej metody w obiekcie
stanowiącym część kompozycji, gdzie ma miejsce cała logika. Dzięki temu
klasa User pozostaje relatywnie czysta i zwięzła.

Jeśli chcemy wstawić w imieniu użytkownika wiadomość powitalną na wszystkich
możliwych serwisach, to:
- wywołujemy tylko metodę post_message() na użytkowniku, która z kolei wywołuje
metodę post_message() obiektu klasy Social, który z kolei wywołuje metody
post_message() dla każdego obiektu w swojej liście _social_profiles. W tych
metodach znajduje się cała logika odpowiedzialna za szczegóły wysłania
użytkownikowi wiadomości na danym serwisie i te detale nas nie interesują.

Z naszego punktu widzenia jedyne co musieliśmy zrobić wywołać na użytkownik
metodę post_message() i podać treść wiadomości. Jeśli zechcemy dodać nowy
rodzaj profilu społecznościowego to nie ma problemu, wystarczy, że będzie
on dziedziczył po klasie SocialProfile i implementował metodę post_message().
I będzie działać, po prostu ;)
'''
