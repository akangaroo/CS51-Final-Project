def get_mode(list):
	
	dict = {}
	mode = None
	freq = 0

	for elt in list:
		if elt in dict:
			dict[elt] += 1
		else:
			dict[elt] = 1
		if dict[elt] > freq:
			mode = elt
			freq = dict[elt]
	print mode
	return mode

