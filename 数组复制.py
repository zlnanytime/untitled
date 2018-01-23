a = []
for i in range(5):
    input_number = int(input())
    a.append(input_number)

# b = a[:]
b = a.copy()
print(b)