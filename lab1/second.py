import random

def second(list_p):
    iter = 0
    k = len(list_p)
    counter = []
    i=0
    while i<k:
        counter.append(0)
        i+=1
    while(iter<100000):
        res = []
        k = len(list_p)
        x = []
        i = 0
        while k > 0:
            x.append(random.randint(1, 100))
            k -= 1
        while(i < len(list_p)):
            if x[i] <= int(list_p[i]):
                res.append(1)
                counter[i] +=1
            else:
                res.append(0)
            i += 1
        print(res)
        iter+=1
    print(counter)
i = 0
l = int(input("Введите кол-во вероятностей"))
list = []
while (i< l):
    list.append(input("Введите вероятность"))
    i+=1
i=0
second(list)