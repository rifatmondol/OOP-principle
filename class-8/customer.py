from abc import ABC, abstractmethod

class Customer(ABC):

    @abstractmethod
    def get_customer_name(self):
        pass

    @abstractmethod
    def set_customer_name(self, name):
        pass

    @abstractmethod
    def get_customer_phone(self):
        pass

    @abstractmethod
    def set_customer_phone(self, phone):
        pass

    @abstractmethod
    def get_customer_email(self):
        pass

    @abstractmethod
    def set_customer_email(self, email):
        pass

    @abstractmethod
    def get_customer_address(self):
        pass

    @abstractmethod
    def set_customer_address(self, address):
        pass