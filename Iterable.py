print("====Iterable Objects & Range======")
# Iterable objects >String dict tuple list range map filter


# ------Range-----
range_obj = range(3)
print("Range qiymat", range_obj)
# ------- string----
text = "MIT-A9"
for letter in text:
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")


print("=====Dictionary====")
# Dictioanry is JSON object;
person = {"name": "Ali", "age": 22, "single": True}
person_obj = dict(name="Riven", age=25, single=True)

print(f"the person:{person}")
print(f"the person_obj{person_obj}")

name = person_obj["name"]
print("name:", name)

# name = person_obj["hobby"]
# print("nmae", name)
name = person_obj.get("name")
hobby = person_obj.get("hobby", )
balance = person_obj.get("balance", 0)
print(f"the name:{name} hobby {hobby} and balnce is {balance}")


del person_obj["single"]  # del bu biz xoxlamagan stateni uchrish uchun
for key in person_obj:
    print(f"key:{key} value=> {person_obj[key]}")


print("====error hendiling=====")
car_dict = dict(name="Toyota", year=2026, electr=True)

try:
    print("Passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("Result", result)
except KeyError as err:  # xatolikning boshqa turlari ham bor
    print("No origin found", err)
except AttributeError as err:  # xatolikning boshqa turlari ham bor
    print("No speed found", err)
else:
    print("Logic is working without errors")
finally:
    print("Everything is done ")
