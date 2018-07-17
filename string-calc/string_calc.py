from contextlib import suppress

def add(string):
	splitted_string = string.split(',')
	outcome = 0
	for string_number in splitted_string:
		with suppress(ValueError):
			outcome += int(string_number)
	return str(outcome)
	