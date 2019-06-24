# no-of-spl-chtrs
i=input()
count=0
for x in range(len(i)):
    if(i[x].isdigit() or i[x].isalpha() or i[x]==(' ')):
        continue
        
    
    else:
        count+=1
print(count)
