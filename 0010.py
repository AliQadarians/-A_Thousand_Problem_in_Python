salary = float(input("Enter emploee salaries :  "))
insurance = (salary *7) / 100
taxation = (salary * 10 ) / 100
income = salary - insurance - taxation
print("Salary = ",salary)
print("Insurance = ",insurance)
print("Tax = ",taxation)
print("Income = ",income)