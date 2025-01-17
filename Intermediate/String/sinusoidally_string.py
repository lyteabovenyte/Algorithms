'''
    Given a string, write the equivalent sinusoidally string
    s = "Hello_World"

      e     _       l
    H  l  o   W   r   d   --> the output should be: e_lHloWrdlo
        l       o
''' 

# brute-force approach
def sinusoidally_string(s):
    box = [[None] * (len(s) // 2 + 1) for _ in range(3)]

    j = 1
    direction = -1
    for i in range(len(s)):
        box[j].append(s[i])
        next_j = j + direction

        if next_j > 2:
            direction = -1
            next_j += direction * 2
        if next_j < 0:
            direction = 1
            next_j += direction * 2
        
        j = next_j
    
    res = [[ele for ele in item if ele is not None] for item in box]
    return "".join([ele for item in res for ele in item])

print(sinusoidally_string("Hello world"))

# pythonic solution with a little bit of focus on the problem
def pythonic_sinusoidally(s):
    return s[1::4] + s[::2] + s[3::4]

print(pythonic_sinusoidally("Hello world"))