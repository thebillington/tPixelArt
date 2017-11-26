# Import the image object
from tPixelArt import Image

# Initialise some image data
NewImageData=[[0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
]

for row in range (0,8):
    binary=""
    binary=input("Input 8 bit binary code for row " + str(row+1) + ":")
    while len(binary)!=8 or any(character not in ["1","0"] for character in binary):
        print("Binary code must be 8 digits (eg: 10110011)")
        binary=input("Input 8 bit binary code for row " + str(row+1) + ":")
    
    for column in range(0,8):
        NewImageData[row][column]=int(binary[column])


print(NewImageData)

# Create images
Image(NewImageData)
