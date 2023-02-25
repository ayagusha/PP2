class Point: 
    def __init__(self,x1,y1): 
        self.x1 = x1 
        self.y1 = y1 
 
    def show(self): 
        print(f"Coordinates of point: ({self.x1} ; {self.y1})") 
     
    def move(self): 
        print("Write a new coordinates for second point: ") 
        self.x2 = int(input()) 
        self.y2 = int(input()) 
     
    def dist(self): 
        self.d = (((self.y1**2) + (self.x1**2))**0.5) - (((self.y2**2) + (self.x2**2))**0.5) 
        if self.d < 0: 
            self.d *= -1 
        print(f"Distance between ({self.x1};{self.y1}) and ({self.x2};{self.y2}) = {self.d}") 
 
x = Point(1,1) 
x.show() 
x.move() 
x.dist()