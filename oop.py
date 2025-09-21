class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} the {self.species} says: {self.sound}")

    def move(self):
        print(f"{self.name} moves around.")

# Inheritance and Encapsulation: Dog is a kind of Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog", "Woof!")
        self.__breed = breed  # encapsulated attribute

    def get_breed(self):
        return self.__breed

    def move(self):
        print(f"{self.name} runs on four legs.")

# Polymorphism Challenge: Different classes, same interface
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

# Demonstration
if __name__ == "__main__":
    # Animals
    generic_animal = Animal("Leo", "Lion", "Roar")
    dog = Dog("Buddy", "Golden Retriever")

    generic_animal.make_sound()
    generic_animal.move()

    dog.make_sound()
    print(f"{dog.name} is a {dog.get_breed()}")
    dog.move()

    # Polymorphism in action
    movers = [Car(), Plane(), dog]
    for mover in movers:
        mover.move()
