# Creating an empty dictionary
my_dict={}

#Creating a dictionary with key-value pairs
student = {
    "name" : "Alice",
    "age" : 25,
    "grade" : "A"
}
# Accesing dictionary values:
name = student["name"]
age = student["age"]
print(name)
print(age)

# Modifying Dictionary Values:
# Modifying a value
student["age"] = 27

#Adding a new key-value pair:
student["city"] = "Bharatpur"


# Iterating through a dictionary:
for key,value in student.items():
    print(f"{key} : {value}")
for key in student.keys():
    print(f"{key}")
for value in student.values():
    print(f"{value}")

# Squares
squares = {num: num**2 for num in range(1,6)}
print(squares)

# delete
del student["grade"]
print(student)

# del student["phone"]
# If I don't want error then
del student.get["phone"]
print(student)
