# problem
# ask user to input a number containing more than one digit 
# example -1256
# calculate 1+2+3+4 and print

number = input("enter a number ")
total=0
i = 0
while i < len(number):
    total += int(number[i])
    i  += 1
print(total)