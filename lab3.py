"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Build a Zoo class to manage a collection of animals from the Animal 
               Kingdom program. Demonstrate managing objects and class interactions.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Import your base class Animal and any derived classes (e.g., Bird, Fish) here from Lab 2.

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

    def look_for_mate(self):
        print(f"The {self.species} is looking for love")

class Octopus(Animal):
    def __init__(self,species,age,diet,habitat,arms):
        super().__init__(species,age,diet,habitat)
        self.arms = arms

    def swim(self):
        print(f"The {self.species} is swimming")

    def camoflage(self):
        print(f"The {self.species} has camoflaged into the terrain")

    def look_for_mate(self):
        print(f"The {self.species} is looking for love!")
    
    def display_info(self):
        print(f"{self.species} is {self.age} old, is a {self.diet}, lives in {self.habitat} and has {self.arms} arms.")

class Snake(Animal):
    def __init__(self,species,age,diet,habitat,length):
        super().__init__(species,age,diet,habitat)
        self.length = length
    
    def hunt(self):
        print(f"The {self.species} is hunting")

    def look_for_mate(self):
        print(f"The {self.species} is looking for love!")

    def display_info(self):
        print(f"{self.species} is {self.age} old, is a {self.diet}, lives in {self.habitat} and is {self.length} long.")

# Define the Zoo class that can manage multiple Animal objects. It should have the following two methods:
# __init__ - Initialises a new Zoo instance with an empty list to hold animal objects.
# add_animal - Adds an animal to the zoo's list and confirms addition with a return message.
# You should then think of and implement at least one additional method for the Zoo class. E.g. feed_all

class Zoo():
    def __init__(self):
        self.animals = []

    def add_animals(self,species):
        self.animals.append(species)
        return f"{self.species} has been added to the zoo"
    
    def feed_animals(self):
        for animal in self.animals:
            print(f"{animal.species} has been fed")
    
    def display_all_info(self):
        for animal in self.animals:
            print(animal.display_info())

# Create instances of derived Animal classes and add them to the Zoo.

octopus = Octopus("octopus","9 months","carnivore","reefs","8")
snake = Snake("green python","1 year","carnivore","Australia","2m")

# Demonstrate the Zoo's functionality by calling its methods.


Zoo.add_animals(octopus)
Zoo.add_animals(snake)
Zoo.feed_animals()
Zoo.display_all_info()
