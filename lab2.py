"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the Animal Kingdom program from Lab 1 to include polymorphism,
               demonstrating method overriding in derived classes.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Paste your base class Animal and the derived classes from Lab 1 here.

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
        (f"The {self.species} has camoflaged into the terrain")

    def look_for_mate(self):
        print(f"The {self.species} is looking for love!")        

class Snake(Animal):
    def __init__(self,species,age,diet,habitat,length):
        super().__init__(species,age,diet,habitat)
        self.length = length
    
    def hunt(self):
        print(f"The {self.species} is hunting")

    def look_for_mate(self):
        print(f"The {self.species} is looking for love!")

# Modify the classes to demonstrate polymorphism through method overriding.
# Each derived class should override at least one method from the Animal class.
# For instance, you might want to override a 'make_sound' method to reflect the specific sound each animal makes.

# Create at least two instances of your derived classes

octopus = Octopus("blue ring octopus","6 months","carnivore","reefs","8")
brown_snake = Snake("brown snake","2 years","carnivore","Australia","1.5m")

# Call the overridden methods on the instances.

octopus.look_for_mate()
brown_snake.look_for_mate()
