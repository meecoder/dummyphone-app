from collections import defaultdict
from random import randint

def encode():
    number2letter = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g',
    8 : 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q',
    18 : 'r', 19 : 's', 20 : 't', 21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 26 : 'z'}
    
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
    pl = 0
    dummyx = 0
    dummyx2 = 0
    varb = vara
    for i in vara:
        pl = pl + 1
        if (dummyx == 1):
            varb.insert(pl + 1, number2letter[randint(1, 26)])
            pl = pl + 1
            if (dummyx2 == 0):
                dummyx2 = 1
            elif (dummyx2 == 1):
                varb.insert(pl + 1, number2letter[randint(1, 26)])
                dummyx2 = 0
                pl = pl + 1
            dummyx = 0
        elif (i == ''):
            break
        else:
            dummyx = 1
    print(''.join(varb))
