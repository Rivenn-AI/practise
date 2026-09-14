'''Classlarni chuqur urganamiz
   (1) INCAPSULATION
   (3)INHERITENCE
   (3)POLIMORPHISM
'''
print("====== Incapsulation ========")

# Pyhton---> public, __private, _protectod


class Account():
    # state
    description = "Bizni Bank ishga tushdi"
    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount
    # method

    def get_balance(self):
        print(f"Your name is {self.__owner}, You have {self.__amount} usd")

    def deposite(self, amount):
        print("*Deposite ishga tushdi*", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("*Pul kamaydi*, ", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("Change ownership", new_owner)
        self.__owner = new_owner


my_account = Account("Riven", 100)
my_account.get_balance()

print("------")
my_account.deposite(4000)
my_account.withdraw(300)
my_account.get_balance()

# my_account.amount = 1000000
# my_account.owner = "Ali"
# my_account.get_balance()
# print(my_account.owner)

try:
    result = my_account.__amount
    print("result", result)
    pass
except Exception as err:
    print("No target state found", err)

# Getter va Setter @ bu dekoretor

# state getter va property decoretor orqali object ichdagi maxviy malumotlarni olib beradi

print("account-owner", my_account.holder)
my_account.holder = "Vali"
# my_account.change_ownership("ali")
# print("owner changed:", my_account.holder)
