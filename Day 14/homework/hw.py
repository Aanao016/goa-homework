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


