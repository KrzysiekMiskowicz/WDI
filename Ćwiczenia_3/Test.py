'''
znaki = input("Podaj znaki -> ")

def substring(string, an, index, is_char):
    if index == len(string)-1:
        if is_char:
            print(an)
            print(an+string[index])
        else:
            if ord(string[index]) >= ord("a") and ord(string[index]) <= ord("z"):
                print(an+string[index])

    else:
        substring(string, an, index + 1, is_char)
        is_char = is_char or (ord(string[index]) >= ord("a") and ord(string[index]) <= ord("z"))
        substring(string, an + string[index], index + 1, is_char)


substring(znaki, "", 0, False)
'''

'''
MAX = 100
result = [0 for _ in range(20)]
result[0] = 1
end = 1
for i in range(2, 10):
    overload = 0
    for j in range(end):
        result[j] = (result[j] * i) + overload
        overload = result[j] // MAX
        result[j] %= MAX
        if j == end-1 and overload != 0:
            end += 1

for i in reversed(result):
    print(i, end="")
'''
'''
n = 9
e = [0 for _ in range(n)]
e[0] = 1

divider = 1
pos = 0
for i in range(1, n):
    divider *= i
    a = 1
    for j in range(pos, n):
        e[j] += int(a // divider)
        a = (a - (int(a // divider) * divider)) * 10

    overload = 0
    for j in reversed(range(pos, n)):
        e[j] += overload
        overload = e[j] // 10
        e[j] %= 10

    while divider > 1:
        divider /= 10
        pos += 1

    if pos >= n:
        break

for i in e:
    print(i, end="")
'''
