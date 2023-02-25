class Student: 
    def __init__(self): 
         
        self.name = '' 
        self.id = '' 
 
    def GetString(self): 
        self.name = str(input()) 
        self.id = str(input()) 
         
    def PrintString(self): 
        name = self.name.upper() 
        id = self.id.upper() 
        print(name, id) 
 
x = Student()   
x.GetString() 
x.PrintString()
