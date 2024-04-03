import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

def mandelbrot(c, max_iterations=100):
    """
    Compute the Mandelbrot set for a given complex number 'c'.

    The Mandelbrot set is a set of complex numbers for which the iteration of the function
    'z = z * z + c' does not diverge when iterated from 'z = 0'. The function returns the number
    of iterations it took for the absolute value of 'z' to exceed 2, or 'max_iterations' if it
    doesn't exceed 2 within the specified number of iterations.

    Parameters:
    - c (complex): The complex number for which to compute the Mandelbrot set.
    - max_iterations (int): The maximum number of iterations to perform.

    Returns:
    - int: The number of iterations it took for the absolute value of 'z' to exceed 2, or
           'max_iterations' if it doesn't exceed 2 within the specified number of iterations.
    """
    z = c
    for n in range(max_iterations):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iterations

def draw_mandelbrot(ax, x_min, x_max, y_min, y_max, max_iterations=100):
    """
    Draw the Mandelbrot set on the given axes.
    
    Args:
        ax (matplotlib.axes.Axes): The axes to draw on.
        x_min (float): The minimum value on the x-axis.
        x_max (float): The maximum value on the x-axis.
        y_min (float): The minimum value on the y-axis.
        y_max (float): The maximum value on the y-axis.
        max_iterations (int): The maximum number of iterations.
    """
    width, height = 600, 400
    image = np.zeros((height, width, 3), dtype=np.uint8)

    for row in range(height):
        for col in range(width):
            c = complex((col / width) * (x_max - x_min) + x_min,
                        (row / height) * (y_max - y_min) + y_min)
            iterations = mandelbrot(c, max_iterations=max_iterations)
            image[row, col] = [iterations * 5 % 256, iterations * 7 % 256, iterations * 11 % 256]

    ax.imshow(image)
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')

def on_select(eclick, erelease):
    """
    Handle the selection event.
    
    Args:
        eclick (matplotlib.backend_bases.MouseEvent): The click event.
        erelease (matplotlib.backend_bases.MouseEvent): The release event.
    """
    global x_min, x_max, y_min, y_max
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    draw_mandelbrot(ax, x_min, x_max, y_min, y_max)
    fig.canvas.draw()

x_min, x_max = -2, 1
y_min, y_max = -1, 1
MAX_ITERATIONS = 100

fig, ax = plt.subplots(figsize=(8, 6))
draw_mandelbrot(ax, x_min, x_max, y_min, y_max, MAX_ITERATIONS)

toggle_selector = RectangleSelector(ax, on_select, useblit=True,
                                    button=[1, 3], minspanx=5, minspany=5,
                                    spancoords='pixels', interactive=True)

plt.show()