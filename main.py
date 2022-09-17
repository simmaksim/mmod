import random
#from matplotlib import pyplot as plt
#import matplotlib.pyplot
#import numpy

#plt.style.use("fivethirtyeight")

def first(p):
    rand = random.randint(0, 100)
    if rand < p:
        return 1
    else:
        return 0

def count(p):
    count_true = 0
    count_false = 0
    res_list=[]
    i = 0
    while (i < 1000000):
        if first(p) == 1:
            count_true += 1
            res_list.append(1)
        else:
            res_list.append(0)
            count_false += 1
        i += 1
    #plt.hist(res_list)
    return count_true/1000000, count_false/1000000



print(count(90))
'''
    plt.title("Result")
    plt.ylabel("Num of true false")
    plt.tight_layout()
    plt.show()'''