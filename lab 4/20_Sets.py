a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
A = set(a)
B = set(b)
only_a = A.difference(B)
print(only_a)
print([name for name in a if name in only_a])
