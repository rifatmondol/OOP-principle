from customer import Customer

class CustomerImpl(Customer):
    def __init__(self, name, phone, email, address):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address

    def get_customer_name(self):
        return self.__name
    def set_customer_name(self, name):
        self.__name = name

    def get_customer_phone(self):
        return self.__phone
    def set_customer_phone(self, phone):
        self.__phone = phone

    def get_customer_email(self):
        return self.__email
    def set_customer_email(self, email):
        self.__email = email

    def get_customer_address(self):
        return self.__address
    def set_customer_address(self, address):
        self.__address = address

    def __str__(self):
        return self.__name + " " + self.__phone + " " + self.__email + " " + self.__address
