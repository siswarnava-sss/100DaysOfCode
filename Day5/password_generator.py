import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','#','$','%','&','*','(',')','+']
numbers = [x for x in range(0,10)]

passwd_matrix = []

length_letter = int(input("Number of letter"))
length_number = int(input("Number of number"))
length_symbol = int(input("Number of symbol"))

for i in range(1,length_letter+1):
    passwd_matrix.append(random.choice(letters))
for i in range(1,length_symbol+1):
    passwd_matrix.append(random.choice(symbols))
for i in range(1,length_number+1):
    passwd_matrix.append(random.choice(numbers))
random.shuffle(passwd_matrix)
res = ""
for i in passwd_matrix:
    res+=str(i)
print(res)
