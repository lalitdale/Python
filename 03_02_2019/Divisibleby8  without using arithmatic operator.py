
# wap to accept a number from user and check if it is divisible by 8 or not without using arithmatic operators

def Isdivisible(num):
    
    temp = num>>3
    temp1 = temp<<3
    if num==temp1:
        return True
    else:
        return False

def main():
    num = int (input ("Enter Number : "))
    res = Isdivisible(num)
    if res == True:
        print("Number is divisible by 8")
    else:
        print("Number is not divisible by 8")
    
if __name__ == '__main__':
    main()
