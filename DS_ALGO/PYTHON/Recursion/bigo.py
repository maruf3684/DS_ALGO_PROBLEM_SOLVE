
import time

def counting(param):
    total=0
    for i in range(0,param):
        total += i
    return total

start=time.time()
print(counting(100000000))
end=time.time()

print(f'performance= {end-start}')