'''
    Given a sentence populated by a set of strings, we would like to reverse the sentence.
    input --> "Amir needs sleep"
    output --> "sleep needs Amir"
'''

# space complexity!!
def reverse_sentence(s):
    l = [list(word) for word in s.split()]
    word_l = ["".join(ele) for ele in list(reversed(l))]
    return " ".join(word_l)


# better solution
# NOTE: assume s is a string encoded as bytearray!
def better_reverse(s):
    s.reverse()

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
        
    start = 0
    while True:
        end = s.find(" ", start)
        if end < 0:
            break # remember to reverse last word!

        reverse_range(s, start, end - 1)
        start = end + 1
    
    # reverse last word
    reverse_range(s, start, len(s) - 1)


print(reverse_sentence("Amir needs sleep"))
