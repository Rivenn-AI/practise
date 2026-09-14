'''CLASS
   (1) what is class
   (2)ordinary va static properties
   (3)special methods
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
