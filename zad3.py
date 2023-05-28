plansza = [[' ']*3 for _ in range(3)]
gracz = 'X'

while True:
    print("Aktualny stan planszy:")
    for row in plansza:
        for cell in row:
            print(cell, end=" | ")
        print("\n-----------")

    ruch = input(f"Gracz {gracz}, podaj ruch (np. 1,1 dla pierwszego wiersza i pierwszej kolumny): ")
    row, col = map(int, ruch.split(','))

    if plansza[row-1][col-1] == ' ':
        plansza[row-1][col-1] = gracz
    else:
        print("Nieprawidłowy ruch. Spróbuj jeszcze raz.")
        continue

    # Sprawdź wygrane w wierszach, kolumnach i przekątnych
    for i in range(3):
        if plansza[i][0] == plansza[i][1] == plansza[i][2] == gracz or \
           plansza[0][i] == plansza[1][i] == plansza[2][i] == gracz:
            print(f"Gracz {gracz} wygrał!")
            break
    else:
        if plansza[0][0] == plansza[1][1] == plansza[2][2] == gracz or \
           plansza[0][2] == plansza[1][1] == plansza[2][0] == gracz:
            print(f"Gracz {gracz} wygrał!")
            break

    if all(all(row != ' ' for row in plansza[i]) for i in range(3)):
        print("Remis!")
        break

    gracz = 'O' if gracz == 'X' else 'X'

print("Finalny stan planszy:")
for row in plansza:
    for cell in row:
        print(cell, end=" | ")
    print("\n-----------")