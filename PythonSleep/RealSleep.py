import time

print(time.time()) 
for _ in range(10000): 
   time.sleep(0.0001) 
print(time.time())