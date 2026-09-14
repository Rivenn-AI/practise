# Objectlarni urganimiz
''' Objects
  --Objectlar uzi nima
  --iterable objectlar & range
  -- Dictionary
  -- Error handiling
'''


import array  # pyhton package /modul. biz bularni import qilshimiz shart bulgan python package hiasoblanadi
# import math  # bu package ichda uzning define bor biz bemlol call qilib va unga method berib keta olamiz
import math  # from math import ceil  bu anniq qilib chaqrib olish usuli
print("====what is Object=====")
# an object has state and method properties
# Everthing is object in Python

print(type("Hello world"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

'''Object orented programmming
  - Abstruction, Incepsilation, Polimorphism, inheritence
- Functional programmming
'''
result1 = math.ceil(43.7)  # math objectini Call qilyapmiz --ceil-- bu method
print("Bizni natija", result1)
