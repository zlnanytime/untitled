f0 = 0
f1 = 1
f_input = int(input())
f_l = [0,1]
for i in range(0,f_input-1):
    f_n = f_l[i] + f_l[i+1]
    f_l.append(f_n)
print(f_l)
print(f_l[f_input])