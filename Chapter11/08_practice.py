class animal:
    pass

class pets(animal):
    pass

class Dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()
