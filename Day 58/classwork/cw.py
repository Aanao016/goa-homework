# 1) შექმენით ფუნქცია(def-ის გამოყენებით), რომელიც იქნება split ფუნქციის კლონი, ანუ შეასრულებს მის ფუნქციას(split-ის გამოყენების გარეშე)
def my_split(text, separator=" "):
    words = []
    current_word = ""
    
    for char in text:
        if char == separator: 
            words.append(current_word)
            current_word = ""
        else:
            current_word += char
    words.append(current_word)  
    
    return words


# 2) შექმენით join ფუნქციის კლონი
def my_join(words_list, separator=" "):
    result = ""
    for i in range(len(words_list)):
        result += words_list[i]
        if i != len(words_list) - 1:  
            result += separator
    return result


txt = "გამარჯობა მე მიყვარს პროგრამირება"

print(my_split(txt))  

print(my_join(['გამარჯობა', 'მე', 'მიყვარს', 'პროგრამირება']))  


