print("===========")
# Variable uzi nima In Java it is name of storage location
# In Python, variable bu reference nomlanshi refrence esa name of storage location
count = 100
count_type = type(count)
# print("count", count, count_type)
print(f"the count: {count} and type: {count_type}")
result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("=====string====")
# Methods>>  upper() lower() title() find() replace()

course = "Ai Pyhton Fullstack"
result = type(course)
print(f"the type of course: {result}")
result = course.title()
print(f"the result (1): {result}")

result = course.upper()
print(f"the result(2): {result}")

result = course.title()
print(f"the result(3): {result}")

result = course.replace("Fullstack", "Masterclass")
print(f"the result(4): {result}")

print("======Boolean=====")
# function >> type() input() bool() int() str()
# y = input("Give your value for y:")
# print("y:", y)


# result = y.isnumeric()
# print(f"the input in numeric: {result}")

# Truthy vs Falsy value
# Truthy > true 100 -100 "MIT"
# False > false 0 "" None

test_falsy = "" or False or None or 0 or 100
print("the falsy:", bool(test_falsy))

test_truthy = "MIT"
print("the falsy:", bool(test_truthy))
