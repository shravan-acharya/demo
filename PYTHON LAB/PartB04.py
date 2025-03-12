a={'name':'Nisha','age':19}
print(a)
#len
print("\n length of a given dictionary:")
print(len(a))
#keys
print("\n dictionary keys:")
print(a.keys())
#Values
print("\n dictionary value:")
print(a.values())
#items
print("\n dictionary items:")
print(a.items())
#membership
b='name' in a
membership='name' in a
print(membership)
#get
print(a.get('name'))
print(a.get('address'))
#Set default
print(a.setdefault('address','ckm'))
#copy
m={'fruit':'apple','color':'red'}
copy=m.copy()
print(copy)
#get
get=m.get('fruit')
print(get)
#item
item=m.items()
print("\n dictionary items:")
print(item)
#pop
pop=m.pop('color')
print("\n poped value:")
print(pop)
#keys
keys=m.keys()
print(keys)
fromkey=dict.fromkeys(m)
print(fromkey)
