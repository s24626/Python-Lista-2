while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Dzielenie bez reszty")
    print("6. Modulo")
    print("7. Pierwiastek kwadratowy")
    print("8. Potęga")
    print("9. Wyjście")

    wybor = int(input("Podaj numer operacji: "))

    if wybor == 9:
        print("Koniec programu.")
        break

    if wybor in [1, 2, 3, 4, 5, 6, 8]:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

    if wybor == 1:
        wynik = a + b
        print("Wynik: ", wynik)
    elif wybor == 2:
        wynik = a - b
        print("Wynik: ", wynik)
    elif wybor == 3:
        wynik = a * b
        print("Wynik: ", wynik)
    elif wybor == 4:
        if b != 0:
            wynik = a / b
            print("Wynik: ", wynik)
        else:
            print("Nie można dzielić przez zero.")
    elif wybor == 5:
        if b != 0:
            wynik = a // b
            print("Wynik: ", wynik)
        else:
            print("Nie można dzielić przez zero.")
    elif wybor == 6:
        if b != 0:
            wynik = a % b
            print("Wynik: ", wynik)
        else:
            print("Nie można dzielić przez zero.")
    elif wybor == 7:
        wynik = a ** 0.5
        print("Wynik: ", wynik)
    elif wybor == 8:
        wynik = a ** b
        print("Wynik: ", wynik)
    else:
        print("Nieprawidłowy wybór operacji.")