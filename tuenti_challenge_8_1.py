# Description: Tuenti Challenge 8 - Challenge 1 - Waffle love.
# Author: Javier Herrero Arnanz.
# Date: 08/12/2018.

# Open the file and read the number of cases. (Change the path to the file).
f = open('TestInput.txt', 'r', 0)
nCases = int(f.readline())

# For every case calculate the result and show it.
for case in range(nCases):
    # Calculate the number of holes.
    dimens = map(lambda x: int(x)-1,f.readline().strip('\n').split(' '))
    nHoles = dimens[0] * dimens[1]
    
    # Print the result for this case.
    print 'Case #' + str(case+1) + ': ' + str(nHoles)
    
# Close the file.
f.close()
