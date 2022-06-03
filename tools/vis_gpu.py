import GPUtil
import time
import os

less_2000_count = 0


while True:

    GPUS = GPUtil.getGPUs()
    print(GPUS[0].memoryTotal, GPUS[0].memoryUsed)

    if GPUS[0].memoryUsed<2000:
        less_2000_count += 1
    else:
        less_2000_count = 0

    if less_2000_count>1:
        os.system("shutdown")
        
    time.sleep(60*2)
# A = GPUtil.showUtilization()
# B = GPUtil.getFirstAvailable()



# C = 
# GPU = GPUtil.getAvailability(GPUs)
# print(B)