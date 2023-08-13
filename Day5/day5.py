#
fruit = ["Apple", "Peach", "Pear"]
#
# for i in fruit:
#     print(i)

# student_heights = map(int, input().split())
# count=0
# sum=0
# for n in student_heights:
#     sum+=n
#     count+=1
# print(sum/count)
# scores = map(int, input().split())
# print(max(scores))
# import math
# max = -999
# for i in scores:
#     max = math.max(max,i)
#
# # print(max)
# num = [i for i in range(2,1,2)]
# sum = sum(num)
# print(sum)


for i in range(1,101):
    if i%3==0 and i%5!=0:
        print("Fizz")
    elif i%5==0 and i%3!=0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)
