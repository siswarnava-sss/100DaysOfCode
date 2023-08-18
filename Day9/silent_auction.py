new_dict = {}


i = 0
while i<5:
    name = input("Enter your name:\n")
    bid = int(input("Enter your bid:\n"))
    new_dict[name]=bid
    i+=1

print(new_dict)
print(max(new_dict.values()))
