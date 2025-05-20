#1) მომხმარებელს შემოატანინეთ ასაკი და შეამოწმეთ თუ ის ნაკლებია 18-ზე მაშინ შეამოწმეთ თუ ასაკი ნაკლებია 14-ზე დაუბეჭდეთ Discount 20%, სხვა შემთხვევაში Discount 10%.
#თუ პირველი if-ი არასწორია დაბეჭდეთ No discount.

age = int(input("შეიყვანეთ თქვენი ასაკი:"))

if age < 18:
    if age < 14:
        print("Discount 20%")
    else:
        print("Discount 10%")
else:
    print("No discount")

#2) შექმენით infinity loop-ი(გამოიყენეთ while loop-ი)
x = 1
while x > 0:
    print("ეს არის უსასრულო ციკლი")
