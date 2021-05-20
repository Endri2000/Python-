 
def main():
 done = False
 while not done:
   word = input("Put the word you want converted here: ")
   word = word.lower() # makes it lowercase
   if word == "done":
     done = True
     return
   findFirstVowel(word)
   convertToPigLatin(word)
   reverse(word)
   encryption(word)
def findFirstVowel(word):
 vowels = 0
 for i in range((len(word))):
   if word[i] in "aeiou":
     vowels +=1
     return int(i)
 if vowels == 0:
    return -1
 
def convertToPigLatin(word):
 if findFirstVowel(word) == 0:
     print("The Pig Latin form is " + "\t" + word[1:] + word[findFirstVowel(word)] + "way")
 elif findFirstVowel(word) !=0 and findFirstVowel(word) !=-1: 
   for i in range((len(word))):
         if word[findFirstVowel(word)] in "aeiou":
           print("The Pig Latin form is "+ "\t"+ word[findFirstVowel(word):] + word [:findFirstVowel(word)] + "ay")
           break
 elif findFirstVowel(word) == -1:
   print("The Pig latin form of the word is"+"\t" + word)
 
def reverse(word):
 reverse = word[::-1]
 print("The reverse form of the word is " + "\t" + reverse)
def encryption(word):
 key = 13
 cipherText = ""
 for i in word:
   value = ord(i) - ord("a")
   Encryptedvalue = (value + key) % 26
   EncryptedLetter = chr(Encryptedvalue + ord("a"))
   cipherText += EncryptedLetter
 print("The encrypted word is" + "\t" +cipherText)
main()
