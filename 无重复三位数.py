count = 0;
for i in range(1,5):
   for j in range(1,5):
       for k in range(1,5):
           if i!=j|j!=k|k!=i:
               count +=1
               print ("This is the "+str(count)+" number:")
               print((i*100)+(j*10)+k)



