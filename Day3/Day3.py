# #Love Calculator
# def count_calculator(name):
#     my_dic = {}
#     for i in name:
#         if i in my_dic:
#             my_dic[i]+=1
#         else:
#             my_dic[i]=1
#
#     return my_dic
#
#
#
# print("Enter your name")
# name = input()
# print("Enter your partner's name")
# partnet = input()
#
# print(count_calculator(name))

print("Welcome to Treasure Island. Your mission is to find the treasure")
print("Choose which way you want to go. Left or Right?")
direction = input().title()

if direction == 'Left':
    print("Would you like to wait or swim")
    action = input().title()
    if action == "Wait":
        print("Choose the door")
        door = input().title()
        match door:
            case "Red":
                print("Game over")
            case "Blue":
                print("Game Over")
            case "Yellow":
                print("You win")
    else:
        print("Game Over")
else:
    print("Game Over")




