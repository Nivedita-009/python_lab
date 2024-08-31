low=1
high=1000

print("please think of a number between {} and {}".format(low,high))
input("press ENTER to start")

guesses=1
while True:
    print("\t guessing in the range of {} to {}".format(low,high))
    guess=low+(high-low)//2
    high_low=input("my guess is{}.should i guess higher or lower?Enter h or l,or c if my guess was correct ".format(guess)).casefold()

    if high_low=="h":
        #Guesses higher.the low end of the range becomes 1 greater than the guesses

        low= guess+1
    elif high_low=="l":
        #guesses lower.the high end of the range becomes 1 less than the guesses
        high= guess-1
    elif high_low=="c":
        print("i got it in {} guesses!".format(guesses))
        break
    else:
        print("please enter h, l or c ")
    guesses=guesses+1
