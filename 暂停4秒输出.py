import time
input_number = int(input('输入数字:'))
for i in range(1,input_number+1):
    for j in range(1,i+1):
        result = i*j
        # print(str(j)+"*"+str(i)+"="+str(result)+"\t"+"")
        print("%d*%d=%d"%(j,i,result),end=" ")
        if i==j:
            print("")
        if i==3:
            time.sleep(4) #暂停4秒