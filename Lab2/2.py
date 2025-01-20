person = {
    "name": "Sujal",
    "age": 21,
    "city": "Kathmandu"
}

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

person["email"] = "sujal.106865@stu.upes.ac.in"
print("Updated dictionary with email: ", person)

person["age"] = 20
print("Updated dictionary with modified age: ", person)

if "city" in person:
    print("Key 'city' exists in the dictionary")

keys = person.keys()
values = person.values()

print("Keys:", list(keys))
print("Values:", list(values))
