print("welcome to the rollercoaster !")
height= int(input("what is your height in cm?"))
bill=0
if height>=120:
    print("you can ride the rollercoaster!")
    age=int(input("what is your age?"))
    if age<=12:
        bill=5
        print("child tickets are $5.")
    elif age<=18:
        bill=7
        print("youth tickets are $7.")
    else:
        bill=12
        print("adults tickets are $12.")
    wants_photos=input("do you want to have a phototake?type y for yes and n for no.")
    if wants_photos=="y":
        bill+=3
    print(f"your final bill is {bill}")
else:
    print("sorry you have to grow taller to ride the rollercostaer!")
