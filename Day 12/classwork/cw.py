# მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში როგორც string-ი. შემდეგ დაბეჭდეთ მისი მონაცემთა ტიპი.
#შეუცვალეთ მას მონაცემთა ტიპი ჯერ integer-ად, შემდეგ float-ად და თითოეული გარდაქმნისას დაბეჭდეთ მისი მონაცემთა ტიპი.

number_str = input("შეიტანეთ რიცხვი: ")
print("მონაცემთა ტიპი (string):", type(number_str))

number_int = int(number_str)
print("მონაცემთა ტიპი (integer):", type(number_int))

number_float = float(number_str)
print("მონაცემთა ტიპი (float):", type(number_float))
