"""
Hinton diagrams in matplotlib.

A Hinton diagram is useful for visualizing a matrix of signed weights.
In the diagram, each matrix element is represented by a square whose
color indicates the sign and whose area represents the magnitude.

"""

import matplotlib.patches as mpatches
import pylab as p
import numpy as n

def _add_centered_square(ax, xy, area, **kwargs):
    size = n.sqrt(area)
    loc = n.asarray(xy) - size/2.
    rect = mpatches.Rectangle(loc, size, size, **kwargs)
    ax.add_patch(rect)

def hinton(a, ax=None):
    """
    Draw a Hinton diagram for the 2D array `a` on the axes.

    Elements of `a` should range between -1 and 1. Each element will
    be represented by a square which is white for positive values, or
    black for negative values, with an area proportional to its
    magnitude.

    The diagram will be drawn on the current axes, or the one
    specified by `ax`. It will look best for axes whose aspect ratio
    matches that of the matrix being diagrammed.

    """
    if ax is None:
        ax = p.gca()
    ax.patch.set_facecolor('gray')
    for xy, val in n.ndenumerate(a):
        color = 'w' if val > 0 else 'k'
        _add_centered_square(ax, n.asarray(xy) + .5,
                             abs(val), color=color)
    ax.autoscale_view()

if __name__ == "__main__":
    p.figure(figsize=(4,4))
    a = n.random.uniform(low=-1., high=1., size=(10,10))
    hinton(a)
    p.show()
