

# wap to accept string from user and return string adding first 2 and last 2 charcters of input string.

Input = str (input ("Enter String : "))

Result1 = Input[0:2]

# print ("Output is : " + Result1)

length = Input.__len__()

Result2 = Input[length-2:]

# print ("Output is : " + Result2)

Final_Output = Result1 + Result2

print ("Output is : " + Final_Output)



