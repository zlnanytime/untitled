# import time

arr = []
s_input1 = int(input('前区间(三位数):'))
s_input2 = int(input('后区间(三位数):'))
for i in range(s_input1,s_input2+1):
    result = 0
    b = len(str(i))
    y = i
    for a in range(int(b)):
        y_result = y%10
        y = int(y/10)
        result = result+pow(y_result,3)
    if result==i:
        arr.append(i)
    # print(b)
    # result = 0
print(arr)
print(len(arr))
# i = 153
# y=i
# for a in range(3):
#
#     y_result = y%10
#     y = int(y/10)
#     print(y_result)
#     # print(y)
#     time.sleep(4)