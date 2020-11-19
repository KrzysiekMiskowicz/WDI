N = 40

p = 1
for i in range(1, N):
    p *= (365-i)/365

print(p)