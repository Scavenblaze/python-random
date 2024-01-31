import random

filepath = 'words.txt'

def getword():
    #choose random word from file 
    with open(filepath, 'r') as file:       #with is used for file (also autocloses file when done), open opens(filepath, in read mode) as file
        wordchecker=[word.strip() for word in file.readlines()]
        currword=list(random.choice(wordchecker)) #random word is chosen
        return currword, wordchecker
        
        
#wordle logic
def check(currword, wordchecker):
    guess_common=[]
    
    
    while(True):
        guess1=(input("Enter your guess (5 lettered word) or type 'no' to exit: ").lower())
        guess=list(guess1)
        if guess1=='no':
            exit()
        elif(len(guess1)<5 or len(guess1)>5):
            print("ay man don't make ur life hard, just enter a 5 letter word")
        elif(guess1 not in wordchecker):
            print("what is this man, don't make up your own words. ")
        elif(len(guess1)==5):
            break
    
   
    #Checks common letters
    matched=set()
    for i in range(len(currword)):
        if i in matched:
            guess_common.append(currword[i])
        elif currword[i]==guess[i]:
            guess_common.append(currword[i])
            matched.add(i)
        elif currword[i] in guess and currword not in guess_common:
            guess_common.append('1')
        else: guess_common.append('_')
    print(guess)
    print(guess_common)
    return guess_common

#main
def main():
    i=0
    print("---------\n5 letter word\n_ means not a correct letter\n1 means letter is correct but not at the right position\n'letter' means correct position")
    currword, wordchecker = getword()
    guess_common=[]
    while(guess_common!=currword and i<6):
        guess_common = check(currword, wordchecker)
        i+=1
        print("guesses left ", 6-i)
    print(currword)
    if(guess_common==currword): print("yaay u won congrats!!")
    x=input("Play again? yes?: ").lower()
    if x=='yes':
        main()
    else: exit()
    
main()

