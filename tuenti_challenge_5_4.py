# Description: Tuenti Challenge 5 - Problem 4 - A Bitter Dinner.
# Author: Javier Herrero Arnanz.
# Date: 01/04/2015.

import base64
import binascii
import re

def cookPiece(piece,size,format,reverse):
    """
    This method transform the given piece of bits according to specifications.
    
    bits: Piece of bits to transform. String.
    size: The size of the piece. Integer.
    format: L or B which means Little-Endian or Big-Endian. Char.
    reverse: True/False. It means that it is necessary to bit-reverse the piece or not.
    output: The resulting integer.
    """
    
    if (format == 'L'): # Change the bytes order.
        bytesLst = []
        for i in range(0,size/8): # Slice in pieces of 8 bits.
            start = i*8
            bytesLst.append(piece[start:start+8])
        # Add last bits.
        start = (size/8)*8    
        bytesLst.append(piece[start:])
        # Reverse the slices and join them.
        bytesLst = bytesLst[::-1]
        piece = ''.join(bytesLst)
    
    if (reverse): # Reverse the piece.
        piece = piece[::-1]   
           
    # Transform to integer.
    print int(piece,2)
    
    
    
################################  MAIN  #######################################

# Open the file and read the string in base64 and the number of pieces. (Change the path to the file).
f = open('submitInput', 'r', 0)
strB64 = f.readline()
nPieces = int(f.readline())

# Convert string from base64 to binary.
strBinary = bin(int(binascii.hexlify(base64.b64decode(strB64)), 16))
strBinary = strBinary[2:]

# Cut the string appropriately and show the results.
for p in range(nPieces):
    # Read the description of the piece
    desc = f.readline()
    desc = desc.rstrip('\n')
    size = int(re.findall("[-+]?\d+[\.]?\d*", desc)[0])
    format = desc[len(str(size))]
    if (desc[-1] == 'R'):
        reverse = True
    else:
        reverse = False
    
    # Cut the piece.
    piece = strBinary[0:size]
    strBinary = strBinary[size:]
    
    # Cook the piece.
    cookPiece(piece,size,format,reverse)

# Close the file.
f.close()
