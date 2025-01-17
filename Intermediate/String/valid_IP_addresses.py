'''
    Given a decimal string denoting IP address, return all valid IP addressess 
    which corresponds to that decimal string
'''
def valid_ip(s):
    def is_valid_part(s):
        # '0' is valid but '00', '000', '01' are not valid
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

    # using nested loop for each part
    result, parts = [], [None] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i + j]
                if is_valid_part(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2], parts[3] = s[i + j: i + j + k], s[i + j + k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append(".".join(parts))
    
    return result


print(valid_ip("19216811"))
