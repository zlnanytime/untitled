a_input = int(input('输入a:'))
n_input = int(input('输入最高加到的位数n:'))
arr_a = []
s = 0
result = 0
for i in range(0,n_input):
    s = s*10+a_input
    arr_a.append(s)
    result = result + s
string_out = str()
for b in range(len(arr_a)):
    if b <len(arr_a):
        string_out = str(string_out) + str(arr_a[b])+'+'
    if b==(len(arr_a)-1):
        string_out = str(string_out) + str(arr_a[b]) + '='
    # print('%d\t'%(arr_a[b]))
    # print('+\t')
print(string_out,end='')
print(result)

