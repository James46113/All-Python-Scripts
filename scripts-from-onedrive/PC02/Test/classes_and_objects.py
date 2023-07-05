# Create a 'Pet' class that contains these instance variables (private)
# - A name
# - An age
# - An owner
# And these functions (public)
# - (Override) A constructor that retrieves and stores values for all instance variables
# - Change the owner to someone else
# - Increase the age of the pet
# - (Override) Create a string that represents the Pet, in the following format "{Name}, {Age} Years Old, Owned By {Owner}"


# Create a list of Pets and ask the user to input the correct information for them
# Once made, output all the Pets, change their owner to another user's name, and output all the Pets again
# Age a random Pet and output all the Pets again
from random import choice


class Pet:
    def __init__(self, name, age, owner):
        self.__name = name
        self.__age = int(age)
        self.__owner = owner

    def change_owner(self, new_owner):
        self.__owner = new_owner

    def increase_age(self, by):
        self.__age += by

    def __str__(self):
        return f"{self.__name}, {self.__age} Years Old, Owned By {self.__owner}"


pets = [Pet(input("name of pet:"), input("age of pet: "), input("owner of pet")),
        Pet(input("name of pet:"), input("age of pet: "), input("owner of pet")),
        Pet(input("name of pet:"), input("age of pet: "), input("owner of pet"))]

print(f"{pets[0]},\n{pets[1]},\n{pets[2]}")

for pet in pets:
    pet.change_owner(input("new owner: "))

print(f"{pets[0]},\n{pets[1]},\n{pets[2]}")

choice(pets).increase_age(3)
print(f"{pets[0]},\n{pets[1]},\n{pets[2]}")
