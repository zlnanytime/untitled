h_input1 = int(input('输入前区间:'))
h_input2 = int(input('输入后区间:'))
h_result = 0
h_arr = []
for i in range(h_input1,h_input2+1):
    h_count = 0
    for a in range (2,i+1):
        h_result = i%a
        if h_result==0:
            h_count+=1
    if h_count>1:
        h_arr.append(i)
print("合数为:"+str(h_arr))
print("合数的个数为:"+str(len(h_arr))+"个")


# s_input1 = int(input('输入前区间:'))
# s_input2 = int(input('输入后区间:'))
s_result = 0
s_arr = []
for i in range(h_input1,h_input2+1):
    s_count = 0
    for a in range (2,i+1):
        s_result = i%a
        if s_result==0:
            s_count+=1
    if s_count==1:
        s_arr.append(i)
print("素数为:"+str(s_arr))
print("一共有"+str(len(s_arr))+"个素数")