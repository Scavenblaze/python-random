import random

suits=["Spades", "Diamonds", "Hearts", "Clubs"]
cards=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
player=0
dealer=0

def cal_card(card):
    if(card in ['K', 'Q', 'J']):
        return 10
    elif(card=='A'):
        return 1
    else:
        return card
    

#player's first 2 cards
def pinitdraw():
    global player
    pinitialdraw1a=random.choice(suits)
    pinitialdraw1b=random.choice(cards)
    pinitialdraw1=(pinitialdraw1a,pinitialdraw1b)
    pinitialdraw2a=random.choice(suits)
    pinitialdraw2b=random.choice(cards)
    pinitialdraw2=(pinitialdraw2a,pinitialdraw2b)
    print("Player's cards are:", pinitialdraw1, pinitialdraw2)
    player+=cal_card(pinitialdraw1[1])
    player+=cal_card(pinitialdraw2[1])
    print("Player is: ",player)
    


#dealer's first 2 cards
def dinitdraw():
    global dealer
    dinitialdraw1a=random.choice(suits)
    dinitialdraw1b=random.choice(cards)
    dinitialdraw1=(dinitialdraw1a,dinitialdraw1b)
    #dinitialdraw2a=random.choice(suits)
    #dinitialdraw2b=random.choice(cards)
    #dinitialdraw2=(dinitialdraw2a,dinitialdraw2b)
    print("dealer's visible card is:", dinitialdraw1)
    dealer+=cal_card(dinitialdraw1[1])
    print("Dealer is: ", dealer)


#logic
def hit():
    global player
    pdraw1=random.choice(suits)
    pdraw2=random.choice(cards)
    pdraw=(pdraw1,pdraw2)
    print(pdraw)
    player+=cal_card(pdraw[1])
    print("player is ",player)
    
def dealerhit():
    global dealer
    while(True):
        if(dealer<player):
            ddraw1=random.choice(suits)
            ddraw2=random.choice(cards)
            ddraw=(ddraw1,ddraw2)
            print(ddraw)
            dealer+=cal_card(ddraw[1])
            print("dealer is ",dealer)
        elif(dealer>21):
            print("You win, dealer loses")
            break
        elif(dealer>player):
            print("You lose, dealer wins")
            break
        elif(dealer==21):
            print("You lose, Dealer wins")
            break
        elif(dealer==player):
            print("Push aka draw")
            break



#output
def main():
    pinitdraw()
    dinitdraw()
    while(True):
        ch=int(input("Enter your move: 1) Hit\n 2) Stand \n"))
        if(ch==1):
            hit()
            if(player==21):
                print("you win")
                break
            elif(player>21):
                print("you lose")
                break
        elif(ch==2):
            print("okay standing... Dealer will play now.")
            dealerhit()
            break
        else: print("i said 1 or 2")



while(True):
    chh=input("play?\n 1) yes\n2) no\n").lower()
    if(chh=='yes'):
        player=0
        dealer=0
        main()
    elif(chh=='no'):
        break
    else:
        print("yes or no dumbass")
        
        
#no split or double or insure cuz i still didn't understand split and insure
#and there is no betting for double.