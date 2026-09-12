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
