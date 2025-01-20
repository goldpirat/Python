from graphics import *
from random import randint

def estimate_pi(window_size):
    win = GraphWin("Pi Estimation", window_size, window_size)  # Create a graphical window
    total_points = 10000
    points_inside_circle = 0
    
    # Draw a circle for reference
    center = Point(window_size / 2, window_size / 2)
    radius = window_size / 2
    circle = Circle(center, radius)
    circle.setOutline("black")
    circle.draw(win)

    for i in range(total_points):
        # Generate random points
        x = randint(0, window_size)
        y = randint(0, window_size)
        point = Point(x, y)
        
        # Check if the point is inside the circle
        if (x - center.getX())**2 + (y - center.getY())**2 <= radius**2:
            win.plotPixelFast(x, y, "red")
            points_inside_circle += 1
        else:
            win.plotPixelFast(x, y, "blue")
        
        # Update the approximation of pi every 100 points
        if (i + 1) % 100 == 0:
            estimated_pi = (points_inside_circle / (i + 1)) * 4
            print(f"Approximate pi at {i + 1} points: {estimated_pi}")
            win.plotPixel(x, y, "green")

    input("Press ENTER to exit")  # Wait for user input to close the window
    win.close()

def main():
    window_size = int(input("Enter the window width: "))  # Prompt user for window width
    estimate_pi(window_size)  # Call the function to estimate pi

main()
