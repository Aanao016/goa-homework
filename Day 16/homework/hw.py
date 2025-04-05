
#კომენტარებით ახსენით რა არის sequence და selection. მოიყვანეთ მათი მაგალითები
#Sequence ნიშნავს ინსტრუქციების მიყოლებით შესრულებას.
 # Selection არის სიტუაცია, როდესაც პროგრამა იღებს გადაწყვეტილებას და სხვადასხვა მოქმედებებს ასრულებს, გარკვეულ პირობაზე დაყრდნობით.

# კომენტარებით ახსენით რა არის Control Flow(ივარჯიშეთ if/else-ბზე და გააკეთეთ მინიმუმ 3 მაგალითი)
#Control Flow არის პროცესი, რომელიც განსაზღვრავს, თუ როგორ მუშაობს 
#პროგრამის სხვადასხვა ნაწილები ერთმანეთთან, როგორ გადადის პროგრამა ერთ ფაზაზე მეორე ფაზაში. 

age = 15
if age >= 18:
    print("You are an adult :")
else:
    print("You are a minor :")


number = -5
if number > 0:
    print("The number is positive:")
elif number < 0:
    print("The number is negative :")
else:
    print("The number is zero :")


age = 25
if age < 13:
    print("You are a child :")
elif age < 18:
    print("You are a teenager :")
else:
    print("You are an adult :")


# შექმენით ცვლადი, სადაც შეინახავთ თქვენს სახელს. მომხმარებელს შემოატანინეთ პაროლი და თუ ის უდრის "1234"-ს დაბეჭდეთ "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect"
# Password check
name = "anno" 
password = input("Enter password: ")

if password == "1234":
    print("Password is correct")
else:
    print("Password is incorrect")

# მომხმარებელს შემოატანინეთ რიცხვი, თუ ის ლუწია დაბეჭდეთ "Number is Even", სხვა შემთხვევაში დაბეჭდეთ "Number is Odd"

number = int(input("Enter a number: "))

if number  == 0:
    print("Number is Even")
else:
    print("Number is Odd")
