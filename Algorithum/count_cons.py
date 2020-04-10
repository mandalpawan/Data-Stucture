#Method 1
def count_cons(input_string):
    count = len(input_string)
    string = "aeiou"
    for i in input_string:
        for j in string:
            if(i.lower()==j.lower()):
                count -=1
    return count

#Method 2
def count_const_iterative(input_string):
    count = 0
    vowel = "aeiou"
    for i in range(len(input_string)):
        if input_string[i].lower() not in  vowel and input_string.isalpha():
            count += 1
    return count

def recursive_count_consonants(input_str):
    vowels = "aeiou"
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])
    
    

print(count_cons("symanWA"))
print(count_const_iterative("symanWA"))
print(recursive_count_consonants("symanWA"))