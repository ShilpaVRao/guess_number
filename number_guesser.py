print("Welcome to my computer quiz!")

playing=input("Do you want to play?")


if playing.lower() != "yes":
    quit()
print("Okay! Lets's playy :)")
score=0

answer=input("what does CPU stands for? ")

if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("what does GPU stands for? ")

if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
    
else:
    print("Incorrect!")

answer=input("what does RAM stands for? ")

if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("what does PSU stands for? ")

if answer.lower()=="power supply":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


print("you got " +str(score)+ " correct")
print("you got " +str((score/4)*100)+ " %")


    
