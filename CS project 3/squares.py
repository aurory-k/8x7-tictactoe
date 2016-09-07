from graphics import *

class Square(object):
    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    checker = 0

def make_square(x1,y1,x2,y2):
    square = Square()
    square.x1 = x1
    square.y1 = y1
    square.x2 = x2
    square.y2 = y2
    square.checker = 0
    square.a = Point(x1,y1)
    square.b = Point(x2,y2)
    square.mid = Point(x1+25, y2-25)
    square.cross1 = Point(x1+8,y1)
    square.cross2 = Point(x2-8,y2)
    square.cross3 = Point(x1+42, y1)
    square.cross4 = Point(x2-42, y2)
    square.checkerWidth = 10
    square.circleRadius = 15

    return square
