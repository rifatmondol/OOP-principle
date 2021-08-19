'''
Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration
print the sum of the current number and previous number
'''

# PreviousNum = 0
# for i in range(0,10):
#     PreviousNum = PreviousNum + i
#     print("Current Number",i,"Previous Number",PreviousNum,"Sum:", PreviousNum+i)


s=0
for i in range (0,10,1):
    prev = s
    s += i
    print ("Current:", i, "Previous:", prev,"Sum:", s)