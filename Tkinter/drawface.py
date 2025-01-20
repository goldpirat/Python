from graphics import *

def main():
    """Draws a face using different shapes."""
    win = GraphWin("Face Drawing", 200, 200)

    # Draw ears using ovals and the color tan
    left_ear = Oval(Point(10, 80), Point(30, 120))
    left_ear.setFill("tan")
    left_ear.draw(win)

    right_ear = Oval(Point(170, 80), Point(190, 120))
    right_ear.setFill("tan")
    right_ear.draw(win)

    # Draw head using an oval
    head = Rectangle(Point(30, 50), Point(170, 180))
    head.setFill("peachpuff") # closest color to skin color I could find
    head.draw(win)

    # Draw hair using a rectangle
    hair = Rectangle(Point(30, 30), Point(170, 70))
    hair.setFill("yellow") # Blonde
    hair.draw(win)

    # Draw eyes using circles as well as pupils for eye color
    left_eye = Circle(Point(70, 90), 15)
    left_eye.setFill("white")
    left_eye.draw(win)

    left_pupil = Circle(Point(70, 90), 5)
    left_pupil.setFill("brown")
    left_pupil.draw(win)

    right_eye = Circle(Point(130, 90), 15)
    right_eye.setFill("white")
    right_eye.draw(win)

    right_pupil = Circle(Point(130, 90), 5)
    right_pupil.setFill("brown")
    right_pupil.draw(win)

    # Draw a triangle for the nose
    nose = Polygon(Point(100, 110), Point(110, 140), Point(90, 140))
    nose.setFill("brown")
    nose.draw(win)

    # Draw a smiling mouth using a stretched oval
    mouth = Oval(Point(80, 150), Point(120, 170))
    mouth.setOutline("black")
    mouth.setFill("pink") # For lips
    mouth.draw(win)

    input()
    win.close()

main()
