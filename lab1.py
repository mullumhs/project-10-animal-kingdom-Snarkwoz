"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initialiser with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.

class Animal():
    def __init__ (self,species,age,diet,habitat):
        self.species = species
        self.age = age
        self.diet = diet
        self.habitat = habitat

    def eat(self):
        print(f"The {self.species} is eating")

    def sleep(self):
        print(f"The {self.species} is going to sleep. Night night!")

# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
# Give each of the derived classes at least one specific behavior. E.g. fly and swim.

class Octopus(Animal):
    def __init__(self,species,age,diet,habitat,arms):
        super().__init__(species,age,diet,habitat)
        self.arms = arms

    def swim(self):
        print(f"The {self.species} is swimming")

    def camoflage(self):
        (f"The {self.species} has camoflaged into the terrain")

class Snake(Animal):
    def __init__(self,species,age,diet,habitat,length):
        super().__init__(species,age,diet,habitat)
        self.length = length
    
    def hunt(self):
        print(f"The {self.species} is hunting")
    
# Create at least two instances of the Animal derived classes with different data.

octopus = Octopus("blue ring octopus","6 months","carnivore","reefs","8")
brown_snake = Snake("brown snake","2 years","carnivore","Australia","1.5m")

# Write code that prints out the details of each animal and calls their specific behaviors.

print(f"{octopus.species} is {octopus.age} old, is a {octopus.diet}, lives in {octopus.habitat} and has {octopus.arms} arms")
octopus.swim()
octopus.camoflage()
print(f"{brown_snake.species} is {brown_snake.age} old, is a {brown_snake.diet}, lives is {brown_snake.habitat} and is {brown_snake.length} long")
brown_snake.hunt()
