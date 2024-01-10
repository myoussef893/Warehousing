# Morse code alphabet and numbers dictionary
morse_code = {
		"a": "·–",
		"b": "–···",
		"c": "–·–·",
		"d": "–··",
		"e": "·",
		"f": "··–·",
		"g": "––·",
		"h": "····",
		"i": "··",
		"j": "·–––",
		"k": "–·–",
		"l": "·–··",
		"m": "––",
		"n": "–·",
		"o": "–––",
		"p": "·––·",
		"q": "––·–",
		"r": "·–·",
		"s": "···",
		"t": "–",
		"u": "··–",
		"v": "····–",
		"w": "·––",
		"x": "–··–",
		"y": "–·––",
		"z": "––··",
		"1": "··––––",
		"2": "··–––",
		"3": "··––",
		"4": "··–",
		"5": "·–",
		"6": "–··",
		"7": "––··",
		"8": "–––··",
		"9": "––––··",
		"0": "––––",
}





prmpt = input("Enter the Morse code to be translated: ")

def translator(prmpt):
	lister = list(prmpt)
	bucket = []
	for i in lister: 
		print(morse_code[i])
		bucket.append(morse_code[i])
	return print(bucket)