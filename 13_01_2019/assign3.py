

#accept two string from user and check if second string is rotation of first


print ("Enter first String : ")
input1 = str (input ())

print ("Enter second string: ")
input2 = str (input ())
   
temp = input1 + input1

print ("output : " + str (input2 in temp))
