import random

#words.txt path, pls change, still figuring it out
filepath = 'C:/Users/yashg/OneDrive/Desktop/codes/python dump/Wordle/words.txt'

def getword():
    global currword, wordchecker
    #choose random word from file 
    with open(filepath, 'r') as file:       #with is used for file (also autocloses file when done), open opens(filepath, in read mode) as file
        wordchecker=[word.strip() for word in file.readlines()]
        currword=random.choice(wordchecker)   #random word is chosen
        
        
#wordle logic
def check():
    global currword, guess, guess_common, wordchecker
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
    for i in range(len(currword)):
        if(currword[i]==guess[i]):
            guess_common.append(currword[i])
        elif(guess[i] in currword):
            guess_common.append('1')
        else: guess_common.append('_')
    print(guess)
    print(guess_common)

#main
def main():
    global guess_common,currword
    i=0
    print("---------\n5 letter word\n_ means not a correct letter\n1 means letter is correct but not at the right position\n'letter' means correct position")
    getword()
    guess_common=[]
    while(guess_common!=currword and i<5):
        check()
        i+=1
        print("guesses left ", 5-i)
    print(currword)
    if(guess_common==currword): print("yaay u won congrats!!")
    x=input("Play again? yes?: ").lower()
    if x=='yes':
        main()
    else: exit()
    
main()