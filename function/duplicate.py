def duplicate(n):
    duplicate_list=[]
    i=0
    while i < len (n):
        j=i+1
        while j < len (n):
            if n[i]==n[j]:
                a=n[i]
                if a not in duplicate_list:
                    duplicate_list.append(a)
            j=j+1
        i=i+1
    return duplicate_list
string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
print(duplicate(string_list))