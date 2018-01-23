input_number = int(input('输入数字:'))
for i in range(1,input_number+1):
    for j in range(1,i+1):#j代表列 i代表行 在乘法表中乘法符号后面一个数和行相等
        result = i*j
        # print(str(j)+"*"+str(i)+"="+str(result)+"\t"+"")
        print("%d*%d=%d"%(j,i,result),end=" ")#end 解决输出分行问题，例如1*2 2*2 位列一行
        if i==j:
            print("")#分行目的 例如1*1 和1*2 分行


# for i in range(1, 10):
#     print
#     for j in range(1, i+1):
#         print ("%d*%d=%d" % (i, j, i*j)),
# input_number = int(input('输入数字:'))
# for i in range(1,input_number):

# for i in range(1,10):
#     for j in range(1,10):
#         print(j, "x", i, "=", i * j,"\t",end="")
#         if i==j:
#             print("")
#             break