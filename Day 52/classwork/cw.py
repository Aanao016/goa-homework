#1)
def positive_sum(arr):
    positive_sum = 0
    for arr in arr:
        if arr > 0:
            positive_sum += arr
    
    return positive_sum

positive_sum( [1, -4, 7, 12])

# 2)

def no_space(x):
     return x.replace(" ","")
no_space("8 j 8   mBliB8g  imjB8B8  jl  B")

# 3)

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        raise ValueError("Invalid operator")
    
# 4)
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"    
    

# 5)
def get_count(sentence):
    vowels = " aeiouy "
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

# 6)
def friend(x):
    result = [ ]
    for name in x :
        if len(name) == 4 :
            result.append(name)
    return result