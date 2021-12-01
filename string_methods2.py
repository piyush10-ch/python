string =" she is beautiful she is good dancer"
print(string.replace("is","was"))
print (string.replace("is","are", 1))# if i want only replace the first "is" 
#find method
print(string.find("good"))# 
print(string.find("is"))
print(string.find("is", 10))#here 10 is where we want to start the searching of the string
# if we don't knw the first (is) position an dwe want to find the second is position 
#for ex
string1= "kfjdfdn is fdvj joj hh  jj k nknnn   hjjjvalvjn jnjvc fdj  f jnnis jn is jnjfffddkjnibcfiuhfxnd fhfdhbjhd"
is_pos1= (string1.find("is"))
is_pos2=(string1.find("is",is_pos1+1))
print(is_pos2)
