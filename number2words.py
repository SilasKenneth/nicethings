import random
from fractions import Fraction
#TODO :DONE Add the functionality for decimal numbers
def numbersTowords(number):
    numbers=["zero","one","two","three","four","five","six","seven","eight","nine"]
    digits={1:"Hundred",2:"thousand",3:"million",4:"billion"}
    others={10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"Seventeen",18:'eighteen',19:'nineteen'}
    startingwith={2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:'ninety'}

    #Get the number of digits
    original=number
    if isinstance(number,float):
        floating=[int(x) for x in (str(number).split(".")[-1])]
    else:
        pass
    number=int(number)
    negative=number
    number=abs(number)
    getthem=[int(x) for x in str(number)]
    words=[]
    if len(getthem)<3 and not len(getthem) <=0 and not number in range(10,20):
        if number in range(0,10):
            words.append(numbers[number])
        else:
            if(getthem[-1]==0):
                words.append("")
                words.insert(0,startingwith[getthem[0]])
            else:
                words.insert(0,startingwith[getthem[0]])
                words.append(numbers[getthem[-1]])
    if number in range(10,20):
        words.append(others[number])
    if len(getthem)==3:
        newtoindex=getthem[-3:]
        if len(getthem)==3:
            words.insert(0,numbers[getthem[0]])
            if getthem[-1]==0:
                words.insert(len(getthem)-1,"")
                if(newtoindex[1]==0):
                    words.append(digits[1])
                    words.append("")
                elif newtoindex[1]==1:
                    words.append(digits[1])
                    words.append("and")
                    if newtoindex[-1]==0:
                        words.append(others[int(str(newtoindex[1]) + str(newtoindex[-1]))])
                        words.append("")
                    else:
                        words.append(others[int(str(newtoindex[1]) + str(newtoindex[-1]))])
                        words.append(startingwith[getthem[newtoindex[1]]])
                else:
                    words.append(digits[1])
                    words.append("and")
                    words.append(startingwith[newtoindex[1]])
                    if getthem[-1]==0:
                        words.append("")
                    else:
                        words.append(numbers[newtoindex[-1]])
            else:
                words.append(digits[1])
                words.append("and")
                if newtoindex[1]==1:
                    words.append(others[int(str(newtoindex[1])+str(newtoindex[-1]))])
                elif newtoindex[1]==0:
                    words.append("")
                    words.append(numbers[newtoindex[-1]])
                else:
                    words.append(startingwith[getthem[-2]])
                    words.append(numbers[newtoindex[-1]])
    elif len(getthem)>3:
        pass
    if isinstance(original,float):
        if negative < 0:
            words.insert(0,"Negative")
        return " ".join(words).strip().capitalize() + convertDecimalParts(floating)
    else:
        if negative<0:
            words.insert(0,"Negative")
        return " ".join(words).strip().capitalize()
def convertDecimalParts(decimal):
    words=[]
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit in decimal:
        words.append(numbers[digit])
    return " point "+ " ".join(words).strip()

#TODO :DONE Fix the bug of the numbers beyond [1-9][2-9][.]
# if its greater than 3 the get each digit value and + with the number
