import random, math, time, sys

f = open('output.txt','w')
BIGNUM = 10000000
times = []

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def loop(loopMod):
    for x in range(0,loopMod):
        randNum = random.randint(1,10)
        factorial(randNum)

def getTime():
    t0 = time.clock()
    loop(BIGNUM)
    t = time.clock()
    return t - t0

def main():
    total = 0
    average = 0

    for x in range(0,10):
        times.append(getTime())
        total = total + getTime()
    
    average = total / len(times)
    times.append(average)

    return times

f.write(str(main()))
f.close
