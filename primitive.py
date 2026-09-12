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
