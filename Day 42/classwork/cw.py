# 1) შექმენით ფუნქცია სახელად even_or_odd, რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაბეჭდავს ლუწია თუ კენტია ის
def even_or_odd():
    num = int(input("რიცხვი: "))
    if num % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")

even_or_odd()

# 2) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს 5 სახელს. შექმნის მისგან სახელების სიას და დაბეჭდავს მას.
def shimpanzinibananini():
    name = input("Enter your name: ")
    print("Hello,", name)


names = ["ANANO", "nini", ",marita", "lika"] 

for i in range(5):
    shimpanzinibananini()


# 3) შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა რიცხვს.
def print_numbers_upto(n):
    for i in range(1, n + 1):
        print(i)

print_numbers_upto(7)

# 4) შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს, და დაბეჭდავს რიგით მე-5 ლუწ რიცხვს შემოტანილი რიცხვის შემდეგ.
def fifth_even_after(n):
    count = 0
    current = n + 1
    while True:
        if current % 2 == 0:
            count += 1
            if count == 5:
                print(current)
                
        current += 1

fifth_even_after(10)
