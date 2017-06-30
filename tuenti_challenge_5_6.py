# Description: Tuenti Challenge 5 - Problem 6 - Airscrews.
# Author: Javier Herrero Arnanz.
# Date: 04/04/2015.

# Read sheet data and store it (Change the path to the file).
f = open('sheet.data', 'r', 0)
size = f.readline().split()
sheetData = []
for i in xrange(int(size[0])):
    line = f.readline().split()
    sheetData.append([int(n) for n in line])
f.close()
   
# Open the file and read the number of test cases. (Change the path to the file).
f = open('submitInput', 'r', 0)
nCases = int(f.readline())

# For every case calculate the result and show it.
for case in xrange(nCases):
    caseData = f.readline().split()
    y0 = int(caseData[0])
    x0 = int(caseData[1])
    y1 = int(caseData[2])
    x1 = int(caseData[3])
    k = int(caseData[4])
    
    # Go through the area in which the axis can be.
    x0 += k
    y0 += k
    x1 -= k
    y1 -= k
    bestQuality = 0
    for x in xrange(x0,x1+1):
        upRowSum = []  
        downRowSum = []
        for y in xrange(y0,y1+1):
            quality = 0          
                                    
            # Up piece.
            xPos = x - k
            if (len(upRowSum) == 0):
                yPos = y - k
                yMove = k
            else:
                yPos = y - 1
                yMove = 1
                upRowSum.pop(0)
            new = [sum(sheetData[_y][xPos:xPos+k]) for _y in xrange(yPos,yPos+yMove)]
            upRowSum += new
            quality += sum(upRowSum)       
            
            # Down piece.
            xPos = x + 1
            if (len(downRowSum) == 0):
                yPos = y + 1
                yMove = k
            else:
                yPos = y + k
                yMove = 1
                downRowSum.pop(0)
            new = [sum(sheetData[_y][xPos:xPos+k]) for _y in xrange(yPos,yPos+yMove)]
            downRowSum += new 
            quality += sum(downRowSum)  
             
            # Check piece quality.
            if (quality > bestQuality):
                bestQuality = quality
        
    print "Case " + str(case+1) + ": " + str(bestQuality)
    
# Close the file.
f.close()
