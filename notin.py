activity=input("what would you like to do today?")
if "cinema" not in activity.casefold():
    print("but i want to go to cinema")
 else:
   print("lets go for cinema then!")
name=input("what is your name?")
age=int(input("how old are you,{0}?".format(name)))
if age >= 18 and age <= 31:
    print("welcome to the holidays ;)")
else:
    print("sorry not applicable!!")
