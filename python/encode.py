from collections import defaultdict

def encode():
	encode = {"a": "y", "b": "z", "c": "a", "d": "b", "e": "c", "f": "d", "g": "e",
	"h": "f", "i": "g", "j": "h", "k": "i", "l": "j", "m": "k", "n": "l", "o": "m", 
	"p": "n", "q": "o", "r": "p", "s": "q", "t": "r", "u": "s", "v": "t", "w": "u", 
	"x": "v", "y": "w", "z": "x"}
	print("This is a work in progress.")
	var = input("Please input the phrase to be encoded, and then press Enter. ")
	vara = list(var.lower())
	i = 0
	while i < len(var):
		if (vara[i] in encode) :
			vara[i] = encode[vara[i]]
			i += 1
		else:
			vara[i] = vara[i]
			i += 1
	print(''.join(vara))
