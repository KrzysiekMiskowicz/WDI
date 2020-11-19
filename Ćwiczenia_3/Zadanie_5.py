n = int(input("Wprowadz dokladnosc -> "))

e = [0 for i in range(n+1)]
e[0] = 1
factorial = 1
pos = 0
divider = 1
while pos <= n+1:
    a = 1
    for i in range(pos, n+1):
        e[i] += int(a // divider)
        a = (a - (a // divider) * divider) * 10

    overflow = 0
    for i in reversed(range(n+1)):
        e[i] += overflow
        overflow = e[i] // 10
        e[i] %= 10

    factorial += 1
    divider *= factorial
    while divider > 1:
        pos += 1
        divider /= 10

print(e[0], end=".")
for i in range(1, n+1):
    print(e[i], end="")

