# Create a list, access elements, modify elements, and perform list operations.

fruits = ["Apple", "Banana", "Cherry", "Date", "Orange"]
print("Accessing elements using indexing : ")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

fruits[1] = "Kiwies"
print(f"Modified list is: {fruits}")

fruits.append("Watermelon")
fruits.remove("Watermelon")
print(f"Modified list is: {fruits}")

length = len(fruits)
print(length)

fruits.sort()
print(f"Sorted fruits list is: {fruits}")
