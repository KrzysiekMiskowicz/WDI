#Krzysztof Miśkowicz

#usuwam po kolei 5-elementy ciahu tablicy T i spraedzamy czy ich odpowiendie trojki maja NWD = 1
#

def NWD(n1, n2, n3):
    result = 1
    dzielnik = 2
    while dzielnik <= min(n1, n2, n3):
        if n1 % dzielnik == 0 and n2 % dzielnik == 0 and n3 % dzielnik == 0:
            n1 //= dzielnik
            n2 //= dzielnik
            n3 //= dzielnik
            result *= dzielnik
        else:
            dzielnik += 1

    return result


def trojki(T):
    n = len(T)
    if n < 3:
        return 0

    elif n == 3:
        if NWD(T[0], T[1], T[2]) == 1:
            print(T)
            return 1
        else:
            return 0

    suma = 0
    for i in range(n):
        if i+3 <= n:
            suma += trojki(T[i:i+3])
        if i+3 < n:
            suma += trojki(T[i:i+2]+[T[i+3]])
        if i+4 < n:
            suma += trojki([T[i]]+[T[i+2]]+[T[i+4]])

    return suma


print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
