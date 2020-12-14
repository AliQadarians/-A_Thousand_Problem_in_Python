amount = int(input("Enter amount :"))
rate = float(input("Enter rate : "))
years = int(input("Enter years : "))
fuchreValue = amount * (1 + (0.1 * rate)) ** years
print (" Fucher value is  ",fuchreValue)