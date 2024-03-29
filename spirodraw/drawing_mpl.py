# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pyplot

from .spirograph_functions import hypocycloid_factory

# %%
def start_drawing():
    fig, ax = pyplot.subplots()
    ax.set_frame_on(False)
    ax.set_axis_off()
    ax.set_aspect("equal", "datalim")
    return fig, ax
# %% 
def add_hypocycloid(ax, big_radius, little_radius, t0=0, t1=100.0, steps=10000):
    ts = np.linspace(t0, t1, steps)
    x, y = hypocycloid_factory(big_radius, little_radius)
    xs, ys = x(ts), y(ts)
    ax.plot(xs, ys)
    return ax

# %%
def example_spiro1():

    # generate an array of equally spaced time points from 0 to 100
    # to act as the discrete input for the parameterized variable
    fig, ax = start_drawing()
    
    ts = np.linspace(0, 100.0, 10000)
    a = 5.0
    b = 2.0 
    print(f"drawing hypocycloid with radii {a}, {b}")
    x, y = hypocycloid_factory(a, b)

    xs, ys = x(ts), y(ts)
    ax.plot(xs, ys)
    
    
    a =10.0
    b = 2.2
    print(f"drawing hypocycloid with radii {a}, {b}")
    x, y = hypocycloid_factory(a, b)
    xs, ys = x(ts), y(ts)
    ax.plot(xs, ys)
    print(f"drawing hypocycloid with radii 15.0, 2.13")
    x, y = hypocycloid_factory(15.0, 2.13)
    xs, ys = x(ts), y(ts)
    ax.plot(xs, ys)
    
    return fig, ax


# %%
def example_spiro2():
    """
    generate a random picuture
    """

    # generate an array of equally spaced time points from 0 to 100
    # to act as the discrete input for the parameterized variable
    ts = np.linspace(0, 100.0, 10000)

    N = np.random.randint(3, 8+1)
    fig, ax = pyplot.subplots()
    ax.set_frame_on(False)
    ax.set_axis_off()
    ax.set_aspect("equal", "datalim")
    
    for ii in range(N):
        a = 10.0 * np.random.ranf()
        b = 5.0 * np.random.ranf()
        x, y = hypocycloid_factory(a, b)
        xs, ys = x(ts), y(ts)
        ax.plot(xs, ys)
        # pyplot.plot(xs,ys, aspect=1.0) # not right so set below

    
    return fig, ax


def example_random_spiro3():
    """
    generate a random picuture
    """

    # generate an array of equally spaced time points from 0 to 100
    # to act as the discrete input for the parameterized variable
    ts = np.linspace(0, 200.0, 10000)

    N = np.random.randint(1, 11+1)

    fig, ax = pyplot.subplots()
    ax.set_frame_on(False)
    ax.set_axis_off()
    ax.set_aspect("equal", "datalim")

    for ii in range(N):
        a = 10.0 * np.random.ranf()
        b = 5.0 * np.random.ranf()
        x, y = hypocycloid_factory(a, b)
        xs, ys = x(ts), y(ts)
        ax.plot(xs, ys)
    
    return fig, ax


def safe_float_input(s):
    while 1:
        r = input(s)
        if len(r) == 0:
            continue
        if r[0].isdigit() or r[0] == ".":
            res = float(r)
            return res
        else:
            print("that wasn't a number. Try again.")


def interactive_spiro(display=True):
    """
    generate a picture based upon input from the keyboard
    in the python2.7 days (2000's) this worked well with ipython -pylab and TkAgg backend
    """

    # generate an array of equally spaced time points from 0 to 100
    # to act as the discrete input for the parameterized variable
    ts = np.linspace(0, 200.0, 10000)

    N = np.random.randint(1, 7 + 1)
    print("Making a figure with %d hypocycloids..." % N)
    fig, ax = pyplot.subplots()

    ax.set_frame_on(False)  
    ax.set_axis_off()
    ax.set_aspect("equal", "datalim")

    l = []
    for ii in range(N):
        # a = 10.0 * np.random.ranf()
        # b =  5.0 * np.random.ranf()
        a = safe_float_input("enter a value for the larger circle radius (a): ")
        b = safe_float_input("enter a value for the smaller circle radius (b): ")
        l.append((a, b))
        x, y = hypocycloid_factory(a, b)
        xs, ys = x(ts), y(ts)
        ax.plot(xs, ys)
        # pyplot.plot(xs,ys, aspect=1.0) # not right so set below
        
    if display:    
        pyplot.show()  # display the plot
    return ax


def spiro5():
    """
    generate a random sprigraph picture
    """

    # generate an array of equally spaced time points from 0 to 100
    # to act as the discrete input for the parameterized variable
    ts = np.linspace(0, 200.0, 10000)

    N = 12
    print("Making a figure with %d hypocycloids..." % N)
    fig, ax = pyplot.subplots()
    ax.set_frame_on(False)
    ax.set_axis_off()
    ax.set_aspect("equal", "datalim")
    
    for ii in range(N):
        # a = 10.0 * np.random.ranf()
        # b =  5.0 * np.random.ranf()
        a = safe_float_input("enter a value for the larger circle radius (a): ")
        b = safe_float_input("enter a value for the smaller circle radius (b): ")
        x, y = hypocycloid_factory(a, b)
        xs, ys = x(ts), y(ts)
        ax.plot(xs, ys)
        # pyplot.plot(xs,ys, aspect=1.0) # not right so set below
    return fig, ax         
        


def spiro_random(N=12):
    """
    generate a random picuture
    """
    
    # generate an array of equally spaced time points from 0 to 100
    # to act as the discrete input for the parameterized variable
    ts = np.linspace(0, 200.0, 10000)

    print("Making a figure with %d hypocycloids..." % N)
    fig, ax = pyplot.subplots()
    ax.set_frame_on(False)
    ax.set_axis_off()
    ax.set_aspect("equal", "datalim")
    
    for ii in range(N):
        scale = 3*(ii+1)/N # make it so they get bigger as you make more
        a = int(scale* np.random.randint(3,17))
        b = int(scale* np.random.randint(2,15))
        print(a,b)
        # a = safe_float_input("enter a value for the larger circle radius (a): ")
        # b = safe_float_input("enter a value for the smaller circle radius (b): ")
        x, y = hypocycloid_factory(a, b)
        xs, ys = x(ts), y(ts)
        ax.plot(xs, ys)
        # pyplot.plot(xs,ys, aspect=1.0) # not right so set below

    return fig, ax


if __name__ == "__main__":
    # simple test requires matplotlib

    numbers = interactive_spiro()
    print(f"generated a spirgraph with radii of: {numbers}")
