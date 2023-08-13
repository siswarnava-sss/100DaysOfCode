import random
# print(random.randint(-9,2))


# import random
# side=random.randint(0,1)
# if side == 0:
#     print("Head")
# else:
#     print("Tails")
names = input().split(", ")
rand_pos = random.randint(0,len(names)-1)

print(f"{names[rand_pos]} will pay the bill")





