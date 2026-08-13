class Dog:
    def __init__(self, name, breed):
        print("__init__ chal raha hai, self ka address:", id(self))
        self.name = name
        self.breed = breed

my_dog = Dog("brunno", "labra")
print("my_dog ka address:", id(my_dog))
my_dog2 = Dog("toffy", "labra")
print("my_dog ka address:", id(my_dog2))
