from graphics import *
from random import randint

def estimate_pi(window_size, total_points):
    win = GraphWin("Pi Estimation", window_size, window_size)  # Create a graphical window
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
        
        # Check if the point is inside the circle
        if ((x - center.getX())**2 + (y - center.getY())**2 <= radius**2):
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
    # Prompt user for window size and number of points
    window_size = int(input("Enter the window size (<= 1000): "))
    total_points = int(input("Enter the number of points to generate: "))

    # Validate inputs
    if window_size > 1000 or window_size <= 0:
        print("Invalid window size! It should be between 1 and 1000.")
        return
    if total_points <= 0:
        print("Invalid number of points! It should be a positive integer.")
        return

    # Call the function to estimate pi
    estimate_pi(window_size, total_points)

main()
