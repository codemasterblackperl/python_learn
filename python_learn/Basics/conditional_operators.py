
num=284
alwaysRun=True

while alwaysRun:
    guess=input("Enter a number:\t")
    if(guess=='quit'):
        break
    elif len(guess)<3:
        print("Enter the number again")
        continue
    guessNumber=int(guess)
    if(guessNumber==num):
        #this is a block
        print("you have guessed correctly")
        print("very good")
        alwaysRun=False
        #end of block
    else:
        for i in range(1,5):
            print("Wrong guess sorry try again")
        for i in 'best of luck':
            print(i)
        print("\n")
