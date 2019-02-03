
# print following pattern
# * * * *
# * * *
# * *
# *


def Pattern(n):
    
    for x in range(n,0,-1):
        for _ in range(0,x):
            print("*",end=' ')

        print()

def main():
    no=int(input("Enter Number :"))
    Pattern(no)

if __name__ == '__main__':
    main()
