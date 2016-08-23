class box():
    def __init__(self, width, height): # parameter creation
        self.width = width # assignment
        self.height = height # assignment
    def area(self):
        return self.height * self.width # area of the box class
x = box(20,10) # calling the class through a variable
print x.area() # getting the area