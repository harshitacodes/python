def list_change(a,b):
    i = 0
    new_list=[]
    while i < len(a):
        add_number = a[i] * b[i]
        new_list.append(add_number)
        i = i + 1
    return new_list
multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
print(multiple_list)