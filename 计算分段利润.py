i = int(input('净利润：'))
arr1 = [1000000,600000,400000,200000,100000, 0]
arr2 = [0.01,0.015,0.03,0.05,0.075,0.1]
result = 0

for b in range(0,6):
    if i>arr1[b]:
        result +=((i-arr1[b])*arr2[b])
        i=i-(i-arr1[b])
print(result)
