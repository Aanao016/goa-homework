# 2) შექმენით რიცხვების სია. გადაუარეთ მას for ციკლითი. შეამოწმეთ თუ რიცხვი ლუწია დაბეჭდეთ "Number is even", სხვა შემთხვევაში "Number is Odd"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")


# 3) შექმენით სიტყვების სია 10 ელემენტისგან. გადაუარეთ for ციკლით ამ სიას ისე, რომ დაბეჭდოთ ყოველი მე-2 ელემენტი(დაგჭირდებათ slicing-ი) 
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

for word in words[1::2]:  # იწყება მეორე ელემენტიდან (index 1), და გადადის 2-ით
    print(word)



# 4) შექმენით ცვლადი, სადაც შეინახავთ სიტყვას. გადაუარეთ მას for ციკლით, დაბეჭდეთ მისი თითოეული სიმბოლო და გვერდით მიუწერეთ მისი რიგის ნომერი string-ში(ანუ მერამდენე სიმბოლოა)

#მაგალითად: academy = "GOA"
"G-1"
"O-2"
"A-3"

#გატესტეთ ეს დავალება სხვადასხვა სიტყვებზე და ნახეთ შედეგი 
word = "GOA"

for index in range(len(word)):
    print(f"{word[index]}-{index + 1}")


#5) მოიძიეთ, როგორ შეიძლება სიის შემოტრიალება, შემდეგ შექმენით სია და დაბეჭდეთ ის შემოტრიალებულად. მაგალითად: [1,2] -> [2,1] 

numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print(reversed_list)

#6) მოიძიეთ, რა არის len ფუნქცია და როგორ მუშაობს ის. გააკეთეთ 2 მაგალითი. 

name = "GOA"
print(len(name))  # შედეგი: 3


fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # შედეგი: 3

#7) შექმენით 5 ელემენტიანი სია. გამოიყენეთ for ციკლი, range და len ფუნქციები, რომ შეცვალოთ ამ სიაში არსებული ყოველი მეორე ელემენტი თქვენი სახელით. შემდეგ დაბეჭდეთ ეს სია. 
my_list = ["a", "b", "c", "d", "e"]

for i in range(1, len(my_list), 2):  # იწყებს index 1-დან და მიდის ყოველ მეორე ელემენტზე
    my_list[i] = "YourName"  # შეცვალე "YourName" შენს სახელზე

print(my_list)

 