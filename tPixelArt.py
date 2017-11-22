# Import the turtle library
import turtle as t

# Create an image object
class Image():
	
	# Constructor that takes in some default width and height for window size, number of squares on the grid and whether the gridlines are visible
	def __init__(self, size = 480, gridSize = 8, gridVisible=False):
		
		# Hide the turtle
		t.hideturtle()
		
		# Disable the tracer
		t.tracer(0, 0)
		
		# Set the default size, width of the grid and grid size
		self.size = size
		self.gridSize = gridSize
		self.pixelWidth = int(size / gridSize)
		
		# Draw the image border
		self.drawBorder()
		
		# If the grid is visible, draw it
		if gridVisible:
			self.drawGrid()
			
		# Draw the grid
		t.update()
		
		# Exit on click
		t.exitonclick()
			
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

img = Image(480, 16, True)
