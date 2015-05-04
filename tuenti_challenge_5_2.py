# Description: Tuenti Challenge 5 - Problem 2 - Almost prime.
# URL: https://contest.tuenti.net/Challenges?id=2
#
# Author: Javier Herrero Arnanz.
# Date: 29/04/2015.

def countAlmostPrimes(start,stop):
    """
    This method counts the number of almost prime numbers that exists 
    in the range [start, stop]. It is based on the Sieve of Eratosthenes.
    
    start: Range begin.
    stop: Range end.
    output: Number of almost prime numbers in the given range.
    """
    assert (stop >= start), "Invalid range" 
    
    # Number of almost primes.
    count = 0
    
    # Sieve stores the Sieve of Eratosthenes until stop.
    # True-Prime number / False-Composite number.
    sieve = ([True]* (stop+1))
    sieve[0] = sieve[1] = False
    i = 2
    while (i*i <= stop):
        if (sieve[i] == True):
            for j in xrange(i*i, stop+1, i):
                sieve[j] = False
        i += 1
 
    # For the composite numbers, check which of them are almost primes.
    # To do it divide for the first prime divisor, the rest should be 0 and 
    # the result should be a prime number.
    i = 2
    while (i*i <= stop):
        if (sieve[i] == True):
            for j in xrange(i*i, stop+1, i):
                if ((j%i == 0) and (sieve[j/i] == True)):
                    if ((j >= start) and (j <= stop)):
                        # Only count almost primes inside the given range.
                        count += 1
        i += 1
 
    return count



################################  MAIN  #######################################

# Open the file and read the number of test cases. (Change the path to the file).
f = open('submitInput', 'r', 0)
nCases = int(f.readline())

# For every case calculate the result and show it.
for case in range(nCases):
    interval = f.readline().split()
    print countAlmostPrimes(int(interval[0]),int(interval[1]))

# Close the file.
f.close()
