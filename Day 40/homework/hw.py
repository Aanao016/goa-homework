# 1) მომხმარებელს შემოატანინეთ წინადადება, დაითვალეთ მასში space-ების რაოდენობა და დაბეჭდეთ.
sentence = input("შეიყვანე წინადადება: ")
space_count = sentence.count(" ")
print("space-ების რაოდენობაა:", space_count)

# 2) შექმენით 5 ელემენტიანი სიტყვების სია. მომხმარებელს შემოატანინეთ სიტყვა და რიცხვი(ეს იქნება პოზიცია სადაც დაამატებთ შემოტანილ სიტყვას). დაბეჭდეთ განახლებული სია.
words = ["კატა", "ძაღლი", "ცხენი", "ვირი", "თაგვი"]
word = input("შეიყვანე სიტყვა: ")
pos = int(input("შეიყვანე რიცხვი (პოზიცია): "))
words.insert(pos, word)
print(words)

# 3) გაკვეთილზე შევქმენით პროგრამა, რომელიც წინადადებას გადაიყვანს camelCase-ში. თქვენი დავალებაა დაწეროთ პროგრამა, რომელიც გააკეთებს პირიქით.
# Input: "helloWorld" -> Output: "Hello world"
word = input("შეიყვანე camelCase სიტყვა: ")
new = ""
for char in word:
    if char.isupper():
        new += " " + char.lower()
    else:
        new += char
print(new.capitalize())


# 4) ასევე დაწერეთ პროგრამა, რომელიც შემოტანილ წინადადებას გადაიყვანს snake_case-ში.
sentence = input("შეიყვანე წინადადება: ")
print(sentence.lower().replace(" ", "_"))

# replace — ეს არის ფუნქცია Python-ში და ზოგ სხვა ენაშიც, რომელიც გამოიყენება სტრიქონში (string) არსებული ტექსტის ჩანაცვლებისთვის.

# 5) შექმენით ცარიელი სია. მომხმარებელს შემოატანინეთ 5 სახელი და ჩაამატეთ ისინი ამ სიაში. გადაურეთ ამ სიას for ციკლით, შემდეგ კი სახელის თითოეულ ასოს(დაგჭირდება 2 for ციკლით, ანუ for ციკლი მეორე for ციკლში). ასევე for ციკლების ზემოთ უნდა გქონდეთ შექმნილი კიდევ ერთი ცარიელი სია, სადაც ჩაამატებთ ასოებიდან მხოლოდ თანხმოვნებს.
# გადაურეთ მიღებულ თანხმოვნების სიას და წაშალეთ დუბლიკატები, მოიძიეთ თუ როგორ შეიძლება სიის დასორტირება, დაასროტრირეთ ის ანბანის მიხედვით და დაბეჭდეთ.
names = []
for i in range(5):
    name = input("შეიყვანე სახელი: ")
    names.append(name)

consonants = []
vowels = "aeiouAEIOUაეიოუ"

for name in names:
    for char in name:
        if char.isalpha() and char not in vowels:
            consonants.append(char.lower())

consonants = list(set(consonants))
consonants.sort()
print("თანხმოვნები:", consonants)
