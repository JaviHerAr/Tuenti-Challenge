# Description: Tuenti Challenge 5 - Problem 1 - The Buffer.
# URL: https://contest.tuenti.net/Challenges?id=1
#
# Author: Javier Herrero Arnanz.
# Date: 27/04/2015.

# Open the file and read the number of cases. (Change the path to the file).
f = open('submitInput', 'r', 0)
nCases = int(f.readline())

# For every case calculate the result and show it.
for case in range(nCases):
    nUrinals = int(f.readline()) # Number of urinals.
    if ((nUrinals % 2) == 0): # Pair.
        print (nUrinals / 2) 
    else: # Odd.
        print ((nUrinals / 2) + (nUrinals % 2))
        
# Close the file.
f.close()
