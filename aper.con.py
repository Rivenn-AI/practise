'''Operators and Conditions
  (1)Operators
  (2)Conditions
  (3)Logical Operators
'''

print("=====Operator====")

# +- <> <= >= * == / is // += **

a = 19
b = 5
result = a//b
left = a % b
print(f"the result {result} and left {left}")
# print("a>b", a > b)
# print("a*b", a*b)
# print("a/b", a/b)
# a = a+100
a += 100
print("a", a)
print("b**", b**2)
print("b**", b**3)

print("="*5)
# Pythonda faqat qiymatlar solishtirladi
c = dict(name="Riven", age=22)
d = dict(name="Ali", age=32)
e = c
print("c==d", c == d)
print(id(c), id(d), id(c))


print("c is d", c is d)
print("c is e", c is e)


print("=====Conditions====")

x = 15
if x > 50:
    print("case A")
elif x > 10:
    print("case B")
else:
    print("case C")
print("=====Logical Operators====")
# logical operators
age = 10
# person = None
# if age > 16:
#     person = "adult"
# else:
#     person = "child"

# print("person:", person)

# Ternery
person = "adult" if age > 18 else "minor"
print("person", person)

is_student = True
is_admin = False
is_guest = True
is_parent = True
if not is_student:  # not operator
    print("Student bulish xoxlayszmi")
elif is_admin:
    print("please go to this university ")
elif is_guest or is_parent:  # bittasi true olsa true olib ketadi. Agar and bulsa bitta xato bulsa false qaytaradi
    print("Witing is over there")
else:
    print("other cases")
