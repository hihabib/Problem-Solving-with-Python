# x = 10
# y = 100

# if x > y:
#     print("40 is greater than 100")
# else:
#     print("40 is not greater than 100")

'''Problem-1: Write a program in python to check whether a year is leap or not'''
# 4 dara vag jay and 100 dara vag jay = leap year na
# 4 dara vag jay + 100 dara jay na + 400 dara jay na = leap year
# 4 dara vag jay + 100 dara vag jay + 400 dara vag jay = leap year

# year = 1700
# if year % 4 == 0:
#     if year % 400 == 0:
#         print("Leap year")
#     else:
#         if year % 100 != 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
# else :
#     print("Not leap year")


'''Problem-2: Write a program in python to find largest among three number using nested if statement.'''

# x = 18
# y = 15
# z = 12

# if x > y:
#     if x > z:
#         print(x)
#     else:
#         print(z)
# else:
#     if y > z:
#         print(y)
#     else:
#         print(z)


'''5. Write a program in python to take input of 5 subject mark and take maximum number. Find total and calculate percent on the basis of percent provide grade like:
    
    Per > 80 “A+”
    Per > 65 and per <=80 “A” 
    Per > 50 and per <=65 “B”
    Per >= 42 and per <=50 “C”
    Per < 42 “Fail'''

# DRY -> Don't repeat yourself

# max = 100

# one = 80.5
# two = 30
# three = 40
# four = 35
# five = 25

# percent_in_one = (one * 100) / max
# percent_in_two = (two * 100) / max
# percent_in_three = (three * 100) / max
# percent_in_four = (four * 100) / max
# percent_in_five = (five * 100) / max


# print("Subject: One")
# if percent_in_one > 80:
#     print("A+")
# elif percent_in_one > 65 and percent_in_one <= 80:
#     print("A")
# elif percent_in_one > 50 and percent_in_one <= 65:
#     print("B")
# elif percent_in_one >= 62 and percent_in_one <= 50:
#     print("C")
# else:
#     print("Fail")


# print("Subject: Two")
# if percent_in_two > 80:
#     print("A+")
# elif percent_in_two > 65 and percent_in_two <= 80:
#     print("A")
# elif percent_in_two > 50 and percent_in_two <= 65:
#     print("B")
# elif percent_in_two >= 62 and percent_in_two <= 50:
#     print("C")
# else:
#     print("Fail")


# print("Subject: Three")
# if percent_in_three > 80:
#     print("A+")
# elif percent_in_three > 65 and percent_in_three <= 80:
#     print("A")
# elif percent_in_three > 50 and percent_in_three <= 65:
#     print("B")
# elif percent_in_three >= 62 and percent_in_three <= 50:
#     print("C")
# else:
#     print("Fail")

# print("Subject: Four")
# if percent_in_four > 80:
#     print("A+")
# elif percent_in_four > 65 and percent_in_four <= 80:
#     print("A")
# elif percent_in_four > 50 and percent_in_four <= 65:
#     print("B")
# elif percent_in_four >= 62 and percent_in_four <= 50:
#     print("C")
# else:
#     print("Fail")

# print("Subject: Five")
# if percent_in_five > 80:
#     print("A+")
# elif percent_in_five > 65 and percent_in_five <= 80:
#     print("A")
# elif percent_in_five > 50 and percent_in_five <= 65:
#     print("B")
# elif percent_in_five >= 62 and percent_in_five <= 50:
#     print("C")
# else:
#     print("Fail")
