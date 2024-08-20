# name = input("please enter your name :")
# age = input("how old are you,{0}? ".format(name))
# print(age)
# if age >= 18:
#     print("you are old enough to vote")
# else:
#     print("please come back in {0} years".format(18-age))

answer=5

print("please guess number between 1 ans 10: ")
guess=int(input())
#
# if guess<answer:
#     print("please guess higher")
# elif guess>answer:
#     print("please guess lower")
# else:
#     print("you got it first time..")
if guess == answer:
    print("you got it first time")
else:
 if guess > answer:
    print("please guess lower")
 else:
    print("please guess higher")
guess = int(input())
if guess == answer:
    print("well done you guessed right !")
else:
    print("you have not guessed right !")
