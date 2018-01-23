res = 0
year = int(input('Year:\n'))
month = int(input('Month:\n'))
day = int(input('Day:\n'))
if year%4==0|(year%400==0&year%100!=0):
    arr = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(0,month):
        res +=arr[i]
    print("这是第"+str(res+day)+"天")
# day = int(input())
# arr = [31,29,31,30,31,30,31,31,30,31,30,31]
# for i in range(0,day):
#     res +=arr[i]
# print("这是第"+str(res)+"天")
else:
    arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, month):
        res += arr[i]
    print("这是第" + str(res + day) + "天")