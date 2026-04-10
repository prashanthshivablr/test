
# print("hello world")
# print("this is my second commit")



class Dog:
    species = "Canis familiaris"
    name = "Rex"
    age = 3

dog = Dog()
print(dog.name)
print(dog.age)
print(dog.species)

def bark(name):
    return f"{name} says: woof!"

def describe(name, age):
    return f"{name} is {age} years old."

print(bark("Rex"))
print(describe("Rex", 3))