# imports
import random
import time as tm

"""
- read clock time
- EQUALITY ALWAYS ACROSS MIDDLE
- (+ - * /) first 
	- make for loop that gets all combinations of each and puts them into an array (both sides)
	- run each entry in first side against each entry in the other, 
- (pow root) next(
- (abs) last
- fix formatting for mult (x), div (÷), pow (^), root ({tens}root({ones}))), abs (||, replace paren)

"""
# variables
time = tm.localtime()
hour = (time.tm_hour % 12)  # not military time
min = time.tm_min
left = []  # list to store combinations on left side as strings
right = []  # list to store combinations on right side as strings

# functions
def printTime(hour, min):  # print time
	if(hour < 10):
		print("0", end = "")  # add zero before hour for consistent spacing
	print(f"{hour}:", end = "")
	if(min < 10):
		print("0", end = "")  # add zero before min for consistent spacing
	print(min)


def getCombos(n):  # return list of strings of all legal number combinations for a hour/min n
	tens = int(n / 10)  # tens position
	ones = (n % 10)  # ones position
	combos = []

	combos.append(f"{n}")  # always add just the number
	if(tens != 0):  # if we have two digits to perform operations on
		if(ones != 0):
			combos.append(f"({tens} + {ones})")
			combos.append(f"({tens} - {ones})")
		combos.append(f"({tens} * {ones})")  # ones zero is okay here
		if(ones != 0):  # do it this way to keep + - * / order
			combos.append(f"({tens} / {ones})")
		combos.append(f"({tens} ** {ones})")
		if((ones != 0) and (ones != 1)):  # root
			combos.append(f"({tens} ** (1 / {ones}))")
	
	return combos

def evaluate(left, right):
	empty = True

	for l in left:
		for r in right:
			if(eval(l) == eval(r)):
				empty = False
				print(f"{l} = {r}")
	
	if(empty):
		print("no combinations possible")

# execute
left = getCombos(3)
right = getCombos(31)
evaluate(left, right)
