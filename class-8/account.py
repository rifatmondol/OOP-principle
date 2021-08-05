from customerImpl import CustomerImpl

class Account(CustomerImpl):
    def __init__(self, name, phone, email, address, deposite, balance, withdraw):
        super(Account, self).__init__(name=name, phone=phone, email=email, address=address)
        self.__deposite = deposite
        self.__balance = balance
        self.__withdraw = withdraw

    def get_deposite(self):
        return self.__deposite

    def get_balance(self):
        ammount = self.__deposite + self.__balance
        return ammount


    def get_withdraw(self):
        total = self.__balance + self.__deposite - self.__withdraw
        return  total