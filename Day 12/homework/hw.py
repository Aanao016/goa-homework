# შექმენით 2 ცვლადი, ერთში შეინახეთ სთრინგ რიცხვი, მეორეში integer-ი . თქვენი დავალებაა მათ შორის მოახდინოთ ყველა მათემატიკური ოპერაცია(+, -, *, /)


string_number = "10" 
integer_number = 5    

sum_result = int(string_number) + integer_number
print("შეჯამება:", sum_result)

difference_result = int(string_number) - integer_number
print("განსხვავება:", difference_result)

multiplication_result = int(string_number) * integer_number
print("გამოცვლა:", multiplication_result)

division_result = int(string_number) / integer_number
print("გაყოფა:", division_result)


# მომხმარებელს შემოატანინეთ სიმაღლე, გადააქციეთ float-ად და დაბეჭდეთ მისი მონაცემთა ტიპი

height = input("შეიტანეთ თქვენი სიმაღლე: ")
height_float = float(height)
print("სიმაღლის მონაცემთა ტიპი (float):", type(height_float))


# კომენტარებით ახსენით რა არის Data Convertion.
#Data Conversion ნიშნავს მონაცემთა ტიპების გადაყვანას ერთიდან მეორეში.

#კომენტარებით ახსენით რა არის implicitly  და explicitly. ჩამოწერეთ ყველა ფუნქცია, რომელიც ცვლის მონაცემთა ტიპს და აღწერეთ

#Implicitly (ავტომატური კონვერტირება): Python-ს შეუძლია ავტომატურად შეიმუშაოს მონაცემთა ტიპების კონვერტირება, 
# როდესაც ვმუშაობთ მონაცემებზე. მაგალითად, როდესაც ვსაუბრობთ ორ რიცხვს (integer და float), Python
#  ავტომატურად გარდაქმნის integer-ს float-ში, რათა მათემატიკური ოპერაცია სწორად შესრულდეს.

# კომენტარებით ახსენით, რა არის ტექსტის ფორმატირების დეგები და ჩამოთვალეთ ისინი

#ტექსტის ფორმატირების დეგები (HTML-ის კონტექსტში) ნიშნავს სპეციალურ ტეგებს,
#რომლებიც გამოიყენება ტექსტის ვიზუალური სტილის, ფორმის და შეწონილობის შესაცვლელად.
 


