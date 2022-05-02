import math


def character_to_value(character):
	return characters.index(character)


def word_to_value(word):
	value = 0
	factor = 1

	for character in reversed(word):
		value += character_to_value(character) * factor
		factor *= len(characters)

	return value


def value_to_word(value):
	word = ""

	while value:
		word += characters[value % len(characters)]
		value //= len(characters)

	word = list(word)
	word.reverse()

	return "".join(word)


def calculate_next_guess(min_guess, max_guess):
	min_value = word_to_value(min_guess)
	max_value = word_to_value(max_guess)

	mid_value = math.ceil((min_value + max_value) / 2)

	guess = value_to_word(mid_value)

	return guess


running = True

while running:
	characters = input("What characters are used? (such as abc...) ")
	# 0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ
	# abcdefghijklmnopqrstuvwxyz
	# 0123456789

	current_min = input("What is the smallest possible answer? (such as aaaaa) ")
	current_max = input("What is the biggest possible answer? (such as zzzzz) ")

	while True:
		next_guess = calculate_next_guess(current_min, current_max)

		print("Next guess: {0}".format(next_guess))
		result = input("More or less? (m for more, l for less, n for next game, x for exit) ")

		if result == "m":
			current_min = next_guess
		elif result == "l":
			current_max = next_guess
		elif result == "n":
			break
		elif result == "x":
			running = False
			break
