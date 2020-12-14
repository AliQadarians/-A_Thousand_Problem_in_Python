lastYearsPrice = float(input("Enter last year's price : "))
thisYearsPrice = float (input("Enter this year's price : "))
inflationRate = (thisYearsPrice - lastYearsPrice) / lastYearsPrice
nextYearsPrice = lastYearsPrice + (thisYearsPrice * inflationRate)
print("**************************")
print("Inflation rate = {}%".format(inflationRate))
print("Next year's Price = ",nextYearsPrice)