#sum from 1 to 10
#1+2+3.....10
# total =0
 #for i in range(1,11):
 #    total=total+i
 # print(total)   
num=input("enter a  number from where ytou want to add a number ")
num=int(num)
total=0
for i in range(1,num+1):
    total+=i 
print(total)