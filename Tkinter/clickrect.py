from graphics import *

def draw_rectangle():
    """Allows user to draw a rectangle on the graphical window."""
    win = GraphWin("Draw Rectangle", 300, 300)
    global first_point, second_point
    first_point = win.getMouse()
    second_point = win.getMouse()
    
    rectangle = Rectangle(first_point, second_point)
    rectangle.setOutline("blue")
    rectangle.setFill("blue")
    rectangle.draw(win)
    
    input("Press Enter to close the window")
    win.close()

def calculate_perimeter():
    """Calculates the perimeter of the drawn rectangle."""
    length = abs(first_point.getX() - second_point.getX())
    width = abs(first_point.getY() - second_point.getY())
    return 2 * (length + width)

def calculate_area():
    """Calculates the area of the drawn rectangle."""
    length = abs(first_point.getX() - second_point.getX())
    width = abs(first_point.getY() - second_point.getY())
    return length * width

# Run the drawing function
draw_rectangle()

# Calculate and display the perimeter and area
rect_perimeter = calculate_perimeter()
print("Perimeter: ", rect_perimeter)
rect_area = calculate_area()
print("Area: ", rect_area)
