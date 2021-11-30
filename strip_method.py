name="      piyush      "
dots=".................."
print(name.lstrip()+dots)#for removing the lsft side space 
print(name.rstrip()+dots)#for removing the right side space
print(name.strip()+dots)#for removing all the space
name1="       piyush chaudhary       "
print(name1.strip()+dots)# it cannot remove the space between the word
name2="     pi     yu  sh      "
print(name2.strip()+dots)#like this for this we use replace method
print(name2.replace(" ","") + dots)


