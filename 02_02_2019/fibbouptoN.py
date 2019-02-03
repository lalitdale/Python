
# Print fibonacci series upto n


def fibo(number):
    temp1=1
    temp2=1
    print(temp1,temp2,end=' ')
    while True:
        temp3=temp1+temp2
        if(temp3>number):
            break
        print(temp3,end=' ')
        temp1=temp2
        temp2=temp3        


def main ():
    no=int(input("Enter Number :"))
    fibo(no)

if __name__ == '__main__':
    main()

