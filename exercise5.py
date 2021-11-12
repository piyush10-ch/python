#EXERCISE ,NUMBER GUESSING GAME
#makw a variable/like winning_number and assign any number to it.
#ask user to guess a number
#if user guessed correctly then:
  #if user guessed lower then actual number then print "too low"
  #if user guessed higher than actual number then print "too high"
winning_number= 10

user_input=input("enter any guessed number between  1 to 20: ")
user_input=int(user_input)

if winning_number==user_input:
    print("YOU WIN!!")
else: 
      if user_input < winning_number:
          print("too low")
      else:
          print("too high")      