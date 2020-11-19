size_divider = 1e16
n = 1000
result = []
for i in range(172):
    result.append(0)

result[0] = 1
end = 1
for i in range(2, n+1):
    overload = 0
    for j in range(end):
        if result[j] > 0 or overload > 0:
            product = (result[j] + overload) * i
            result[j] = int(product % size_divider)
            overload = int(product // size_divider)
            if j == end-1 and overload > 0:
                end += 1


for i in reversed(result):
     print(""+"{:0>16d}".format(i), end="")
