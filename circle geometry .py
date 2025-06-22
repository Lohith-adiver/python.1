print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def point_in_circle(circle, point):
    dx = circle.center.x - point.x
    dy = circle.center.y - point.y
    distance = math.hypot(dx, dy)
    return distance <= circle.radius

def rect_in_circle(circle, rect):
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return all(point_in_circle(circle, pt) for pt in corners)

def rect_circle_overlap(circle, rect):
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return any(point_in_circle(circle, pt) for pt in corners)

# Example test
c = Circle(Point(150, 100), 75)
r = Rectangle(Point(130, 90), 20, 20)
p = Point(160, 100)

print("Point in Circle:", point_in_circle(c, p))
print("Rectangle in Circle:", rect_in_circle(c, r))
print("Rectangle overlaps Circle:", rect_circle_overlap(c, r))
