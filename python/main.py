from collections import defaultdict
from encode import encode
from decode import decode
from random import randint

def go():
	test = input("Press 1 for encoding and 2 for decoding, then press Enter. ")
	
	if(test == "1"):
		encode()
	elif(test == "2"):
		decode()
	else:
		print("Please type 1 or 2. Try again.")
		go()

go()

