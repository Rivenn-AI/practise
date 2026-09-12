''' Functions
(1) Define and call
(2) Parametr va argument
(3) Keyword va default arguments
(4) scope
'''
print("====Define <Parametr> and Call <Argument>")
# build in function > print() type()
# Function - reuseable block of code
# Instead of block { } in Java, Python uses Indentation


# define
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"hi {b}"


# Call - execute
result1 = greet("Martin")
print("result1:", result1)

result2 = greeting("Justin")
print("result2", result2)

print("======Keyword and default arguments")

# define


def give_great(name, age=22):
    print("give_great is executed")
    return f"Hi {name} your age {age} years old"


# call >> keyboard arguments
result3 = give_great(name="Justin", age=20)
print("result3", result3)

result4 = give_great(name="Justin")
print("result3", result4)


print("====Scopelar=====")

b = 100

# define


def calculate(a):
    c = a*b
    print(f"the value of c; {c}")


# call
calculate(5)
