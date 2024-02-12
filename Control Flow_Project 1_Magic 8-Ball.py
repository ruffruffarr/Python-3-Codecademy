#import the random module
import random

#generate infomration fomr  user
name = "Jake"
question = "Am I pretty?"
answer = ""

#generate a random number between 1 and 9 using the random module
random_number = random.randint(1,9)
print (random_number)

#create random answers based on the randomnly generated numbers 
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say not so good"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

if name=="":
   print("Question: " + question)
   print ("Magic 8-Ball's answer: " + answer)
else:
  print (name + " asks: " + question)
  print ("Magic 8-Ball's answer: " + answer)