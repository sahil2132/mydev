import random

guessTaken=0

number = random.randint(1,20)


while guessTaken<5:
	print ('Take a Guess')
	guess=input()
	guess=int(guess)

	guessTaken=guessTaken+1

	if guess < number:
		print ('Guess Was Smaller than Number')
	if guess > number:
		print ('Guess was Larger than Number')
	if guess == number:
		print ('Correct')
		break