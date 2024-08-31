available_exits=["north","south","east","west"]

choosen_exit=""
while choosen_exit not in available_exits:
    choosen_exit=input("please choose a direction:")
    if choosen_exit=="quit":
        print("game over")
        break

print("arent you glad you got out of there")
