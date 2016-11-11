import random,time

f = open('output.txt','a') #Finds file 'output.txt' that we will append data to
BIGNUM = 1000000 
times = [] #creates an empty 'times' array

def factorial(x): #creates a 'factorial' function that will recursively find the factorial of 'x'
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def loop(loopMod): #creates a 'loop' function that will find a random number, 'randNum', to find the factorial of 'loopMod' times
    for x in range(0,loopMod):
        randNum = random.randint(1,10)
        factorial(randNum)

def getTime(): #creates a 'getTime' function that will return the time the 'loop' function takes to execute
    t0 = time.clock()
    loop(BIGNUM)
    t = time.clock()
    return t - t0

def main(): #creates a 'main' function that will run the 'getTime' function 10 times and then returns an array of the times with their average
    total = 0
    average = 0
    count = 0
    
    for x in range(0,10):
        times.append(getTime())
        total = total + getTime()
        count = count + 1
        print(count)
    
    average = total / len(times)
    times.append(average)

    return times

f.write(str(main()) + "\n") #writes the array of times to the 'output.txt' file
f.close #closes the 'output.txt' file
