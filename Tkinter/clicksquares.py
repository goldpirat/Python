from graphics import *

def main():
    win = GraphWin()
    # Since original Circle was 20 points we make square that size too
    shape = Rectangle(Point(50, 50), Point(80,80))
            #Square is just a rectangle with equal sides. 20 units
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        # To make it on click we can simply make a copy of the original
        # For each click provided and move it to the click position and draw
        new_shape = shape.clone()
        new_shape.move(dx, dy) # Moves the shape to the new position
        new_shape.draw(win) # Draws the shape

    win.close()

main()
