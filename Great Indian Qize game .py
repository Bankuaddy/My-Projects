print ("Welcome to the Great Indian Quiz")
print("")

playing = input("Do You want to play or not?\n")
print (playing)
if playing.lower() != "yes":
    quit()
print("")

print ("Okay! so let's start the Quiz :)")
score = 0
print("")

print("Question number 1")
answer = input ("What is the capital of India?\n")
if answer.lower() == "delhi":
    print ("correct! ")
    score += 1
else:
    print("Incorrect!")
print("")

print("Question number 2")
answer = input ("In which year India gained its Independance?\n")
if answer.lower() == "1947":
    print ("correct! ")
    score += 1
else:
    print("Incorrect!")
print("")

print("Question number 3")
answer = input ("How many Wars did India fought against Pakistan?\n")
if answer.lower() == "3":
    print ("correct! ")
    score += 1
else:
    print("Incorrect!")
print("")

print("Question number 4")
answer = input ("What is the national animal of India?\n")
if answer.lower() == "tiger":
    print ("correct! ")
    score += 1
else:
    print("Incorrect!")
print("")

print("Question number 5")
answer = input ("Which city of India is known as the city of lakes?\n")
if answer.lower() == "udaipur":
    print ("correct! ")
    score += 1
else:
    print("Incorrect!")
print("")

print("You got " + str(score) + " Questions correct!")
print("You got " + str((score/5) * 100) + "%.")