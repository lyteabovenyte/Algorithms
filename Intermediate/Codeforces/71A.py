'''
    Way too long words.
    problem at : https://codeforces.com/problemset/problem/71/A
'''

def automation(s):
    if len(s) <= 10:
        return s
    else:
        return s[0] + str(len(s[1:-1])) + s[-1]



words = int(input())

all_words = []

for _ in range(words):
    all_words.append(str(input()))
    
    
for i in range(len(all_words)):
    print(automation(all_words[i]))