# Take in a string, get the first number and the last number from it and return the concat value
# TODO: Need to parse out first and last number from digits and words of digits
from enum import IntEnum

class Word_Digits(IntEnum):
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9


# Return a tuple of the number and the start index
def get_digit_word_from_line(line):
	pair = []

	for digit in Word_Digits:
		length = len(digit.name)
		left_index = line.find(digit.name.lower())
		right_index = line.rfind(digit.name.lower())

		if left_index == -1 and right_index == -1:
			continue
		elif (left_index == right_index):
			pair.append((Word_Digits[line[left_index:left_index+length].upper()].value, left_index))
		else:
			if left_index != -1:
				pair.append((Word_Digits[line[left_index:left_index+length].upper()].value, left_index))
			if right_index != -1:
				pair.append((Word_Digits[line[right_index:right_index+length].upper()].value, right_index))

	return pair

def get_numbers_from_line(line):
	pair = []

	for n in range(1, 10):
		right_index = line.find(str(n))
		left_index = line.rfind(str(n))

		if left_index == -1 and right_index == -1:
			continue
		elif (left_index == right_index):
			pair.append((int(line[left_index]), left_index))
		else:
			if left_index != -1:
				pair.append((int(line[left_index]), left_index))
			if right_index != -1:
				pair.append((int(line[right_index]), right_index))

	return pair

def get_first_and_last_digits(line):
	digits = []
	left_most_digit = (0, 0)
	right_most_digit = (0, 0)

	digits += get_digit_word_from_line(line)
	digits += get_numbers_from_line(line)

	for i in range(0, len(digits)):
		if i == 0:
			left_most_digit = digits[i]
			right_most_digit = digits[i]

		left_most_digit = digits[i] if left_most_digit[1] > digits[i][1] else left_most_digit 
		right_most_digit = digits[i] if right_most_digit[1] < digits[i][1] else right_most_digit

	print(digits)
	return int(f"{left_most_digit[0]}{right_most_digit[0]}")


if __name__ == "__main__":
	end_value = 0

	with open('day1_inputs.txt') as file:
		for line in file:
			# breakpoint()
			end_value += get_first_and_last_digits(line.strip())
			print(f"Current value {end_value}.")

	# get_first_and_last_digits('gtlbhbjgkrb5sixfivefivetwosix')

	print(f"\nFinally value: {end_value}")