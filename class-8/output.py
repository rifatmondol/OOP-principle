# from bankerImpl import BankerImpl
#
# info = BankerImpl("Rashed Islam", "+8801754657643", "abc@gmail.com", "Dhaka")
# print("User info:", info)

from account import Account

acc = Account(" Rashed Islam", "+8801754657643", "abc@gmail.com", "Dhaka", 3000, 5000,  1500)
print(acc)
print(" Deposite:", acc.get_deposite(), "\n", "Total Balance:", acc.get_balance(), "\n", "After Withdraw, total balance:", acc.get_withdraw())