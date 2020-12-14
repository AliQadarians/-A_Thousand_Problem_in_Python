from math import tan,pi
numberOfSides=int(input("Enter number of sides :  "))
lenghOfASide=float(input("Enter lengh of a sides : "))
areaOfThePolygon=(numberOfSides * lenghOfASide**2)/(4 * tan(pi/numberOfSides))
print("area of the polygon is {}".format(areaOfThePolygon))

