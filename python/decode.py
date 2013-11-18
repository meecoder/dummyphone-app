decode = {"a": "c", "b": "d", "c": "e", "d": "f", "e": "g", "f": "h", "g": "i",
"h": "j", "i": "k", "j": "l", "k": "m", "l": "n", "m": "o", "n": "p", "o": "q",
"p": "r", "q": "s", "r": "t", "s": "u", "t": "v", "u": "w", "v": "x", "w": "y",
"x": "z", "y": "a", "z": "b"}
print("This is a work in progress. Does not support numbers.")
var = input("Please input the coded message to be decoded, and then press Enter.")
vara = list(var)
i = 0
while i < len(var):
       vara[i] = decode[vara[i]]
       i += 1
print(''.join(vara))
