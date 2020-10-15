n1 = 8
n2 = 61
for i in range(10):
    n2, n1 = n1+n2, n2
print(n2/n1)