def func(lst, ind=0):
    if ind < len(lst):
        func(lst, ind+1)
        if lst[ind] % 2 != 0:
            lst.append(lst.pop(ind))
        i = 0
        if ind == 0:
            for x in lst:
                i=i+1
                if (x % 2 != 0):
                    sortEvenNumbers(lst, i-1)      
                    sortOddNumbers(i, len(lst), lst)
                    break
    return lst

def sortOddNumbers (index, length, lst):
    for y in range(index -1, length):
        for z in range(index-1, length):
            if (lst[z] > lst[y]):
                temp = lst[y]
                lst[y] = lst[z]
                lst[z] = temp   

def sortEvenNumbers(lst, length):
    for y in range(0, length):
        for z in range(0, length):
            if (lst[z]>lst[y]):
                temp = lst[y]
                lst[y] = lst[z]
                lst[z] = temp
    
input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(func(input))