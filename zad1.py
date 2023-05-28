
a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))
c = int(input("Podaj trzecią liczbę całkowitą: "))

for _ in range(a):
    print("*", end=" ")
print()

for _ in range(b):
    print("#", end=" ")
print()

for _ in range(c):
    print("$", end=" ")
print()
