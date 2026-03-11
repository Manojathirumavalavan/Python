def sq():
    side=int(input("Enter the side is: "))
    print("Area of square is ",side*side)
def rect(l,b):
    print("Area of reactangle ",l*b)
def tri():
    base=int(input("Enter the base is:"))
    ht=int(input("Enter the ht is:"))
    return 0.5*base*ht
def cir(r):
    return 3.14*r*r
while
print("_____MENU_____")
print("1.SQUARE")
print("2.REACTANGLE")
print("3.TRIANGLE")
print("4.CIRCLE")
print("5.EXIT")
ch=int(input("Enter ur choice:"))
if(ch==1):
    sq()
elif(ch==2):
    l=int(input("Enter length: "))
    b=int(input("Enter breadth:" ))
    rect(l,b)
elif(ch==3):
    x=tri()
    print("Area of triangle is ",x)
elif(ch==4):
    r=int(input("Enter radius:"))
    y=cir(r)
    print("Area of circle is ",y)
else:
    print("Invalid input")
