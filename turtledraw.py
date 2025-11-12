#brings in teh turtle library
import turtle

#Clear the Screen
import os
os.system("cls")


#create a turtle object
t = turtle.Turtle()
#create screen object
screen = turtle.Screen()


def reset_turtle():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def draw_square(size):
    #reset_turtle
    # for loop to do 4 lines
    for _ in range(4):
        t.forward(size)
        t.right(90)
        


def draw_triangle(size):
    #reset_turtle
    for _ in range(3):
        t.forward(size)
        t.left(120)



def draw_circle(radius):
    #reset_turtle
    t.circle(radius)


#main function
def draw_shape():
    while True:
        print("\nSelect a Shape to Draw:")
        print("1. Square")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")

        #prompt user
        choice = input("Enter the number of your choice: ")

        #choice logic
        if choice == "1":
            size = int(input("Enter the size of the Square: "))
            draw_square(size)
        elif choice == "2":
            size = int(input("Enter the size of the Triangle: "))
            draw_triangle(size)
        elif choice == "3":
            size = int(input("Enter the radius of the Circle: "))
            draw_circle(size)
        elif choice == "4":
            print('Exiting the program. Later!')
            turtle.bye()
            break
        else:
            print('That is not a valid choice. Please try again...')
            
        

#run the app
draw_shape()



# stop/complete 
#turtle.done()