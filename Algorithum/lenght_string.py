def length_iterative(input_string):
    count = 0
    for i in input_string:
        count += 1
    return count

def length_recursive(input_string,pos=0):
    if pos == len(input_string):
        return pos
    return length_recursive(input_string,pos+1)


print(length_iterative("pawanMandal"))
print(length_recursive("pawanmandal"))