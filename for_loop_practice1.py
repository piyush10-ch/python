# practice for loop
#ask user a number like 1256
# calculate the sum of digits 1+2+3+5+6
total=0
num =input("enter a number: ")
for i in range(0,len(num )):
    total+=int(num[i])
    print(total)