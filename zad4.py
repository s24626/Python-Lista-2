import hashlib

class Uwierzytelnienie:
    def __init__(self):
        self.token = None
        self.dane_uzytkownika = {}

    def generuj_token(self, imie, nazwisko, email, data_waznosci):
        dane = imie + nazwisko + email + data_waznosci
        self.token = hashlib.sha256(dane.encode()).hexdigest()

        self.dane_uzytkownika = {
            'Imię': imie,
            'Nazwisko': nazwisko,
            'E-mail': email,
            'Data ważności': data_waznosci
        }

    def sprawdz_token(self, token):
        if self.token is None:
            return False

        return token == self.token

uwierzytelnienie = Uwierzytelnienie()

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
email = input("Podaj adres e-mail: ")
data_waznosci = input("Podaj datę ważności tokena: ")

uwierzytelnienie.generuj_token(imie, nazwisko, email, data_waznosci)

print("Wygenerowany token: ", uwierzytelnienie.token)

token_sprawdzanie = input("Podaj token do sprawdzenia: ")

if uwierzytelnienie.sprawdz_token(token_sprawdzanie):
    print("Token jest prawidłowy. Dane użytkownika:")
    for key, value in uwierzytelnienie.dane_uzytkownika.items():
        print(key + ':', value)
else:
    print("Token jest nieprawidłowy.")