# OBJECT
# 1.__init__ method :- is special method used to iniitialize the object



# 2. Self is a reference to the current instance of a class

# 3. In the "objects" and "Classes",self is used within __init__ method to refer to the instance being created.

# Creating an Object
# class Dog:
#     def __init__(self,name):
#         self.name = name 
# dog1 = Dog("Buddy")
# print(dog1.name)

# Classes in python are like blueprints for creating objects.
# 1.
# class car:
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model
# # Creating objects from the class
# car1 = car("Toyota","Camry")
# car2 = car("Honda","Civic")
# print(car1.make,car1.model)
# print(car2.make,car2.model)

#ENCAPSULATION
# 2.
class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number
        self.__balance = balance
    def get_balance(self):
        return self.__balance
account1 = BankAccount("12345",1000)
print(account1._account_number)
print(account1.get_balance())

#INHERITANCE
# Inheritance allows you to create new classes that inherit propertes and methods from existing classes.
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name,dog.speak())
print(cat.name,cat.speak())
