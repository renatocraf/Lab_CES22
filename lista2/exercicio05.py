class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def print_point(pt):
        print("({0}, {1})".format(pt.x, pt.y))
    
    def __str__(self):    # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)
    
    def midpoint(p1, p2):
        mx = (p1.x + p2.x)/2
        my = (p1.y + p2.y)/2
        return Point(mx, my)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def reflect_x(self):
        return (self.x,-self.y)


x = Point(3,5).reflect_x()

print(x)
    




    

