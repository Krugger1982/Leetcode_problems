lists = [None, [1, 2, 3], None]

for i in range(len(lists)-1, -1, -1):
    if lists[i] is None:
        lists.pop(i)
        
                
print( lists )

