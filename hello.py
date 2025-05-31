#Clear the Screen
import os
os.system("clear")


#Classes

class Square:
	def __init__(self, side_length):
		#define Square side length
		self.side_length = side_length

	#get area of square
	def area(self):
		return(self.side_length * self.side_length)

# get perminmeter of my_square

	def perimeter(self):
		return(self.side_length * 4)

# creating a report
	def report(self):
		print(f'Side Lenght: {self.side_length}\n')
		print(f'Area: {self.area()}\n')
		print(f'Perimeter: {self.perimeter()}\n')



#Instantiate our class
my_square = Square(10)



#print stuff
#print(my_square.area())
#print(my_square.perimeter())
my_square.report()
