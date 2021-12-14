playing=input("Do you want Play ? : ").lower()
if playing !="yes":
    quit()
print("Ok Let's Play!")
score=0
quiz=input("What does CPU Stand For ? ").lower()

if quiz=="central processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")

quiz=input("What does UPSC Stand For ? ").lower()

if quiz=="union public service commission":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

quiz=input("What does GPU Stand For ? ").lower()

if quiz=="graphical user interface":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
quiz=input("Is English Programming Language ? ").lower()

if quiz=="yes":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

score
print("You got "+str(score) +" questions correct!")
print("You got "+str((score /4)*100)+"%.")