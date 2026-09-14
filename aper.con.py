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
