# Program to take user input, process it, and display the result.

name = input("Enter your name : ")
greet = (f"Hello {name} !")
print(greet)
yob = int(input("Enter your Year Of Birth: "))
age = 2025 - yob
print(f"Currently your age is : {age}")