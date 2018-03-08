print("=====================")
print("###### Hangman ######")
print("=====================")

from random import choice
import os
import re
d=open("tmdb_5000_movies.csv",'r')

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

data=d.read()
rows = data.split('\n')
rows = rows[1:len(rows)]
wins,Total = 0,0
print("{} wins out of {} tries. press enter to start a new game.".format(wins,Total))
usedLetters = []
# os.system('cls')
A = choice(rows).lower() #choose a random voc and replace all the letters with lowercase
while(hasNumbers(A)): #ignore all vocs with digits
    A = choice(rows).lower()
A = A.replace(",","") #remove all ,
A = A.replace(";","") #remove all ;
A = A.replace("-"," ") #replace all - with space
A = A.replace("."," ") #replace all - with space
A = A.replace("\"","") #remove all "
A = A.replace("&","and") #replace all & with and
if ":" in A: #ignore : and everything after it
    ASplit = A.split(":")
    A = ASplit[0]
if "harry potter" in A: #ignore all parts of this movie and stick with just harry potter :D
    A = "harry potter"

out = A

for i in A:
    if i != " ":
        out = out.replace(i,"-") #initial out as A with replaced characters by -
print(out)

while True:
    try:
        if out == A: #announce if the player wins
            print("You Won.\n")
            break
        print("to exit the game enter 1 or press Ctrl+C:\n")

        B = input("Choose a letter from alphabet:   ").lower() #get a letter

        if B=="1":
            print("Thank you for playing this game! have fun.\n")
            break

        while(B in usedLetters or len(B)>1 or str(B).isdigit() or str(B).isspace()): #ignore used letters and digits and spaces and let the player choose just one letter at a time
            B = input("Choose a valid letter from alphabet:   ").lower()
        usedLetters.append(B)
        indexOfChar = [m.start() for m in re.finditer(B,A)] #make a list of indexes of given letter in string
        if indexOfChar==[]: #if the given letter is not in the string increase total by 1
            Total+=1
        else: #if the given letter is in the string do as follow
            outList = list(out) #make "out" a list
            for j in indexOfChar: #for each of the letter in the string remove - and place the letter
                outList[j]=B
                out = ''.join(outList) #join the "out" list to create a string again
        print(out)
        if Total==1:
            print("O")
        if Total==2:
            print("O")
            print("^")
        if Total==3:
            print("O")
            print("^")
            print("|")
        if Total==4:
            print("O")
            print("^")
            print("|")
            print("^")
            print("You Lost.\n")
            break
    except ValueError: print("Incorrect input. try again")
    except KeyboardInterrupt:
        print("Thank you for playing this game! have fun.\n")
        break
