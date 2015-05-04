# Description: Tuenti Challenge 5 - Problem 3 - Favourite primes.
# URL: https://contest.tuenti.net/Challenges?id=3
#
# Author: Javier Herrero Arnanz.
# Date: 30/04/2015.

# Global Variables.
numFact = {} # Dict with all numbers in numbers.txt factored.
factBlocks = [] # Blocks of prime factors.
primes25 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]  # List of first 25 prime numbers.

def searchFPrimes(start,stop):
    """
    This method searchs the favourite primes for the given range [start, stop).
    
    start: Range begin.
    stop: Range end.
    output: Prints the number of repetitions of the most popular prime(s) followed by the most popular prime(s).
    """
    
    assert (stop >= start), "Invalid range"
    
    global numFact # Dict with all numbers in factored.
    global factBlocks # Blocks of prime factors.
    
    # Sum the blocks within which is the current range.
    blockStart = start/1000
    blockEnd = stop/1000
    totalRepetDic = {} # Key-> Prime number / Value-> Number of repetitions.
    for i in range(blockStart,blockEnd+1):
        for p in primes25:
            if (p in totalRepetDic):
                totalRepetDic[p] += factBlocks[i][p]
            else:
                totalRepetDic[p] = factBlocks[i][p]
     
    # Delete the margins difference. Up and down.
    for i in range((blockStart*1000),start):
        for p in primes25:
            if ((p in totalRepetDic) and (p in numFact[i])):
                totalRepetDic[p] -= numFact[i][p]        
    for i in range(stop,(blockEnd*1000)+1000):
        for p in primes25:
            if ((p in totalRepetDic) and (p in numFact[i])):
                totalRepetDic[p] -= numFact[i][p]
    
    # Print results in a file.  
    resultsF = open('submitInputResult.txt','a',0)
    maxRep = 0
    for p in totalRepetDic:
        if (totalRepetDic[p] > maxRep):
            maxRep = totalRepetDic[p]
    resultsF.write(str(maxRep))
    for p in totalRepetDic:
        if (totalRepetDic[p] == maxRep):
            resultsF.write(' '+str(p))
    resultsF.write('\n')
    resultsF.close()


################################  MAIN  #######################################

# Open the file and read the number of test cases. (Change the path to the file).
f = open('submitInput', 'r', 0)
nCases = int(f.readline())

# Preprocess the range of numbers to make the calculations faster.
# 1- Read and store all the numbers as strings in a list. (Change the path to the file).
numbersF = open('numbers.txt','r',0)
numbersL = list(numbersF)
numbersF.close()
# 2- Factorise all numbers and fill the blocks of prime factors.
for i in range(len(numbersL)/1000): # Initialize blocks of prime factors.
    factBlocks.append({})
for i in range(len(numbersL)):
    n = int(numbersL[i])
    repetDic = {} # Key-> Prime number / Value-> Number of repetitions.
    for p in primes25: # Factorise the current number.
        while (n%p == 0):
            n = n/p
            if (p in repetDic):
                repetDic[p] += 1 
            else:
                repetDic[p] = 1
    numFact[i] = repetDic
    for p in repetDic: # Update the block.
        if (p in factBlocks[(i/1000)]):
            factBlocks[(i/1000)][p] += repetDic[p]
        else:
            factBlocks[(i/1000)][p] = repetDic[p]

# For every case calculate the result and show it.
for case in range(nCases):
    interval = f.readline().split()
    searchFPrimes(int(interval[0]),int(interval[1]))
    
# Close the file.
f.close()
