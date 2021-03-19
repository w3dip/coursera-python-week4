class Value:
    def __set__(self, instance, value):
        self.value = value - instance.commission * value

    def __get__(self, instance, owner):
        return self.value

class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

# new_account = Account(0.1)
# new_account.amount = 100
#
# print(new_account.amount)
