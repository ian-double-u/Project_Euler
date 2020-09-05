# Project Euler Problem 22

import re

def string_score(s):
    """returns score for string s based on the alphabetical 
    position of its letters"""
    s = re.sub(r'[^a-zA-Z]', "", s)
    s = s.lower()
    s = list(s)
    
    alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
              'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
              'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
              'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
              'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    score = 0
    
    for i in s:
        score += alpha[i]
    
    return score

file = open('p022_names.txt', 'r')
names = file.readline()
names = names.split(',')

for i in names:
    names[names.index(i)] = i.replace('"', '')

names.sort()

score = 0
for i in names:
    score += (names.index(i) + 1)*string_score(i)

print(f'Ans = {score}')
