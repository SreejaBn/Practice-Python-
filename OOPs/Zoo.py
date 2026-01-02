class Animal:
    def __init__(self, species, age):
        self.species= species
        self.age= age

    def __str__ (self):
        return f"Animal: {self.species}\nAge: {self.age}"
    
class Zoo:
    def __init__ (self):
        self.animals= []

    def add_animal(self, animal_instance):
        self.animals.append(animal_instance)

    def count_animals(self):
        return len(self.animals)
    
    def find_oldest(self):
        oldest= self.animals[0]
        for a in self.animals:
            if oldest.age<= a.age:
                oldest= a
        return oldest
            
a1 = Animal("Lion", 5)
a2 = Animal("Elephant", 12)
a3 = Animal("Monkey", 2)

my_zoo = Zoo()
my_zoo.add_animal(a1)
my_zoo.add_animal(a2)
my_zoo.add_animal(a3)

print(f"Total animals: {my_zoo.count_animals()}")
print(f"Oldest species: {my_zoo.find_oldest()}")
