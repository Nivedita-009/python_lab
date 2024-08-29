shopping_list=["pasta","bread","rice","spam","pulses"]
for item in shopping_list:
    if item=="spam":
        continue           #continue
    print("buy " + item)
    if item=="spam":
        break              #break
    print("buy " + item)
