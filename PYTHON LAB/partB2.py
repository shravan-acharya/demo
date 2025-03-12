num=[]
print("Enter 10 elements for the list:")
for i in range(10):
    num.append(int(input()))
for i in range(9):
    chk=0
    small=num[i]
    for j in range(i+1,10):
        if small>num[j]:
            small=num[j]
            chk=chk+1
            index=j
    if chk!=0:
        temp=num[i]
    num[i]=small
    num[index]=temp
print("\n Sorted list is:")
for i in range(10):
    print(num[i])
    
