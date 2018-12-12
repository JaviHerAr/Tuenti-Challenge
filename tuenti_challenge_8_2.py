# Description: Tuenti Challenge 8 - Challenge 2 - Hidden numbers.
# Author: Javier Herrero Arnanz.
# Date: 12/12/2018.

# Open the file and read the number of cases. (Change the path to the file).
f = open('TestInput.txt', 'r')
nCases = int(f.readline())

# For every case calculate the result and show it.
for case in range(nCases):
  # Get base and max digit for that base.
  base = len(f.readline().strip('\n'))
  maxDigit = base - 1

  # Go through each digit of the max and min numbers of the current base in order to
  # calculate their respective numbers in decimal base.
  maxDecimal = 0
  minDecimal = 0
  for i in range(base):
    maxCurrentDigit = i

    if (i == maxDigit - 1):
      minCurrentDigit = 0
    elif (i == maxDigit):
      minCurrentDigit = 1
    else:
      minCurrentDigit = maxDigit - i
    
    maxDecimal += maxCurrentDigit * base**i
    minDecimal += minCurrentDigit * base**i

  # Print the result for this case.
  result = maxDecimal - minDecimal
  print('Case #' + str(case+1) + ': ' + str(result))

# Close the file.
f.close()
