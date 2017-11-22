# Import the turtle library
import turtle as t
import sys

# Create an image object
class Image():
	
	# Constructor that takes in some default width and height for window size, number of squares on the grid and whether the gridlines are visible
	def __init__(self, imageData, size = 480, gridSize = 8, gridVisible=False, showDrawing = False, showBorder = False):
		
		# Set the traceback limit
		sys.tracebacklimit = None
		
		# Clear the turtle window
		t.clear()
		
		# If the user doesn't want to show the drawing
		if not showDrawing:
		
			# Hide the turtle
			t.hideturtle()
			
			# Disable the tracer
			t.tracer(0, 0)
			
		# Otherwise
		else:
			# Reset
			t.showturtle()
			t.tracer(1, 0)
		
		# set the pixel colours
		self.colours = ["white", "black"]
		
		# Set the default size, width of the grid and grid size
		self.size = size
		self.gridSize = gridSize
		self.pixelWidth = int(size / gridSize)
		
		# Get the image data
		self.imageData = imageData
		
		# Check the image data
		self.checkImageData()
			
		# Draw the image
		self.drawImage()
		
		# Set the colour to black
		t.color("black")
		
		# If the grid is visible, draw it
		if gridVisible:
			self.drawGrid()
			
		# If the user wants to show the border
		if showBorder:
			
			# Draw the image border
			self.drawBorder()
		
		# If the user doesn't want to show the drawing
		if not showDrawing:
			
			# Draw the grid
			t.update()
			
		# Wait for user input
		input("Press any key to continue...")
			
	# Define a function to draw the image border
	def drawBorder(self):
		
		# Go to the top left
		self.setLocation(0, 0, 0)
		
		# Draw the border
		for i in range(4):
			t.forward(self.size)
			t.right(90)		
			
	# Function to move the pen to a specific location and heading
	def setLocation(self, x, y, heading = 0):
		
		# Set the x and y locations
		x = x - int(self.size / 2)
		y = -y + int(self.size / 2)
		
		# Set the pen colour to black
		t.color("black")
		
		# Go to the specified location
		t.penup()
		t.goto(x,y)
		t.pendown()
		
		# Set the heading
		t.setheading(heading)
			
	# Create a draw grid method
	def drawGrid(self):
		
		# Iterate over each column
		for i in range(self.gridSize - 1):
			
			# Set the location for the line and heading
			self.setLocation((i + 1) * self.pixelWidth , 0, 270)
			
			# Draw the line
			t.forward(self.size)
			
			# Set the location for the line and heading
			self.setLocation(0, (i + 1) * self.pixelWidth, 0)
			
			# Draw the line
			t.forward(self.size)
			
	# Function to check that the image data is compatible
	def checkImageData(self):
		
		# Check if there is the correct number of rows
		if not len(self.imageData) == self.gridSize:
			
			# Throw an exception
			raise ImageDataError("You do not have the correct number of rows in your image!")
			
		# Check that each row has the correct number of pixels
		for i in range(len(self.imageData)):
			
			# Get the row
			row = self.imageData[i]
		
			# Check if there is the correct number of rows
			if not len(row) == self.gridSize:
				
				# Throw an exception
				raise ImageDataError("You do not have the correct number of pixels in row {} of your image!".format(i + 1))
	
	# Create a function to draw the image
	def drawImage(self):
		
		# For each row in the image data
		for i in range(self.gridSize):
			
			# Look at each pixel
			for j in range(self.gridSize):
				
				# Set the x and y
				x = j * self.pixelWidth
				y = i * self.pixelWidth
				
				# Set the location for the line and heading for this pixel
				self.setLocation(x, y, 0)
				
				# Get the pixel colour
				t.color(self.colours[int(self.imageData[i][j])])
				
				# Start the fill
				t.begin_fill()
				
				# Draw the pixel
				for x in range(4):
					t.forward(self.pixelWidth)
					t.right(90)
					
				# End the fill
				t.end_fill()
		
# Define an image data error
class ImageDataError(Exception):
	
	pass
