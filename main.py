

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


names = ['maks derevencha', 'mike folk', 'jayden rodriquez']

for tempVariable in names:
    #email = first + . + last + @company.com
    # maks.derevencha@company.com
    splitNames = tempVariable.split(" ") # ['maks', 'derevencha']
    email = splitNames[0] + '.' + splitNames[1] + "@company.com"
    print(email)















