#sweepujemy po gornym lewym elemencie t1
def f(t1, t2):
    n1 = len(t1)
    n2 = len(t2)
    r1 = c1 = -n1+1
    r2 = c2 = n2
    for r_sweep_start in range(r1, r2):
        for c_sweep_start in range(c1, c2):
            common_field = 0
            common_even = 0
            for r in range(n1):
                for c in range(n1):
                    if 0 <= r_sweep_start + r < n2 and 0 <= c_sweep_start + c < n2:
                        common_field += 1
                        if count_even(five_system(t1[r][c])) == count_even(five_system(t2[r+r_sweep_start][c+c_sweep_start])):
                            common_even += 1
                            print(r_sweep_start, c_sweep_start, r, c)

            if common_even / common_field > 1/3:
                return True

    return False

def five_system(n):
    result = 0
    while n != 0:
        result *= 5
        result += n % 5
        n //= 5

    return result


def count_even(n):
    even = 0
    while n != 0:
        if n % 2 == 0:
            even += 1
        n //= 10

    return even

t1 = [[2, 2],
      [2, 1]]

t2 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

print(f(t1, t2))
