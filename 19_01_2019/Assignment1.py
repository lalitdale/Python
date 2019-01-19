

# wap to accept 3 numbers from user and print minimum of them

number1,number2,number3 = eval (input ("Enter 3 numbers : "))

if number1 < number2 and number1 < number3 :
    minimum = number1

elif number2 < number3 :
    minimum = number2

else:
    minimum = number3
    
print ("Minimum of 3 numbers is : " + str(minimum))

