height = []
s_heigh = 100.0 #起始高度
rebond = 10 #反弹次数
sum_height = 0

for i in range(0,10):
    height.append(s_heigh)
    s_heigh = s_heigh/2
    sum_height = sum(height)
print("总共经过了多少米:"+str(sum_height))
print("第%d次弹起高度:"%(rebond)+str(height[rebond-1]))