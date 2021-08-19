'''
Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150,
stop the loop iteration.
'''
list = [10, 16, 26, 30, 50, 80, 100, 150, 160, 190]
for item in list:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)