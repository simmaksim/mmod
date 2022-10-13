import math
import numpy as np
import scipy.stats as sct
def truncated_Nbinom(n, p, max_value, size):
    temp_size = size
    while True:
        temp_size *= 2
        temp = sct.nbinom.rvs(n, p, size = temp_size)
        truncated = temp[temp <= max_value]
        if len(truncated) >= size:
            return truncated[: size]

m = 0
input_1 = truncated_Nbinom(3, 0.5, 15, 100000).tolist()

arr = [0]*15
for item in input_1:
    if item < len(arr):
        arr[item] += 1
for i in range(0, len(arr)):
    arr[i]/=100000

schet = 0
#print(arr)
y = np.arange(0, 15)
theor = sct.nbinom.pmf(y, 3, 0.5)
#print()
for i in range(0 , 15):
    schet += math.pow((arr[i]-theor[i]), 2)/theor[i]
print(schet)
print(schet < sct.chi2.ppf(0.95, 15 - 3))