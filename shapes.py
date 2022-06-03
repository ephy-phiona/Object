# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr



class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area (self):
        return self.radius**2*3.14  
     

    def circumference(self):
        return self.radius *3.14

class Square:
    def __init__(self,side):
        self.side=side
          
    def Area(self):
        return self.side**2   

    def perimeter(self):
        return 4 *  self.side   


class Rectangular:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        w=2*(self.length * self.width)
        return w
    def perimeter(self):
        h=  2*(self.length + self.width)  
        return h

class Sphere:
    def __init__(self,radius):
         self.radius=radius

    def calculate_area(self):
        Area=4*3.14*self.radius**2
        return Area

    def Volume(self):
        volumes=(4/3)*3.14* self.radius*self.radius 
        return volumes  
                  