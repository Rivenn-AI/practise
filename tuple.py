'''Tuple
   (1) what is tuple: type vs list
   (2)Unpacking arguments
   (3)zip
'''
print("========What is tuple: type vs list=====")
# Java/PHP NodeJS array => Python List,


# Literal
numbs = [3, 6, 4, 7, 8]
print(numbs)
# car_dic = {"brand": "Ferare", "year": 1990}
# constructor function
letter = list("Hello world")
# print(letter)
# person_dict = dict(name="Riven", age=34)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits", fruits)
# qiymatlarni uzgartira olmaslik uchun tuple kerak => ()
fruits[2] = "melon"
print("before fruits", fruits)

animals = ("'dog'", "cat", "lion")
table_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"

# try avoid this
# people = "Andreww" ,"john"
# animals = "dog",


print("========Arguments unpacking=====")  # tuple orqali argumentlarni yoyamiz
groups = ["Mit", "Flex", "Devex", "MG"]
(x, y, *z) = groups
print(f"Xning qiymati {x}, y qiymati {y}")
print("z teng", z)

# *args > tuple
# bu argumentlarni sonni bilmaganimizda yoyish orqali kurish.


def calculate(*args):
    print("*args>", args)
    total = 1
    for x in args:
        total *= x
    print(f"the typeargs value{type(args)}")
    print(f"the total value:{total}")
    return total


# call
calculate(1, 7, 2, 3)
print("---")
calculate(0, 3, 400)
print("---")
calculate(5, 7)

# **kwargs bu argumentlarning kurnishi dictionary orqali xosil buladi


def introduce(**kwargs):
    print(f"the type: (**kwargs) value: {type(kwargs)}")
    print(f"Hi  i {kwargs["name"]} and i am {kwargs["age"]} years old")
    pass


# Call
introduce(name="Riven", age=25)
introduce(name="shawn", age=34, single=True)


def greeting(*args, ** kwargs):
    print("*arg>", args)
    print("**kwargs", kwargs)


# Call
greeting("hi", True, 10, name="John", age=19)
