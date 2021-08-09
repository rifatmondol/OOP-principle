from customerImpl import CustomerImpl

class Account(CustomerImpl):
    def __init__(self, name, phone, email, address, balance, deposite, withdraw):
        super(Account, self).__init__(name=name, phone=phone, email=email, address=address)
        self.__balance = balance
        self.__deposite = deposite
        self.__withdraw = withdraw

    def get_balance(self):
        return self.__balance

    def get_deposite(self):
        ammount = self.__deposite + self.__balance
        self.__balance = ammount
        return "Deposite:", self.__deposite, "Balance:", self.__balance


    def get_withdraw(self):
        total = self.__balance - self.__withdraw
        return  "Withdraw:", self.__withdraw, "Present Balance:", total