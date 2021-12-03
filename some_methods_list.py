# count
# sort method
# reverse
# clear
# copy
fruits=['apple','mango','banana','orange','pineapple','apple']
print(fruits.count('apple'))
# sort method can be used in both the string or numbers
fruits.sort()
print(fruits)
numbers=[1,4,6,8,10,4,5]
numbers.sort()
print(numbers)
print(numbers[::-1])#reverse
# if we want to sort the list without changing in the list
num=[1,3,45,63,632,562,1,6,2,7,22]
print(sorted(num))
print(num)
#clear
print(num.clear())
#copy
num1=[4,65,8,6,3456,85,854684,895]
num2_copy=num.copy()
print(num2_copy)
