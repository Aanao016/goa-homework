
# 1) მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ის uppercase-ში
name = "anano"
print(name.upper())
# 2) იგივე სახელი დაბეჭდეთ lowercase-ში
print(name.lower())
# 3) იგივე სახელი დაბეჭდეთ ისე, რომ მისი პირველი ასო იყოს uppercase-ში დაწერილი, ხოლო დანარჩენი lowercase-ში
formatted_name = name.capitalize()
print(formatted_name)

# 4) შექმენით ცვლადი, სადაც შეინახავთ ნებისმიერ სიტყვას. მომხმარებელს შემოატანინეთ სიმბოლო, რომლის ინდექსიც უნდა იპოვოთ სთრინგში და დუბეჭდოთ შემდეგი ფორმატით "a - 0"

# თუ მომხმარებელმა ჩაწერა ისეთი სიმბოლო, რომელიც არ არის სიტყვაში. დაუბეჭდეთ რომ "This symbol is not in word"

word = "example"
symbol = input("Enter a symbol to find its index: ")

if symbol in word:
    for i in range(word):
        if word[i] == symbol:
            print(symbol + " - " + str(i))
else:
    print("This symbol is not in word")

