class Animal:
    def __init__(self, location : str):
        self.location = location
        
    def walk(self):
        print(f"The animal is walking through {self.location}")
        
        
class Dog(Animal):
    def __init__(self, location : str) -> None:
        super().__init__(location)
        
    def bark(self):
        print("The dog is barking")
        self.walk()


class Cat(Animal):
    def __init__(self, location):
        super().__init__(location)
        
    def meow(self):
        print("The cat is meowing")
        
        
dog = Dog("Brasil")
dog.bark()

cat = Cat("Canada")
cat.meow()