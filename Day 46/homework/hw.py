# 1) შექმენით ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს.`

def sum_two_numbers(a,b):
    return a + b
result = sum_two_numbers(6, 9)
print(result)

# 2) შექმენით ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მისი კვადრატის მნიშვნელობას.

def numbers(x):
    return x ** 2
result = numbers(9)
print(result)

# 3) შექმენით ფუნქცია, რომელიც იღებს სიას და აბრუნებს ამ სიაში უდიდეს რიცხვს.

def find_max_number(numbers):
    return max(numbers)
my_list = [ 3 , 9, 18 , 30]
result = find_max_number(my_list)
print(result)

# 4) შექმენით ფუნქცია, რომელიც იღებს 3 რიცხვს და აბრუნებს მათ საშუალო არითმეტიკულს (sum / quantity).

def average_of_three(a, b, c):
    return (a + b + c) / 3

result = average_of_three(5, 10, 20)
print(result)  


# 5) შექმენით ფუნქცია, რომელიც იღებს სიას და აბრუნებს ამ სიის შებრუნებულ ვერსიას.

def reverse_list(my_list):
    return my_list[::-1]

numbers = [1, 2, 3, 4, 5]
result = reverse_list(numbers)
print(result) 

# 6) შექმენით ფუნქცია, რომელიც იღებს სიტყვას და აბრუნებს, არის თუ არა ეს სიტყვა პალინდრომი. როგორი სიტყვებია პალინდრომი, შეგიძლიათ გაეცნოთ ქვემოთ დართულ წყაროში:

def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome("mother"))     
print(is_palindrome("man"))     
