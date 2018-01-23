import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(4)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
