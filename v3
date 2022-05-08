# imports
import random
import time as tm

"""
- read clock time
- EQUALITY ALWAYS ACROSS MIDDLE
- (abs) last
- fix formatting for mult (x), div (÷), pow (^), root ({tens}root({ones}))), abs (||, replace paren)

"""

# functions
def printTime(hour, min):  # print time
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
			combos.append(f"{tens} + {ones}")
			combos.append(f"{tens} - {ones}")
		combos.append(f"{tens} * {ones}")  # ones zero is okay here
		if(ones != 0):  # do it this way to keep + - * / order
			combos.append(f"{tens} / {ones}")
		combos.append(f"{tens} ** {ones}")
		if((ones != 0) and (tens != 1)):  # root
			combos.append(f"{ones} ** (1 / {tens})")
	
	return combos

def evaluate(left, right):
	empty = True

	for l in left:
		for r in right:
			if(eval(l) == eval(r)):
				empty = False
				if(len(l) == 1):  # so no parentheses around single digit
					print(f"{l} = ", end = "")
				else:
					print(f"({l}) = ", end = "")
				if(len(r) == 1):  # so no parentheses around single digit
					print(f"{r}")
				else:
					if(r[2:4] == "* "):
						print(f"({r[0:1]} x {r[4:5]})")
					elif(len(r) == 6): # length of pow
						print(f"({r[0:1]} ^ {r[5:6]})")
					elif(len(r) == 12): # length of root
						print(f"{r[10:11]}root({r[0:1]})")
					else:
						print(f"({r})")
	if(empty):
		print("no combinations possible")

def production():
	# variables
	time = tm.localtime()
	hour = (time.tm_hour % 12)  # not military time
	min = time.tm_min
	# hour = 2; min = 24
	left = getCombos(hour)  # list to store combinations on left side as strings
	right = getCombos(min)  # list to store combinations on right side as strings

	printTime(hour, min)
	evaluate(left, right)

def main():
	production()

# execute
main()
