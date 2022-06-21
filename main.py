isHungry = input("Y/N: Are you hungry?")
isBored = input("Y/N: Are you bored?")

if(isHungry == "Y" or isHungry == "y"):
  print("Go eat")
else:
  print("Don't eat")
if(isBored == "Y" or isBored == "y"): 
  print("Go to sleep")
else: 
  print("Do nothing")

userNumber = int(input("Give me a number: "))
if(userNumber>0):
  print("Your numberis positive")
else:
  print("Your number is negative")

  #ask the user for their age. 
  #if the user is older than 17, let them know they can watch all movies.
  #if they are younger than 17 but older than 13, let them know they can watch G-rated movies and PG-13
  #if they're younger than 13, they're only allowed to watch just G-rated movies

  userAge= int(input("Enter your age:"))

if(userAge >=17): 
  print("You can watch all movies!")
elif(userAge <17 and >=13):
  print("You can watch G-Rated and PG-13 movies!")
else:
  print("You can only watch G-Rated movies.")