

'''Quiz Game Python Script'''

print("Welcome to the MCU Quiz!")

playing = input("Would you like to play my game? ")

if playing != "yes":
	quit()

print("Amazing! Let's start playing! ")
score = 0

answer = input("Who is the God of Thunder? ").lower()
if answer == "thor":
	print("Correct, continue to Question 2 ")
	score += 1
else: 
	print("Sorry, that's incorrect!")

answer = input("What was Dr Strange's previous proffession? ").lower()
if answer == "surgeon":
	print("Correct, continue to Question 3 ")
	score += 1

else: 
	print("Sorry, that's incorrect!")

answer = input("Who sacrifices themself for the Soul Stone in Avengers Endgame? ").lower()
if answer == "black widow":
	print("Correct, continue to Question 4 ")
	score += 1
else: 
	print("Sorry, that's incorrect!")

answer = input("Who does Robert Downey Jr portray in the MCU? ").lower()
if answer == "iron man":
	print("Correct, continue to Question 5 ")
	score += 1
else: 
	print("Sorry, that's incorrect!")

answer = input("Who does Heimdall send back to Earth via the Bifrost at the start of Infinity War? ").lower()
if answer == "hulk":
	print("Correct, continue to Question 6 ")
	score += 1
else: 
	print("Sorry, that's incorrect!")

answer = input("What was Hela the God of ").lower()
if answer == "death":
	print("Correct, Quiz Complete! ")
	score += 1
else: 
	print("Sorry, that's incorrect!")

print("You scored " + str(score) + " out of 6")
if score == 6:
	print("Full Marks, well done!")
else:
	if score == 5:
		print ("Not a bad score, try again for full marks! ")
	if score < 5:
		print("Better luck next time! ")	