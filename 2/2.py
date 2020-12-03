from functools import reduce

def get_list():
    with open('2/2.input') as file:
        lines = file.read().strip().split('\n')
        tokens = [ l.split() for l in lines ]
        parsed = [ (list(map(int, t[0].split('-'))), t[1].rstrip(':'), t[2]) for t in tokens ]
        return parsed

def char_count(char, string):
    return reduce(lambda accum, c: (accum + 1) if c == char else accum, string, 0)

def valid1(x):
    lower, upper = x[0]
    char = x[1]
    passw = x[2]
    return lower <= char_count(char, passw) <= upper

def valid2(x):
    lower, upper = x[0]
    char = x[1]
    passw = x[2]
    return (passw[lower - 1] == char) ^ (passw[upper - 1] == char) # xor


entries = get_list()
print(sum(map(valid1, entries)))
print(sum(map(valid2, entries)))

