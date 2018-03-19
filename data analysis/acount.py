class Acount(object):
    """
    Acount of the bank
    """
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    #获取名称
    def get_name(self):
        return self.__name.title()

    #获取余额
    def get_balance(self):
        return self.__balance

    #存款
    def save_money(self, num):
        self.__balance += num

    #取款
    def take_money(self, num):
        self.__balance -= num

    #设置余额
    def set_balance(self, num):
        self.__balance = num

    #转账
    def transfer(self, name, amount):
        self.__balance -= amount
        name.__balance += amount

class CreditAcount(Acount):
    """
    Credit Acount
    子类调用父类的属性、方法
    """

    #信用额度和透支额度为必须的
    def __init__(self, name, balance, quota):
        super().__init__(name, balance)
        self.__quota = quota
        self.__overdraft = self.__quota
    """
    #重写取钱方法一  parent_cladd.mothed(self, arg)
    def take_money(self, num):
        if num <= Acount.get_balance(self):
            Acount.take_money(self, num)
        elif num <= Acount.get_balance(self) + self.__overdraft:
            self.__overdraft = self.__overdraft + Acount.get_balance(self) - num
            Acount.take_money(self, Acount.get_balance(self))
        else:
            print("Sorry! The operation has failed!")
    
    #重写取钱方法二  super().mothed(arg)
    def take_money(self, num):
        if num <= super().get_balance():
            super().take_money(num)
        elif num < super().get_balance() + self.__overdraft:
            self.__overdraft = super().get_balance() + self.__overdraft - num
            super().take_money(super().get_balance())
        else:
            print("Sorry! The operation has failed!")
    """

    #重写取钱方法三   super(CreditAcount, self).mothed(arg)
    def take_money(self, num):
        if num <= super(CreditAcount, self).get_balance():
            super(CreditAcount, self).take_money(num)
        elif num < super(CreditAcount, self).get_balance() + self.__overdraft:
            self.__overdraft = super(CreditAcount, self).get_balance() + self.__overdraft - num
            super(CreditAcount, self).take_money(super(CreditAcount, self).get_balance())
        else:
            print("Sorry! The operation has failed!")

    #得到剩余透支额
    def  get_balance_overdraft(self):
        return self.__overdraft

"""
sam = Acount('Sam', 1000)
john = Acount('John', 3000)
john.transfer(sam, 1000)
print("The %s's banlance is $%d." % (sam.get_name(), sam.get_balance()))
print("The %s's banlance is $%d." % (john.get_name(), john.get_balance()))
"""

sam = CreditAcount('Sam', 1000, 1000)
sam.take_money(700)
print(sam.get_balance())                      #300
print(sam.get_balance_overdraft())            #1000

sam.take_money(800)
print(sam.get_balance())                      #0
print(sam.get_balance_overdraft())            #500

sam.take_money(800)                           #Sorry!
