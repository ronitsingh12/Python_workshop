#***********FUNCTIONS************
# function is reusable block of code and declared by def
# Scope of Variables
# Local scope---variables defined within a function are local to function and can only be accessed within that function
# Eg :-
# def my_function():
#     x = 10
#     print(x)
# my_function()

# def my_function():
#     x = int(input("Enter number :- "))
#     if(x%2==0):
#         print("even")
#     else:
#         print("odd")
# my_function()

#**************GLOBAL SCOPE EXAMPLE***********
# x =10
# def my_function():
#     print(x)

# my_function()

#**************NON LOCAL SCOPE*************
# x = 10
# def my_function():
#     global x
#     x = 20
#     print(x)
# my_function()


# GAME 1
# import random
# def guess_number():
#     return random.randint(1,100)
# target_number = guess_number()
# attempts = 0

# while True:
#     user_guess = int(input("Guess the number :- "))
#     attempts +=1
#     if user_guess == target_number:
#         print(f"Congratulations! You guessed the number in {attempts} attempts")
#         break
#     elif user_guess<target_number:
#         print("Try higher number")
#     else:
#         print("Try lower number")

# GAME 2
