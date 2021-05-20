#use python to read text files and recognize patterns 
#create a strong password detection and a password generator that is strong

import re
import random
#REG EX NUMBER 1 

# read a text file and count the number of words containing cat or dog
def problem1():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    catDogRegex = re.compile(r'\w*((cat)|(dog))\w*')
    number = 0
    for i in text:
        mo = catDogRegex.search(i)
        if mo:
            number += 1
    print(number, " cat or dog words")

# How many four letter words are there in a text file
def problem2():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    fourRegex = re.compile(r'^\w{4}$')
    number = 0
    for i in text:
        mo = fourRegex.search(i)
        if mo:
            number += 1
    print(number, "four letter words")    

# How many words contain hun
def problem3():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    hunRegex = re.compile(r'\w*hun\w*')
    number = 0
    for i in text:
        mo = hunRegex.search(i)
        if mo:
            number += 1
    print(number, " hun words")

# how many words end in ing or ion
def problem4():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    ingRegex = re.compile(r'\w*ing$')
    ionRegex = re.compile(r'\w*ion$')
    numberIng = 0
    numberIon = 0
    for i in text:
        mo  = ingRegex.search(i)
        mo2 = ionRegex.search(i)
        if mo:
            numberIng += 1
        if mo2:
            numberIon += 1
    print(numberIng, "words end with -ing")
    print(numberIon, "words end with -ion")

# how many words contain a q that is not followed by a u
def problem5():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    qRegex = re.compile(r'\w*(q|Q)([a-t]|[v-z]){1}\w*')
    number = 0
    accum = ""
    for i in text:
        mo = qRegex.search(i)
        if mo:
            number += 1
            accum += i + " "
    print(number, "q not followed by u words")
    print(accum)

# how many words contain no vowels 
def problem6():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    noVowelRegex = re.compile(r'^[BCDFGHJKLMNPQRSTVWXYZ]?[bcdfghjklmnpqrstvwxyz]+$')
    number = 0
    for i in text:
        mo = noVowelRegex.search(i)
        if mo:
            number += 1
    print(number, " no vowel words")

# how many words have only vowels in them
def problem7():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    VowelRegex = re.compile(r'^[AEIOU]?[aeiou]+$')
    number = 0
    for i in text:
        mo = VowelRegex.search(i)
        if mo:
            number += 1
    print(number, "only vowerls words")

#how many words end in 'nt
def problem8():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    notRegex = re.compile(r"('nt)$")
    number = 0
    for i in text:
        mo = notRegex.search(i)
        if mo:
            number += 1
    print(number, "words that have 'nt words")

#how many words with two vowels in a row are there
def problem9():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    twoInARowRegex = re.compile(r'(([AEIOU]|[aeiou])[aeiou])')
    number = 0
    for i in text:
        mo = twoInARowRegex.search(i)
        if mo:
            number += 1
    print(number, "two vowels in a rowwords")  

#how many words have at least two vowels in there regardless of the position. 
def problem10():
    text = open('words.txt', 'r')
    text = text.read()
    text = text.split("\n")
    twoRegex = re.compile(r"([AEIOU]|[aeiou])[^aeiou]*[aeiou]")
    number = 0
    for i in text:
        mo = twoRegex.search(i)
        if mo:
            number += 1
    print(number, "words that contain at least two vowels")



#REG EX NUMBER 2
#Check if the input name contains the last name "Nakamoto"
def nameMatch(): # DONE 
    n = input("Put the name")
    RegexName = re.compile(r'[A-Z][a-z]* Nakamoto')
    mo = RegexName.search(n)
    if mo:
        print(True)
    else:
        print(False)

#Check if the user puts a correct number in words like sixty-five etc. 
def moneyMatch(): # DONE 
    n = input("Put the number ")
    RegexName = re.compile(r'(twenty|thirty|forty|sixty|seventy|eighty|ninety)(-one|-two|-three|-four|-five|-six|-seven|-eight|-nine)?$')
    mo = RegexName.search(n)
    if mo:
        print(True)
    else:
        print(False)

#Regex that checks if an input dollar sum is a valid input (follows the $xxx,xxx,xxx pattern that we usually write
#Money problem #DONE
#Reg ex $10000
def moneyVerifyier():
    regExMoney = re.compile(r'\$((\d{4})|((\d{3}(\,))*(\d{3})))\.?(\d\d)?')
    regExMoney2 = re.compile(r'\$(\d{2}(\,))(\d{3})\.?(\d\d)?')
    regExMoney3 = re.compile(r'\$\d{3}\.?(\d\d)?')
    regExMoney4 = re.compile(r'\$(\d(\,))(\d{3}(\,))*(\d{3})\.?(\d\d)?')
        
    n = input("Put the amount of money here: ")
    mo = regExMoney.fullmatch(n)
    mo2 = regExMoney2.fullmatch(n)
    mo3 = regExMoney3.fullmatch(n)
    mo4 = regExMoney4.fullmatch(n)
                            # it gives error sometimes hwen it doesnt find a match 
    if mo or mo2 or mo3 or mo4:
        print(True)
    else:
        print(False)

#Detect if a password is strong. Strong passwords are at least eight characters long, contain both uppercase and lowercase characters and 
#have at least one digit. 
#Reg ex Password #DONE
def passwordStrength():
    charRegex = re.compile(r'(\w{8,})')  # Check if password has atleast 8 characters
    lowerRegex = re.compile(r'[a-z]+') # Check if at least one lowercase letter
    upperRegex = re.compile(r'[A-Z]+')# Check if atleast one upper case letter
    digitRegex = re.compile(r'[0-9]+') # Check if at least one digit.
    anyCharRegex = re.compile(r'[$^&*#@\\)(!]') # includes cases like $ and #
    n = input("Put the password here: ")
    mo = charRegex.search(n)
    mo1 = lowerRegex.search(n)
    mo2 = upperRegex.search(n)
    mo3 = digitRegex.search(n)
    mo4 = anyCharRegex.search(n)
    if mo and mo1 and mo2 and mo3 or mo4:
        print("Password is strong")
        print("True")
    else:
        print("Password is weak")
        print("False")

#Reccomends a strong password based on an input text file. You pick four words from a textfile at random and combine to create a strong password. 
#Reg ex Recommendation password # DONE 
def passwordRecommend():
    text = open("words.txt" , "r")
    wordRegEx = re.compile(r'[a-z]{4}')
    emptyLst =[]
    accum = ""
    for i in text:
       mo = wordRegEx.search(i)
       if i[0] in "ABCDEFGHIJKLMMNOPQRSTUVWXYZ": # could do it with regex by having the first char be a lowercase ^[a-z]
           continue
       else:
           if mo:
               emptyLst.append(i)

    for j in range(4):
       random.shuffle(emptyLst)
       k = emptyLst[0]
       k = k.strip("\n") # removes the new line attached from the file reading
       accum += " " +str(k)

    print("The Passowrd we recommend is " + '"' + accum + ' "')
