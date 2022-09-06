import random


def f(min_len, max_len):
    l = []
    for _ in range(random.randint(min_len, max_len)):
        l.append(random.randint(0, 9))
    print(l)


f(8,10)