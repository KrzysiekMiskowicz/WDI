#sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)))
An = 0.5**0.5
iloczyn = 1
for i in range(20):
    iloczyn *= An
    An = (0.5+0.5*An)**0.5

pi = 2/iloczyn
print(pi)