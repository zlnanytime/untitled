arr_1 = []
for i in range(1,1001):
    arr_2 = []
    for x in range(1,int(i/2)+1):
        if i%x==0:
            arr_2.append(x)
    if i==sum(arr_2):
        print(i)
        print(arr_2)
        arr_1.append(i)
print("一共有%d个完数"%(len(arr_1)))
