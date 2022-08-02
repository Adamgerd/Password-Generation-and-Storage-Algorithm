#Password Generation and Storage Algorithm

#Module Import
import random

#Custom Variable to check if the combination already exists (0=No, 1=Yes)
var = 0

#Shuffle Function
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Sitename Input
sitename=input("Enter the name of the site for the password you require?\n")

#Creates the Password File
with open('python passwords.txt', 'a', encoding='utf-8') as f:
    f.write("")
    
#Checks for Input in File
f = open('python passwords.txt', "r",encoding='utf-8').read().splitlines()
for line in f:
    if sitename in line: #combination Found
        print("A site and password combination has been found.")
        var = 1
        
#ASCII Digit Generator Using the ASCII Code Table
uppercaseLetter=chr(random.randint(65,90)) #A random uppercase ASCII letter
lowercaseLetter=chr(random.randint(97,122)) #A random lowercase ASCII letter
decimalLetter=chr(random.randint(48,57)) #A random decimal ASCII letter
randomdigitlist=[*range(48,57),*range(65,90),*range(97,122)] #Range of ASCII letters+numbers
randomdigitletter1=chr(random.choice(randomdigitlist)) 
randomdigitletter2=chr(random.choice(randomdigitlist))
randomdigitletter3=chr(random.choice(randomdigitlist))
randomdigitletter4=chr(random.choice(randomdigitlist))
randomdigitletter5=chr(random.choice(randomdigitlist))

#Password Generation
password=uppercaseLetter+lowercaseLetter+decimalLetter+randomdigitletter1+randomdigitletter2+randomdigitletter3+randomdigitletter4+randomdigitletter5
password=shuffle(password)

#Combination Not Found
if var == 0:
    print("No site and password combination has been found, a new combination has been printed.")

#Password Storage in a UTF-8 Text File
with open('python passwords.txt', 'a', encoding='utf-8') as f:
    if var == 0:
        f.write("% s % s"%(sitename,password))
        f.write("\n")

var = 0

#Password Output 
f = open('python passwords.txt', "r",encoding='utf-8').read().splitlines()
for line in f:
    if sitename in line: #Site Password combination gets printed
        print("Your site and password combination is: " + line)
