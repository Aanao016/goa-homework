# 2) კომენტარებით ახსენით რა არის slicing
# Python-ში დაჭრა საშუალებას გაძლევთ ამოიღოთ სიის (ან სტრიქონის, tuple-ის) ნაწილი შემდეგი ფორმატის გამოყენებით:
# list[start:stop:step]
# ეს დარამეstopში

# 3) გაიმეორეთ range ფუნქცია და გააკეთეთ 3 მაგალითი

# მაგალითი 1: 0-დან 4-მდე რიცხვები
# print(list(range(5)))     # [0, 1, 2, 3, 4]

# # მაგალითი 2: 3-დან 9-მდე რიცხვები
# print(list(range(3, 10)))  # [3, 4, 5, 6, 7, 8, 9]

# # მაგალითი 3: 2-დან 20-მდე ყველა მეორე რიცხვი (ნაბიჯით 2)
# print(list(range(2, 21, 2)))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# 4) შექმენით 10 ელემენტიანი სია და slicing-ის გამოყენებით დაბეჭდეთ სიის მე-2, მე-5 და მე-8 ელემენტი
#          0    1   2   3   4   5   6   7   8   9
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

second_element = my_list[1:2]
fifth_element = my_list[4:5]
eighth_element = my_list[7:8]

print("მე-2 ელემენტი:", second_element)
print("მე-5 ელემენტი:", fifth_element)
print("მე-8 ელემენტი:", eighth_element)

# 5) slicing-ის გამოყენებით დაბეჭდეთ იგივე სიის მე-3 ელემენტიდან დაწყებული სიის ყველა ელემენტი
  
fourth_element = my_list[3:]
print(fourth_element)
