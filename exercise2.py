#ask user to input 3 numbers and you have to print average of three numbers using string formatting
num1,num2,num3=input("enter first number,second number,third number").split(",")

print(f"the avg is {(int(num1)+int(num2)+int(num3))/3}")
