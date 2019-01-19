

#accept two string from user and check if second string is rotation of first

input1 = str (input ("Enter first String : "))

input2 = str (input ("Enter second string: "))

length1 = len(input1)
length2 = len(input2)

if length1 == length2 :
    
    temp = input1 + input1

    if input2 in temp :
        print ("rotation present")
    else :
        print ("rotation NOT present")

else :
    print ("Invalid input")
