# Import the image object
from tPixelArt import Image

# Create some image data

checkerboardImageData = [
	[0, 1, 0, 1],
	[1, 0, 1, 0],
	[0, 1, 0, 1],
	[1, 0, 1, 0]
]

squareImageData = [
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,0,0],
	[0,0,1,0,0,1,0,0],
	[0,0,1,0,0,1,0,0],
	[0,0,1,1,1,1,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0]
]

# Create some images
Image(squareImageData)
Image(checkerboardImageData, size = 240, gridSize = 4, showDrawing = True, showBorder = True, gridVisible = True)
