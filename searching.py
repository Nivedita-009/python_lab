shopping_list=["pasta","bread","rice","spam","pulses"]
item_to_find="pasta"
found_at= None
# for index in range(len(shopping_list)):
#     if shopping_list[index]==item_to_find:
#         found_at=index
#         break
if item_to_find in shopping_list:
    found_at=shopping_list.index(item_to_find)
print("item found at position {}".format(found_at))
