'''import random
#random_side = random.randint(0,1)
if random_side == 1 :
    print("Heads")
else :
    print("Tails")'''

##Lists

# states_of_America = ["Delaware", "nepal", "india", "china"]
# states_of_America[1] = "Nepoli"
# print(states_of_America[1])
#
# states_of_America.append("USA")
# print(states_of_America[-1])
#
# print(states_of_America)

# Names = ["samir", "milan", "Anuj", "Pratik"]
# names = names_string.split(", ")
# import random
# names = ["samir" , "milan", "Anuj", "Pratik"]
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " is going to pay the bill today")


# #Final Project
# import random
# user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors.\n" ))
# computer_choice = random.randint(0,2)
# print(f"computer chooses {computer_choice}")
#
#
# if user_choose >=3 or user_choose<0:
#     print("Invalid Input ")
#
# elif user_choose == 0 and computer_choice == 1:
#     print("You Lose")
# elif user_choose == 1 and computer_choice == 2:
#     print("You win")
# elif user_choose ==2 and computer_choice == 0:
#     print("you lose")
# elif user_choose == 0 and computer_choice == 2:
#     print("You win")
# elif user_choose == computer_choice:
#     print("Draw")

#
# fruits = ["apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")
# print(fruits)

# student_scores = [20, 30, 40, 50, 56, 87, 45]
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is :{highest_score}")


#For loop in range
# for number in range(1,11,3):
#     print(number)
#
# total = 0
#
# for number in range(1,101):
#     total += number
#     print(total)


# target = int(input(" Enter the target number: "))
# even_sum = 0
# for number in range(0, target+1, 2):
#    even_sum += number
# print(even_sum)

#FizzBuzz Game

# target = 100
#
# for number in range(1,target + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizzbuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")


#Password Generator
import random
# uppercase_letters = [chr(i) for i in range(65, 91)]  # ASCII values for uppercase letters (A-Z)
# lowercase_letters = [chr(i) for i in range(97, 123)]  # ASCII values for lowercase letters (a-z)

# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the password generator")
# nr_letters = int(input("How many letters would you like in your password? \n"))
# nr_symbols = int(input(" HOw many symbols ? \n"))
# nr_numbers = int(input("How many numbers you want? \n"))

#Easy Level
# password = ""
# for char in range(1, nr_letters + 1):
#      password += random.choice(letters)
# for char in range(1, nr_letters + 1):
#      password += random.choice(symbols)
# for char in range(1, nr_letters + 1):
#      password += random.choice(numbers)
# print(password)


#Hard Level
# password_list = []
# for char in range(1, nr_letters + 1):
#      password_list.append(random.choice(letters))
# for char in range(1, nr_letters + 1):
#      password_list += random.choice(symbols)
# for char in range(1, nr_letters + 1):
#      password_list += random.choice(numbers)
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
# password = ""
# for char in password_list:
#      password += char
# print(f" Your pasword is : {password}")


#Day 6
#Defining and calling python functions

# def my_function():
#      print("Hello")
#      print("Bye")
# my_function()

#Indentation


# Letter Guessing Game



# import random
# word_list = ["adavark", "baboon", "camel"]
# choosen_word = random.choice(word_list)
# print(choosen_word)
# word_length = len(choosen_word)
# display = []
# for _ in choosen_word:
#      display+= "_"
# print(display)
#
# end_of_game = False
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     for position in range(word_length):
#         letter = choosen_word[position]
#        # print(f"Current positon: {position} \n Current letter: {letter} \n Guessed Letter:{guess}")
#         if letter == guess:
#             display[position] = letter
#     if guess not in choosen_word:
#          lives -= 1
#
# print(display)
# if "_" not in display:
#      end_of_game = True
#      print("You Win")


#Functions : Positonal vs Keyword Arguments

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in location {location}")
# greet_with("samir","Kathmandu")
# #
# greet_with("Kathmandu", "Samir") #positonal arguments
# greet_with(location= "kathmandu", name= "samir")
# import math
#
# wall_height = int(input("Enter the height : "))
# wall_width = int(input("Enter the width : "))
# coverage= 5
# def Paint_calc(height, width, cover):
#     total_cans = (wall_height * wall_width)/cover
#     round_up_cans = math.ceil(total_cans)
#     print(f"total number of cans : {round_up_cans}" )
# Paint_calc(height=wall_height, width=wall_width,cover=coverage)

#prime number checker

# Number = int(input("Enter the number to Check: "))
# def prime():
#     if Number % 1== 0 and Number % Number== 0 :
#         print("Prime")
#     else:
#         print(" Number is not Prime")
# prime()

#Caeser Cypher Encryption
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



# Day 9_ dictionaries {


# #nesting
#
# capitals = {
#     "France": "Paris",
#     "Germany": "berlin",
# }
# # nesting a list in dictionary
# travel_log = {
#     "france":  ["paris", "lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttagart"],
#  }
#
# # Nesting dictionary in dictionary
# travel_log = {
#     "france": {"cities_visited": ["paris", "lille", "Dijon"],"total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttagart"], "total_visits": 5},
#  }

#Nesting a dictionary in a list

# travel_log = [
#     {
#         "country": "france",
#         "cities_visited": ["paris", "lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttagart"],
#         "total_visits": 5
#     },
# ]
# def add_new_country(name,visits,list_of_cities):
#     new_country = {}
#     new_country["country"] = name
#     new_country["total_visits"] = visits
#     new_country["cities_visited"] = list_of_cities
#     travel_log.append(new_country)


# DAy 9 creating a bidding project
# Day 10
#creating a calculator
#Functions with output

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 != 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30,31,30, 31]
#     if month == 2 and is_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]
#
# year = int(input("Enter Year: "))
# month = int(input("Enter Month: "))
# days = days_in_month(year, month)
# print(days)

#docstring
""" inside docstirng we can write as long as you want to write"""

# Final project Calculator
# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1/n2
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }
# #recursion
# def calculator():
#     num1 = float(input("Enter the first number: "))
#     for symbol in operations:
#         print(symbol)
#     should_continue = True
#     while should_continue:
#         operation_symbol = input("Enter the symbol you want to perform: ")
#         num2 = float(input("Enter the next number: "))
#         # operation_symbol = input("Enter the symbol you want to perform: ")
#         calculation_funtion = operations[operation_symbol]
#         answer = calculation_funtion(num1, num2)

#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator ") == "y":
#             num1=answer
#         else:
#             should_continue = False
#             calculator()

# calculator()
#print vs return
