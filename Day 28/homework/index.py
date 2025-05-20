# 2) გაიმეორეთ ყველა განვლილი მასალა: range ფუნქცია for/while ციკლები და if/elif/else
for i in range(5):
    print("რიცხვი:", i)

i = 0
while i < 5:
    print("რიცხვი while ციკლით:", i)
    i += 1

num = int(input("შეიყვანეთ რიცხვი: "))
if num > 0:
    print("დადებითი")
elif num < 0:
    print("უარყოფითი")
else:
    print("ნული")

# 3) მომხმარებელს შემოატანინეთ 5 რიცხვი. თქვენი დავალებაა დაითვალოთ აქედან დადებითი და უარყოფითი რიცხვები. საბოლოოდ დაბეჭდეთ შემდეგი ფორმატით:
# "Positive numbers count: {count}"
# "Negative numbers count: {count}"
positive_count = 0
negative_count = 0

for i in range(5):
    number = int(input(f"შეიყვანეთ რიცხვი: "))
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

print("Positive numbers count:", positive_count)
print("Negative numbers count:", negative_count)

# 4) მომხმარებელს შემოატანინეთ 3 რიცხვი და დაითვალეთ რამდენი მათგანია 10-ზე მეტი. თუ ყველა შემოტანილი რიცხვი ათზე მეტია, დაბეჭდეთ "All the numbers that are larger than ten.", სხვა შემთხვევაში დაბეჭდეთ "Some numbers that are less than or equal to ten."
count = 0

for i in range(3):
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number > 10:
        count += 1

if count == 3:
    print("All the numbers that are larger than ten.")
else:
    print("Some numbers that are less than or equal to ten.")

# 5) მომხმარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ეს რიცხვი მარტივი(მარტივი არის რიცხვი, რომელიც მხოლოდ 1-ზე და საკუთარ თავზე იყოფა). შემდეგ კი დაბეჭდეთ "This is prime number" თუ რიცხვი მარტივია, სხვა შემთხვევაში "This isn't prime number"

num = int(input("შეიყვანეთ რიცხვი: "))

if num <= 1:
    print("This isn't prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("This is prime number")
    else:
        print("This isn't prime number")

