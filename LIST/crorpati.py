kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
crorpati=0
lakhpati=0
dilwale=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>10000000:
        crorpati=crorpati+1
    elif 10000000>kitna_paisa_hai[i]>100000:
        lakhpati=lakhpati+1
    else:   
        dilwale=dilwale+1
    i=i+1
print(crorpati,"crorpati")
print(lakhpati,"lakhpati")
print(dilwale,"dilwale")