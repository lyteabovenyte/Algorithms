'''
  Given a string, determine whether it is palindromic or not.
'''

def palindromic(str):
  for i in range(len(str) // 2):
    if str[i] != str[~i]: 
      return False
  return True

def nicer_palindromic(s):
  return all(s[i] == s[~i] for i in range(len(s) // 2))


print(palindromic("amiralaeifar"))
print(palindromic("amirima"))

print(nicer_palindromic("amirima"))

