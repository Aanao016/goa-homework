
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
    


def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False
    



def find_average(numbers):
    if numbers != []:
        return sum(numbers) / len(numbers)
    else:
        return 0
    


a = "code"
b = "wa.rs"
name = a + b




def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4
    


def say_hello(name):
    return "Hello, " + name


