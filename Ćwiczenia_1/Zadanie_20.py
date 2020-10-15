An = 5
Bn = 8
for i in range(4):
    An, Bn = (An*Bn)**0.5, (An+Bn)/2
print(An)
print(Bn)
