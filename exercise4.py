#take two comma separated inputs from user
#1. user's name 
#2. a single character 
#output
#1. user's name length 
#2.count the character that user inputed 
name,char=input("enter your name and a single character:").split(",")
print(f"lenth of the name:{len(name)}")
print(name.count(char))

