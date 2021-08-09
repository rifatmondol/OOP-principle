# from bankerImpl import BankerImpl
#
# info = BankerImpl("Rashed Islam", "+8801754657643", "abc@gmail.com", "Dhaka")
# print("User info:", info)

from account import Account

acc = Account(" Rashed Islam", "+8801754657643", "abc@gmail.com", "Dhaka", 1000, 5000,  2000)
print(acc)
print(" Balance:", acc.get_balance(), "\n", "After deposite, Total Balance:", acc.get_deposite(), "\n", "After Withdraw, Total balance:", acc.get_withdraw())