# Desc: Tuenti Challenge 4 - Problem 2 - F1 Bird's-eye Circuit.
# URL: https://contest.tuenti.net/resources/2014/Question_2.html
#
# Author: Javier Herrero Arnanz.
# Date: 11/04/2015.

def showTrack(track):
    """
    This method receives a track in plain text format and prints out the graphic
    representation of it. Shows how it looks like in real life from an overhead view.
    
    track: A track in plain text format.
    output: Prints a graphic representation of the track.
    """
    
    # The graphic representation of the track is stored in a list of lists.
    # Every nested list is a different row who should be printed as output.
    trackMatrix = []
    
    # Coordinates and direction to go through the track.
    x = 0
    y = 0
    direct = (0,0) # Item 0: 0-Horizontal/1-Vertical -- Item 1: 0-Right,Up/1-Left,Down.
    
    if (track[0] != '/'): # The first line of the track is chunked.
        # Store correctly the top left corner of the track. 
        splitTrack = track.split('/')
        topLeftC = '/' + splitTrack[len(splitTrack) - 1]
        track = topLeftC + track
        track = track[:-len(topLeftC)]        
    
    # Create the matrix of the track.
    trackMatrix.append(['/']) # First row, first char.
    x, y = 1,0     
    for i in range(1,len(track)):
        if (len(trackMatrix) < (y+1)): # Add an empty row.
            trackMatrix.append([])
            
        if (len(trackMatrix[y]) <= x): # Add empty spaces.
            spaces = x - len(trackMatrix[y]) + 1
            addSpaces(spaces,trackMatrix[y])
             
        # Evaluate the char.   
        char = track[i]     
        if ((char == '-') and (direct[0] == 1)): # Vertical.
            char = '|'
        elif (char == '/'):
            # Update direction.
            direct = (abs(direct[0]-1),direct[1])
        elif (char == '\\'):
            # Update direction.
            direct = (abs(direct[0]-1),abs(direct[1]-1))
                    
        # Add char to matrix.
        trackMatrix[y][x] = char
        
        # Update the coordinates.
        newC = updateCoor(x,y,direct)
        x = newC[0]
        y = newC[1]
    
    # Search the longest row of the track.
    maxLen = 0
    for row in trackMatrix:
        if (len(row) > maxLen):
            maxLen = len(row)
    
    # Prints the graphic representation.
    for row in trackMatrix:
        if (len(row) < maxLen): # Add spaces.
            addSpaces((maxLen - len(row)),row)
        for char in row:
            print (char),
        print('\n') # Print EOL.

def addSpaces(n,row):
    """
    Adds empty spaces at the end of the row.
    
    n: Number of spaces to add.
    row: Row (list) in which add the spaces.
    return: Row (list) with spaces at the end.
    """
    
    for i in range(n):
        row.append(' ')

def updateCoor(x,y,direct):
    """
    Updates the coordinates according to the current direction.
    
    x: X coordinate.
    y: Y coordinate.
    direct: Current direction.
    return: A tuple (x,y) with the new coordinates.
    """
    
    if (direct[0] == 0): # Horizontal.
        if (direct[1] == 0): # Right.
            return (x+1,y)
        else: # Left.
            return (x-1,y)
    else: # Vertical.
        if (direct[1] == 0): # Up.
            return (x,y-1)
        else: # Down.
            return (x,y+1)
        
        

########### Examples of use. ###########
track1 = '#----\-----/-----\-----/'
track2 = '------\-/-/-\-----#-------\--/----------------\--\----\---/---'
track3 = '-#----\---\----\---/--/---/------\------\--\----/-'
track4 = '---#------\--/-------------\--/---'

showTrack(track1)
showTrack(track2)
showTrack(track3)
showTrack(track4)
