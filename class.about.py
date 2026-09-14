'''CLASS
   (1) what is class
   (2)ordinary va static properties
   (3)special methods / magic methods
'''
print("=====What is class")
# classlar - blueprint for creation
# classlar tarkibiy strukturalari State | constructor | method
# bitta shablon yasaladi va boshqa objectlar bn ishlata olamiz


class Person():  # Bu oddiy state
    # state
    message = "class state property"
    # constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method

    def introduce(self):
        print(f"Hi my name is {self.name} i am {self.age}")

    def say_age(self):
        print(f"my age is {self.age}")

    @classmethod
    def explain(cls):
        print("static method connected")


person1 = Person("Riven", 22)
person2 = Person("Ali", 28)


# Ordinary state properties
name = person1.name
print(name)
# odatiy methods
person1.introduce()
person2.say_age()


print("=====static properties=====")
# static state
new_message = Person.message
print("new_message", new_message)
# ordinary method
Person.explain()

print("=====maxsus methodlar=====")
# Pyhtonning eng kup ishlatiladigan maxsus methodlar
# __init__ __new__ __str__ __call__ __qetiten__ __oq__ __len__


class Car():
    # state
    description = "This class rules about cars"

    # constructor
    def __new__(cls, *args):
        print("*__new__")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"This {self.name} started engine")

    def stop_engine(self):
        print(f"This {self.name} stopped engine")

    def __str__(self):
        return f"the car name: {self.name} was produced {self.year}"

    def __call__(self):
        print("Object called by function")
        return True


my_car = Car("BMW", 2002)
my_car.start_engine()
my_car.stop_engine()
your_car = Car("Toyota", 2040)
print(your_car)
response = your_car()
print(response)
