# 1)
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

# 2)
def between(a, b):
    return list(range(a, b + 1))

# 3)
def reverse_words(s):
    return ' '.join(s.split()[::-1])
