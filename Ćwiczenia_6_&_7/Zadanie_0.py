from math import log10

def is_primary(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    divider = 5
    while divider*divider <= n:
        if n % divider == 0 or n % (divider + 2) == 0:
            return False
        divider += 6

    return True



def search_primes(n, result):
    if n == 0:
        return
    dl = int(log10(n)) + 1
    if dl < 2:
        return
    if is_primary(n):
        result.append()
        return

    for i in range(dl):
        # 1234 -> (1234//1000) * 100 + 34
        prawy_n = n % (10 ** i)
        lewy_n = n // (10 ** (i+1))
        #print(lewy_n, prawy_n)
        search_primes((10**i)*lewy_n + prawy_n, result)

    return

result = {}
# prawa = n % (10**i)
search_primes(12345, result)

# zeby raz wypiswyac uzyc slownika
#dl liczby n -> log(10)+1