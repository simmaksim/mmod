import random


def four(Pi):
    counter = []
    iter = 0
    i = 0
    while i < len(Pi):
        counter.append(0)
        i += 1
    i = 0
    while(iter<1000000):
        x = random.randint(1, 100)
        ans = []

        f = 0
        while (len(ans) != len(Pi)):
            ans.append(f)

            f += 1
        k = 0

        res = []
        while (k != len(Pi)):
            i = 0
            left = 0
            right = 0
            while (i != k):
                left += Pi[i]
                i += 1
            i = 0
            while (i != k + 1):
                right += Pi[i]
                i += 1
            if (x >= left) & (x < right):
                counter[k] += 1
                print(ans[k], right)
            k += 1

        iter+=1
    print(counter)

c = 0
l = int(input("Введите кол-во вероятностей"))
list = []
while (c != l):
    list.append(int(input("Введите вероятности")))
    c += 1
i = 0

four(list)

