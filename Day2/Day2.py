# # 1. Sum of digit
# # num = int(input())
# #
# # sum = 0
# # while(num):
# #     sum = sum + num%10
# #     num//=10
# # print(sum)
#
# # 2. BMI
# # print("Enter your height:")
# # height = float(input())
# # print("Enter your weight:")
# # weight = float(input())
# #
# # bmi = weight/(height ** 2)
# #
# # print("Your bmi is %f"%bmi)
#
# #3. Your life in Weeks
# age = int(input())
# maximum_day_left = 365*90 - age
# maximun_weeks_left = 52 * 90 - age
# maximun_years_left = 90 -age
# print(f"You have only {maximum_day_left},{maximun_weeks_left},{maximun_years_left} left. Live it.")

print("Welcome to the tip calculator")
print("What was the total bill?")
bill = float(input())
print("What percent will be the tip? 10, 12 or 15?")
tip = int(input())
print("How many people to split the bill?")
split = int(input())

each_person = round((bill + tip ) / split,2)
print(f"Each person should pay: {each_person}")