# Name: Dennis Tran
# Period 6
# Dice Rolling Simulator
import random
random.randint(1,6)
# Welcome to Dice Game
print("Welcome to the Dice Game. ")

# Result Score
def printResults():
	print("1s - ")
	print("2s - ")
	print("3s - ")
	print("4s - ")
	print("5s - ")
	print("6s - ")

print("Input the number of times a 6 sided die will be rolled: ")
numRolls = int(input("how many rolls: "))
x = 1

while x <= numRolls: 
	x += 1
	x <= 100
	print(random.randint(1,6))
	
	# Show Results
	printResults()
while True: 
	if x == 1:
		pass