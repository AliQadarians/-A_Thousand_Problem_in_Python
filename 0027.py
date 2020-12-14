number1 = int(input("Enter number one : "))
number2 = int (input("Enter number two : "))
sum = number1 + number2
print("{} + {} = {}".format(number1,number2 ,sum))
mul = number1 * number2
print("{} * {} = {}".format(number1,number2,mul))
if number2 == 0 :
    print("{} / {} = infinity ".format(number1,number2))
    print("{} mod {} = {}".format(number1,number2,number1))
else :
    div = number1 / number2
    print("{} / {} = {}".format(number1,number2,div))
    mod = number1 % number2
    print("{} % {} = {}".format(number1,number2,mod))
