n = int(input("Podaj liczbe -> "))

primary_n = []
for i in range(n):
    primary_n.append(True)

primary_n[0] = False
primary_n[1] = False
for i in range(2, int(n**0.5)+1):
    if primary_n[i]:
        counter = 2
        while counter * i < n:
            primary_n[counter * i] = False
            counter += 1

for i in range(n):
    if primary_n[i]:
        print(i)

