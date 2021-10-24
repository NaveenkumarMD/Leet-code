dictionary = {"first":[1, 2, 3], 
              "second":[4, 5, 6, 7, 8]}

d = {k: list(map(str, v)) for k,v in dictionary.items()}
print(d)