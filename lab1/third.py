import random

def third_check(pA, usl):
    x1=random.randint(1, 100)
    x2=random.randint(1, 100)
    if ((x1 <= pA) & (x2 <= usl)):
        return 0
    if ((x1 > pA) & (x2 <= 100-usl)):
        return 1
    if ((x1 <= pA) & (x2 > usl)):
        return 2
    if ((x1>pA) & (x2 > 100-usl)):
        return 3

def third_cont(pA, usl):
    pb = (pA*usl)+((100-pA)*(100-usl))
    return pb/100

def result(pa, usl):
    flag = third_check(pa, usl)
    pb = third_cont(pa, usl)
    if flag == 0:
        return pa*pb/100
    if flag == 1:
        return pa*(100-pb)/100
    if flag == 2:
        return pb*(100-pa)/100
    if flag == 3:
        return (100-pa) * (100 - pb)/100

if __name__ == '__main__':
    i = 0
    while(i!=1000):
        print(result(80,60))
        i+=1