'''
Given two integer numbers return their product. If the product is greater than 1000, then return their sum.
'''

p1 = int(input("Enter first number:"))
p2 = int(input("Enter second number:"))

product = p1 * p2

if product > 1000:
    print(p1+p2)
else:
    print(product)