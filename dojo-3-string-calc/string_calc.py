from contextlib import suppress
import re

def add(string):
	splitted_string = re.split(r'[,\n]', string)

	outcome = 0
	for string_number in splitted_string:
		with suppress(ValueError):
			outcome += float(string_number)
	return '{:.0f}'.format(outcome)
	