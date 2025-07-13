# 1) გადაიმეორეთ ყველაფერი რაც აქამდე ისწავლეთ ფუნქციებზე, მათ სახეობებზე მათ დანიშნულებებზე.
def greet():
    print("Hello")

def greet(name):
    print("Hello,", name)
    
def add(a, b):
    return a + b

# 2) დაწერე ფუნქცია, რომელიც ბეჭდავს "Hello, world!"
def say_hello():
    print("Hello, world!")

# 3) დაწერე ფუნქცია, რომელიც იღებს სახელს და ბეჭდავს "Hello, [სახელი]!"
def greet(name):
    print(f"Hello, {name}!")

# 4) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს
def add_numbers(a, b):
    return a + b

# 5) დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 6) დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს
def average(numbers):
    return sum(numbers) / len(numbers)

# 7) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს ამ სტრიქონის სიგრძეს
def string_length(text):
    return len(text)

# 8) დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მას შებრუნებულ მდგომარეობაში
def reverse_list(lst):
    return lst[::-1]

# 9) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მას დიდ ასოებად გადაყვანილს
def to_upper(text):
    return text.upper()

# 10) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ შორის უმეტესს
def max_of_two(a, b):
    return max(a, b)

# 11) დაწერე ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს True თუ ის უარყოფითია, False თუ არა
def is_negative(n):
    return n < 0

# 12) დაწერე ფუნქცია, რომელიც იღებს სიტყვების სიას და აბრუნებს სიის ყველაზე გრძელ სიტყვას. გამოიყენე ციკლი და 'len()' შედარებისთვის
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# 13) დაწერე ფუნქცია, რომელიც იღებს რიცხვს 'n' და აბრუნებს სიას 1-დან 'n'-ის ჩათვლით ყველა ლუწი რიცხვით. გამოიყენე for ციკლი და if-else
def even_numbers(n):
    evens = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

# 14) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მასში ხმოვნების (a, e, i, o, u) რაოდენობას. გამოიყენე ციკლი და if-else
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
