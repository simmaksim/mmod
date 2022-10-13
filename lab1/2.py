#точечные оценки мат ожидания и дисперсии
import math

import scipy.stats as sct

def truncated_Nbinom(n, p, max_value, size):
    temp_size = size
    while True:
        temp_size *= 2
        temp = sct.nbinom.rvs(n, p, size = temp_size)
        truncated = temp[temp <= max_value]
        if len(truncated) >= size:
            return truncated[: size]

m =0
input_1 = truncated_Nbinom(3, 0.5, 15, 1000).tolist()
for item in input_1:
    m += item
m /=100000

d = 0
for item in input_1:
    d += math.pow((item - m), 2)
d/=100000
print(input_1)
#print(d)