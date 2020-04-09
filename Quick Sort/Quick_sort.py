def Quick_sort(sequence):
    if len(sequence)<=1:
        return sequence
    else:
        pivot = sequence.pop()
    item_greater = []
    item_less = []

    for item in sequence:
        if item > pivot:
            item_greater.append(item)
        else:
            item_less.append(item)

    return Quick_sort(item_less) + [pivot] + Quick_sort(item_greater)


print(Quick_sort([5,4,8,9,6,2,5,1,5,3]))


