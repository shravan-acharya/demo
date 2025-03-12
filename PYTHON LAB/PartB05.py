tuple1=()
print("Empty tuple:",tuple)

tuple1=("Apple")
print("\nIn Tuple string is:",tuple1)

tuple=("Apple")
print("\nIn tuple with one item:\n",tuple)
print(type(tuple))

tuple_constructor=("Apple","Banana")
print("\nIn Constructor tuple:",tuple_constructor)

tuple='python'
print("\nIn tuple without parameter:",tuple)
print(type(tuple))

tuple=('Apple','Banana','orange','Grapes','Apple')
name=tuple.count('Apple')
print("\nIn count tuple:",name)

tuple=(1,2,3,4,5)
num=tuple.index(3)
print("\nIn index of given value:",num)

tuple=("Apple")
name=len(tuple)
print("\nIn length of a tuple:",name)

tuple1=(0,1,2,3)
tuple2=('Apple','Banana','Graphs')
tuple3=tuple1+tuple2

print("\nIn tuple after concatenation:")
print(tuple3)

tuple1=(0,1,2,3)
print("\nIn tuple with string:")
print(tuple1[1:1])
print(tuple1[::-1])
print(tuple1[2:4])
