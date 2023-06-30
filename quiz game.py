print("Welcome to my computer quiz")

playing=input("Do you want to play the game?: ")

if playing.lower()!="yes":
    quit()

print("Let's play the game") 
score=0



answer=input("What is the national game of India? ")
if answer.lower()=="hockey":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is the national animal of India? ")
if answer.lower()=="bengal tiger":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is the national flower of India? ")
if answer.lower()=="lotus":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is the national song of India? ")
if answer.lower()=="vande mataram":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got" + str(score) + "questions correct")
print("You scored"+str((score/4)*100)+"%")







