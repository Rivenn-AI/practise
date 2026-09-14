'''Classlarni chuqur urganamiz
   (1) INCAPSULATION
   (3)INHERITENCE ----> father child 
   (3)POLIMORPHISM
'''

print("=====Inheritence=====")
# Parent >child
# Parent only provides only public and protectod properties states constructor and methodlarni olaoladi


class Animal():
    # state
    description = "Bu class parent for animal"
    # constructor

    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice
    # method

    def make_voice(self):
        print(f"Bu xayvon ovoz chiqara oladi: {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def inroduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def protect(self):
        print("Yes i can protect you ")

    def make_voice(self):
        print(f"Bu {self.name} can make this voice {self.voice}")


class Cat(Animal):
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def inroduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def inroduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def swim(self):
        print("Yes i can swim")


dog = Dog("Bobek", "wow wow", True)
cat = Cat("Tom", "Myooow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.inroduce()
cat.inroduce()
fish.inroduce()

print("-----")

dog.make_voice()
fish.make_voice()

print("----")
print(Animal.description)
print(Dog.description)
print(dog.voice)
print("status", dog.status)
print("status", cat.status)


print("=====POLIMORPHISM====")
# bir narsani bir necha xil shakilga ega bulshi
# agar child tarkibida chaqrilgan method bulsa ushani oladi agar yuq bulsa parent classdan oladi

print("-----")

dog.make_voice()
fish.make_voice()

print("----")
# fish> Fish >Animal> object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result ", {result})

# fish> Fish >Animal> object
data = issubclass(Fish, Animal)
data1 = issubclass(Animal, object)
print("data", data, data1)
