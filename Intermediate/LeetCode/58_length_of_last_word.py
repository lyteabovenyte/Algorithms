def length_of_last_word(s: str) -> int:
    s = s.rstrip()
    length = [len(ele) for ele in s.split(" ")]
    return length[-1]

print(length_of_last_word("Hello world"))