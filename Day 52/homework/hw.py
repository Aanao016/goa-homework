# 1)
def multiply(a, b):
    return a * b

print (multiply(5 , 10))


# 2)
def simple_multiplication(number):
    if number % 2 == 0:  
        return number * 8
    else:  
        return number * 9
    

# 3)
def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3 

    if 90 <= avg <= 100:
        return "A"
    elif 80 <= avg < 90:
        return "B"
    elif 70 <= avg < 80:
        return "C"
    elif 60 <= avg < 70:
        return "D"
    else:
        return "F"
    
# 4)
def make_negative(number):
    if number > 0:      
        return -number    
    else:                 
        return number     
    