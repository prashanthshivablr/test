class Bird:
    species = "peacock"
    name = "kuku"
    age = 9

bird = Bird()
print(bird.name)
print(bird.age)

def chirp(name):
    return f"{name} says: tweet!"

def describe(name, age):
    return f"{name} is {age} years old."

print(chirp("kuku"))
print(describe("kuku", 9))