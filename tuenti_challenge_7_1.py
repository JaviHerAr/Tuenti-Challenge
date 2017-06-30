# Description: Tuenti Challenge 7 - Challenge 1 - Pizza love.
# Author: Javier Herrero Arnanz.
# Date: 30/06/2017.

# Open the file and read the number of cases. (Change the path to the file).
f = open('D:/JAVIER/CONCURSOS/Tuenti Challenge/tuenti_challenge_7_1/submitInput.txt', 'r', 0)
nCases = int(f.readline())

# Number of slices per pizza.
nSlicesPizza = 8

# For every case calculate the result and show it.
for case in range(nCases):
    # Consume the line with the number of people attending the party.
    f.readline()
    
    # Calculate the number of pizza slices that are necessary during the party.
    nSlices = sum(map(int,f.readline().strip('\n').split(' ')))

    # Calculate the minimum number of pizzas needed to order to ensure that nobody goes hungry.
    nPizzas = nSlices / nSlicesPizza
    if (nSlices % nSlicesPizza > 0):
        nPizzas += 1

    # Print the result for this case.
    print 'Case #' + str(case+1) + ': ' + str(nPizzas)
    
# Close the file.
f.close()
