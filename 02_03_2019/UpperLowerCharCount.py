
def UpperLowerCount (sentence):
    output={"UpperChar":0,"LowerChar":0}
    count1=0
    count2=0
    for x in sentence:
        if x.isupper() == True:
            count1 += 1
        elif x.islower()== True:
            count2 += 1

    output["UpperChar"] = count1
    output["LowerChar"] = count2
    return output

def main():
    sentence = eval(input("Enter Sentence : "))
    temp=UpperLowerCount(sentence)
    print(temp)

if __name__=="__main__":
    main()
