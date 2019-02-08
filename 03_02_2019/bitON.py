
# wap to accept no. from user and no. bits to turn ON from given position


def bitON(No,position,bit=1):
    x=1<<bit-1
    x=x<<(position-bit)

    return No | x

def main():
    num,position,bits = eval(input("Enter No,position,no of bits "))
    result=bitON(num,position,bits)
    print("Output is : " + str(result))
    

if __name__ == "__main__":
    main()
    

