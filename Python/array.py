a = [0, 1, 2, 3, 4, 5]

print(a[1:3])  # elements except first one and upto first three
print(a[:-2])  # elements except last two
print(a[1:-2])  # elements except first one and last two
b = a[:]  # shallow copy of the array

a[0] = 4
print(b)
