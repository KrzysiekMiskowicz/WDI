n = int(input("Podaj liczbę "))
dzielnik = int(n**0.5)
while True:
    if(n % dzielnik == 0):
        print(dzielnik, n / dzielnik)
        break
    dzielnik -= 1