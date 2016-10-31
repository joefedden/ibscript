import random, math, time, sys

BIGNUM = 10000000

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def loop(loopMod):
    for x in range(0,loopMod):
        randNum = random.randint(1,10)
        factorial(randNum)

def main(count):
    t0 = time.clock()
    loop(int(count))
    t = time.clock()
    return t - t0

print(str(main(BIGNUM)) + " secs")
