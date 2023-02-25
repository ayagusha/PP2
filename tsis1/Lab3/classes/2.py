class Shape: 
    def __init__(self): 
        self.area = 0 
 
    def Area(self): 
        print(self.area) 
 
class Square(Shape): 
    def __init__ (self, length): 
        self.length = length 
         
    def Area(self): 
        self.area = self.length ** 2 
        print(self.area) 
 
length = int(input()) 
x = Square(length) 
x.Area()