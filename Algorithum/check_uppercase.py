def find_upper_iterative(input_string):
    value = ""
    for i in input_string:
        if(i.isupper()):
            value +=i 
    return value

def find_upper_recursive(input_string,pos=0):
    if(input_string[pos].isupper()):
        return input_string[pos]
    if pos == len(input_string):
        return "No Uppercase character found"
    return find_upper_recursive(input_string,pos+1)

print(find_upper_recursive("amSsePS"))