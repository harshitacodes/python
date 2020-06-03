def check_number(a,b):
    i = 0
    while i < len(list1):
        if list1[i] %  2 == 0:
            if list2 [i] % 2 == 0:
                print("dono even hai")
            else:
                print("even nhi hai")
        else:
            print("even nhi hai")            
        i = i + 1
list1=[12, 44, 45, 22, 9, 43, 56]
list2=[23, 42, 99, 114, 43, 76, 34]
check_number(list1,list2)