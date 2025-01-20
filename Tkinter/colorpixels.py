from graphics import *

def generate_colorful_window():
    # Generates a 255x255 pixel window with each pixel having a unique color.
    size = 255
    win = GraphWin("Colorful Pixels", size, size)

    for red in range(size):
        for green in range(size):
            # Generate a unique color for each pixel
            blue = (red + green) % size
            color = color_rgb(red, green, blue)
            # Use plotPixel() to display every 150th pixel for results visibility
            if (red * size + green) % 150 == 0:
                win.plotPixel(red, green, color)
            else:
                win.plotPixelFast(red, green, color)
    
    input()
    win.close()

generate_colorful_window()
