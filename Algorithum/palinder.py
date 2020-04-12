s = "Was it a cat I saw?"


#Method1
# Solution uses extra space proportional to size of string "s"
# s = ''.join([i for i in s if i.isalpha()]).replace(" ", "").lower()
# print(s == s[::-1])

#Method 2 check both side it take time logn
def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False 
        i += 1
        j -= 1
    return True


print(is_palindrome(s))