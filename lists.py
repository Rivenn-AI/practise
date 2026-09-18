'''List
  (1) Working with list
  (2)List methods
  (3)Lambada function
  (4)enumarate, map and filter
'''

print("========Working with list=====")
# Java/PHP/Nodejs array => Python list

# Literal
person = {"name": "Justin", "age": 25}  # dictionary uslubi
people = ("Andrew", "John", "Michel")  # tuple

groups = ["MIT", "Flexy", "devex", "mg"]  # list
for tean in groups:
    print(f"the team {tean}")

# constructor
result = list("Hello world")
print(f"the letter: {result} and size: {len(result)}")

print("------")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]  # [0, 2) 2 index kirmaydi
c = fruits[::3]  # boshlang'ish qiymatni olib ber va 3 qadam sakra
d = fruits[::-1]  # teskari xolatda

print("a:", a)
print("b", b)
print("c", c)
print("c", d)

print("========list methods=====")
# method > append() insert() pop() remove() clear() sort() index() => muteable
letters = ["a", "b", "d"]

letters.append("c")  # oxridan qushadi Muteable
print(f" the append reult: {letters}")

letters.insert(0, "z")  # bu oldidan qushib beradi
print(f" the insert reult: {letters}")

size = len(letters) - 1
result = letters.pop(size)  # bu oxridan pop olib tashlash kabi
print(f"pop result: {result} and letters {letters}")

result1 = letters.pop(0)  # bu oldidan ajratib beradi
print(f" pop oldidan {result1} and letters {letters}")

print('---')

animals = ["dog", "cat", "capyvara", "fish", "lion"]
print("animals", animals)

animals.remove("lion")  # shu indexni uchrib yuboradi
print(f"Lion kette {animals}")

del animals[2:4]  # faqat shu indexlarni olib beradi
print("animals deleted:", animals)

exist = animals.index("cat")  # bu index raqamni bilib beradi
print(exist)

animals.clear()  # bu list butunlay valuelarni tushrib yuboradi
print(animals)


if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat is not in the list")

print("------")
numbers = [2, 30, 12, 8, 57]
numbers.sort()  # list ichni tartiblaydi
print("numbers", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable sorted
numbs = [2, 50, 48, 300]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new one {new_numbs}")

print("========Lambada function=====")
# Labda bu kichik annonymous functionlar xisoblanadi


def calculate(x, y):
    return x*y


result = calculate(3, 5)
print("result", result)

people = [
    ("robert", 29),
    ("ali", 33),
    ("riven", 22),
    ("Michel", 12),
]
people.sort()
print("people1", people)
# sort by age via labda
people.sort(key=lambda person: person[1])
print("people2:", people)  # bu yoshi buycha tartiblab beradi

print("========enumerate, map and filter=====")
# enumerate for index & value
animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print("enimertaded", element)

for (index, value) in enumerate(animals):
    print(f"the index {index}. va qiymat {value}")

# similar in dictioanry
car_obj = dict(brand="ferrari", year=3000)
result = car_obj.items()
print("result", result)
for (key, value) in result:
    print(f"the key {key}. va qiymat {value}")

print("------")
cars = [
    ("ferrari", 49),
    ('Bmw', 44),
    ('Audi', 116),
    ("tayota", 34),
    ("chevralet", 400),
]
# new_cars = []
# for car in cars:
#     new_cars.append(car[0])
# print(new_cars)

result1 = map(lambda car: car[0], cars)
print(f"the result1{result1}  and type: {type(result1)}")

new_cars = list(result1)
print(new_cars)

print("----")
# filter uzning functionga ega
result_filter = filter(lambda car: car[1] > 40, cars)
print(f"the result1{result_filter}  and type: {type(result_filter)}")
print(list(result_filter))
