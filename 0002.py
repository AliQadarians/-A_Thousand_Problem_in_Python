PI=3.14
height=float(input("Enter height of cylinder :  "))
radius=float(input("Enter radius of cylinder :  "))
volum=PI*(radius**2)*height
surfaceArea=((2*PI*radius)*height)+(2*(PI* radius**2))
print("volum of cylinder is {}".format(volum))
print("surface area of cylinder is {}".format(surfaceArea))

