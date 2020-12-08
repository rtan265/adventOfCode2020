import os
import sys


value = sys.stdin.readline()
integerArray = []
test = []
while value != "":
	integerArray.append(int(value))
	value = sys.stdin.readline()

integerArray.sort()

start_index = 0
end_index = len(integerArray) - 1
TARGET = 2020

total = 0

while total != TARGET:
	total = integerArray[start_index] + integerArray[end_index]
	if total == TARGET:
		print(integerArray[start_index] * integerArray[end_index])
		break
	elif start_index > end_index:
		print("Incorrect, try again.")
		break
	elif total > TARGET:
		end_index -= 1
	elif total < TARGET:
		start_index += 1
