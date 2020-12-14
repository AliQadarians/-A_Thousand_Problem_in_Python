OneYearInSeconds =3.156e7
OneYearInSeconds1 = 3.156 * 10**7
ageByYear = int(input("Enter your age by year : "))
ageBySeconds = int( OneYearInSeconds1 * ageByYear )
if ageBySeconds == 1 :
    print("{} year is {} per second".format(ageByYear,ageBySeconds))
else:
    print("{} years is {} per second".format(ageByYear,ageBySeconds))