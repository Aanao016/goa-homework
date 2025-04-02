#შექმენით რეგისტრაცია/ავტორიზაციის სიმულაცია:
#მომხმარებელს შემოატანინეთ ემაილი, პაროლი და შეინახეთ ისინი ცვლადებში.
# ისევ შემოატანინეთ ემაილი და პაროლი(ეს იქნება ავტორიზაცია) და თუ შემოტანილი 
# მნიშვნელობები დაემთხვევა რეგისტრაციისას შეყვანლის, დაბეჭდეთ True, სხვა შემთხვევაში False.

password="ananoo"
user_input=input("enter your email : ")
print(user_input == password)  #false

password="password"
user_input=input("enter your email: ")
print(user_input  == password)  #true

# კომენტარებით ახსენით რა არის ლოგიკური ოპერატორები და გააკეთეთ თითოეულ ოპერატორზე 4-4 მაგალითი

if 5 > 3 and 7 > 2:
    print("Both conditions are True")

if 5 > 3 and 2 > 7:
    print("This will not print")

if 2 > 3 and 1 > 0:
    print("This will not print either")

if "apple" == "apple" and "banana" == "banana":
    print("Both strings are equal")



if 5 > 3 or 2 > 7:
    print("One of the conditions is True")

if 10 > 5 or 3 < 7:
    print("Both conditions are True")

if 1 > 3 or 4 > 2:
    print("This will print because the second condition is True")

if 1 > 3 or 2 > 7:
    print("This will not print")



if not (5 > 3):
    print("This will not print")

if not (3 > 5):
    print("This will print")

if not ("apple" != "banana"):
    print("This will not print")

if not (7 == 7):
    print("This will not print")





if (5 > 3) != (7 < 2):
    print("Only one condition is True")


if (5 > 3) != (2 < 7):
    print("This will not print")


if (2 > 3) != (4 > 7):
    print("This will not print either")


if (10 == 10) != (7 > 8):
    print("This will print because only one is True")
