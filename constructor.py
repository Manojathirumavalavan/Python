class Rect:
    def __init__(self,a,b):
        self.l=a 
        self.b=b 
    def display(self):
        print(self.l*self.b)
    
a=Rect(20,30)
b=Rect(40,50)
a.display()
b.display()