
# Accept string which has repitative charcters consigetively & optimize storage space for the same
# Input : aaabbccccddddddaa
# Output : a3b2c4d5a2


def OptStorage(str1):
    count = 1
    temp = str1[0]
    
    for x in str1[1:]:
        if x==temp:
            count+=1

        else:
            print (temp + str(count),end='')
            temp = x
            count = 1
    print (temp + str(count))

def main():
    var1 = str(input("Enter String : "))
    print ("Optimize string is:")
    OptStorage(var1)
    
if __name__ == "__main__":
    main()    





