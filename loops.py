'''LOOPS
  (1) for
  (2) break/else
  (3) while
'''
print("=====For=====")
# Iterable objects >String dict tuple list range map filter
# ketma ketlik aniq

text = "MIT"
numbs = [10, 5, 7, 3]
car_obj = dict(brand="Toyota", year=2025)
range_obj = range(5)

for letter in text:
    print(f"letter id:{letter}")

print("-----")
for number in numbs:
    print(f"the number:", {number})

print("----")

for x in range_obj:
    print(f"the element", {x})

for key in car_obj:
    print(f"the key:{key}=> value: {car_obj.get(key)}")

for x in range(1, 29, 5):
    print(f"the x {x}")

print("=====Breake/else=====")

for x in range(1, 20, 5):
    print(f"the x {x}")
    if x > 10:
        print("Reached break", )
        break
else:
    print("Succeded Loop")

print("=====While=====")
numb = 40
while numb > 0:
    numb -= 10
    print(f"the number is {numb}")

print("----")  # while loopda aniq bulmagan qadam niu topishda ishlatiladi
count = 0
while True:
    count += 1
    x = int(input("find number"))

    if x == 41:
        print(f"you found number in {count} steps")
        break
    else:
        print("please try again")
