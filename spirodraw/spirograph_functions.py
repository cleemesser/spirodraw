# -*- coding: utf-8 -*-
"""
Functions for having fun with math.  Spirograph-esque drawing.
expects python 3.5+ and numpy for numeric arrays
"""
# import the numeric array trigometric functions
from numpy import cos, sin, pi 

def circle(r: float,theta:float ):
    """parametric function for a circle as a function of increasing theta"
    with angular frequency 1 or $ f= 1/(2\pi) $"""
    return r*cos(theta), r*sin(theta)

def cycloid(r:float,theta:float):
    """a cycloid is the curve generated by a point on the circumference of a circle that
     rolls along a straight line.
     @r is the radius of the circle
     @theta is the angular parameters for rotation of the circle 
     this is stand in for the time parameter
    """
    x = a* (theta-sin(theta))
    y = a* (1-cos(theta))
    return x, y

def prolate_cycloid(a,b,t):
    """cycloids
    prolate cycloid b > a   this makes loops and path extendes outside of circle
    curtate cycloe  b < a   no cusps with this one no loops

    Args:
        a (float): radius the rolling circle
        b (float): radius of the spoke (if b < a) or 
        t (float): rolling parameter each revolution is $2\pi a$

    Returns:
        (float,float): x, y

    reference: https://mathworld.wolfram.com/ProlateCycloid.html
    """
    x = a*t - b * sin(t)
    y = a - b*cos(t)
    return x, y

def epicycloid(a:float,b:float, t:float):
    """an epicycloid is a plane curve tracing the path of a circle as it rolls around the outer 
    circumference of a circle see https://en.wikipedia.org/wiki/Epicycloid

    Args:
        a (float): radius of the larger circle
        b (float): radius of the smaller circle
        t (float): time parameter indicating how far the outer circle has rolled. 
                     Every $2b\pi$ the circle rolls one complete time

    Returns:
        (float,float): x,y values 
    """
    x = (a+b)*cos(t) - b * cos((a+b)*t/b)
    y = (a+b)*sin(t) - b * sin((a+b)*t/b)
    return x,y
    
def hypotrochoid(a,b,d,t):
    """
    a is the radius of the base circle
    q > 1
    b = a/q that of the rolling circle and
    d = k b the distance bewteen the point and the center of the moving circle
    t = time parameter 
    
    z = (a-b) exp(i t) + d exp(-i(q-1) t

    x = a( (q-1) cos(t) + k cos(q-1)t )
    y = a( (q-1) sin(t) -k sin(q-1)t )

    for d=b or k=1, we get the hypocyloids
    a -> a d/b, b -> (a-b) d/b and d -> (a-b) we get the same curve
    so can consider only the cases q>=2 

    for q=2, we get the ellipses
    $$ \frac{x^2}{(1+k)^2} + \frac{y^2}{(1-k)^2} = \frac{a^2}{4} $$

    for q>2 if k<1 : curtate hypocycloid
    for q>2 if k>1 : prolate hypocycloid
    (this is reversed for 1 <q<2)

    Hypotrochoids can also be defined as the trajectories of a movement
    composed of two circlular motions in opposite directions:
    
    $$ z = r_1 e^{i w_1 t} + r_2 e^{- w_2 t} $$

    ellipses if:
       $w_1 = w_2$, 

    prolate hypocycloids if:
       w_1 > w_2 and r_1 w_1 > r_2 w_2  
       w_1 < w_2 and r_1 w_1 > r_2 w_2 

    prolate hypocycloids if:
       w_1 > w_2 and r_1 w_1 < r_2 w_2 or w_1 < w_2 and r_1 w_1 > r_2 w_2 

    https://www.geogebra.org/classic/scmy5ya2    
    
    """
    q = a/b
    
    x = a*( (q-1) * cos(t) + k*cos((q-1)*t) )
    y = a*( (q-1) * sin(t) - k*sin((q-1)*t) )
    return x,y


def hypocycloid(a,b,t):
    """
    
    Parametric function that describes the path drawn out by a point
    on a small circle with diameter b inside a larger circle of
    diameter a.  This is done as a function of t "time"

    For visual display, there are certain cases which look This is what 
    a > b
    generally you want to avoid a == 2*b because it makes a straight line

    Note that the first terms are the equation for circle of radius
    r = (a-b) which describes the movement of the center of the smaller circle

    $$ x = (a-b) \cos(t) + b \cos((a-b)t/b) $$
    $$ y = (a-b) \sin(t) - b \sin((a-b)t/b) $$


    Returns:
        (float,float): x,y vector values in the plane


    in geogebra: Curve((a-b) cos(t)+b cos((a-b)*((t)/(b))),(a-b) sin(t)-b sin((a-b)*((t)/(b))),t,0,t1)
    https://www.geogebra.org/classic/pa8pv8jk
    double spirograph2

    https://www.geogebra.org/classic/ag6pc795  -  spirograph4 (adds derivative)
    """
    x = (a-b)*cos(t) + b*cos((a-b)*t/b)
    y = (a-b)*sin(t) - b*sin((a-b)*t/b)
    return x,y


def hypocycloid_factory(a,b):
    """
    return two python functions which describe the x-axis and y-axis
    components for a cycloid with outer circle radius $a$ and rotating
    circle with radius $b$

    returns:
        x(t), y(t)  : tuple of python functions
    """
    def x(t):
        return hypocycloid(a,b,t)[0]
    def y(t):
        return hypocycloid(a,b,t)[1]
    return x,y

def x_hypocycloid(a,b,t):
    x = (a-b)*cos(t) + b*cos((a-b)*t/b)
    return x
    
def y_hypocycloid(a,b,t):
    
    y = (a-b)* sin(t)- b*sin((a-b)*t/b)
    
    return y

def test_1():
    a = 3.0
    b = 1.0
    r1 = a-b
    print(a,b,r1)
    t=0.9
    print(r1 * sin(t))
    print(b * sin( r1 * t/b))


if __name__ == '__main__':
    test_1()

    
