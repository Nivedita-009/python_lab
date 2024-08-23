#boolean expresions
day="Monday"
temperature=30
raining=True
if day=="saturday" and temperature>27 and not raining:
    print("go swimming")
else:
    print("learn python")
    #truthy values
name=input("what is your name?")
if name:
    print("hello,{}".format(name))
else:
    print("dont you have your name:)")
