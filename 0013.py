number = int(input("Enter a number :    "))
copyOfNumber = number
invertedNumber = 0
sumOfNumber = 0
while copyOfNumber > 0 :
    invertedNumber = ( invertedNumber * 10 ) + ( copyOfNumber % 10 )
    sumOfNumber += ( copyOfNumber % 10 )
    copyOfNumber //= 10

print("Number = ",number)
print("Sum of number =  ",sumOfNumber)
print("Inverted number = ",invertedNumber)
