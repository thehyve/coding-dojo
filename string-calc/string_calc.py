def add(string):
	splitted_string = string.split(',')
	outcome = 0
	for string_number in splitted_string:
		if not string_number:
			string_number = '0' 
		outcome += int(string_number)
	return str(outcome)
	