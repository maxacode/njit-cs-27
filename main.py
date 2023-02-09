

# # Account_1_username = "Maks"
# # Account_1_password = "HelloWorld"
 

# # asking_username = input("enter your username: ")
# # asking_password = input("Enter your password: ")

# # #  Whatever the user entered - The saved username
# # if asking_username == Account_1_username or asking_password == Account_1_password:
# #     print("Welcome to the Server as Admin")

# # else:
# #     print("Wrong username or password")





# # Step 1 Get integer input from the user
# int_from_user = int(input("Please enter your number grade: "))


# # step 2 Create an if-else statement Check the grade level
# # Print the relevant grade.

# if int_from_user > 110 or int_from_user < 0:
#     print("You number is to high! try again")

# elif int_from_user > 95:
#     print("A+")

# elif int_from_user > 90:
#     print("A-")

# elif int_from_user > 80:
#     print("B")

# elif int_from_user > 70:
#     print("C")

# else:
#     print("You Failed")





# For Loop example:


# names = ['maks beiber', 'britany spears', 'barbie doll']

# for tempVariable in names:
#     #email = first + . + last + @company.com
#     # maks.derevencha@company.com
#     splitNames = tempVariable.split(" ") # ['maks', 'derevencha']
#     email = splitNames[0] + '.' + splitNames[1] + "@company.com"
#     print(email)





# names = ['maks beiber', 'britany spears', 'barbie doll', 'joe dirt', 'mcgyver', 'james bond']

# #   start, end, stepby/counter/incriment 
# # range( 0, 10, 2)

# # empty list named peopleInvited
# peopleInvited = []
# for x in range(0, len(names),2):
#     peopleInvited.append(names[x])
#     print(peopleInvited)

# while len(peopleInvited) <= 3:
#     print(f'Here is an invitation to my party: {peopleInvited[0]}')
     



# names = ['maks beiber', 'britany spears', 'barbie doll', 'joe dirt', 'mcgyver', 'james bond']


# maxPeople = 5

# for x in names:
#     while maxPeople > 0:
#         maxPeople -= 1

#         print(f"You are invited to my party: {x}")




# Mixing conditions

# names = ['maks beiber', 'britany spears', 'barbie doll', 'joe dirt', 'mcgyver', 'james bond']

#   start, end, stepby/counter/incriment 
# range( 0, 10, 2)

# # empty list named peopleInvited
# peopleInvited = []
# for x in range(0, len(names),2):
#     if "maks" in names[x]:
#         print(f"YOu are not invited {names[x]}")
#         continue
        
#     print(f"Your invited to my party: {(names[x])}")

 

# infinite loop/controlled


# x = 1
# #x = 0, 1, 2,3,4,5
# while x > 0:
#     x += 1 
#     print(x)
#     input('press enter to continue')



















# Lesson 4 
# lab 1


# Request a number from a user, divide by zero and handle the errors

# if number.isnumeric():
#     print("this IS a number")
# else:
#     print("this is a string")
# if number == 0 or number2 == 0:
#     print("Cant divide by Zero")

# while True:
#     try:
#         number = int(input("Enter a number: "))
#         number2 = int(input("Enter another number: "))
#         print(number / number2 )
#         break
#     except ZeroDivisionError:
#         print("Can not divide by Zero")
#     except ValueError:
#         print("Please enter a number and not a LETTER!!!!")

# print("Other code here!")


# Lesson 2 
"""Lab Objective: Practice handling errors that may occur in the code."""

# product = 1
# for i in range(4): # 0, 1, 2, 3
#     while True:
#         try:
#             num = int(input("Enter a number: "))
#             product *= num
#             break
#         except:
#             print("The input is not a valid number")
# print("The product of the 4 numbers is: " + str(product))

#input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution




































