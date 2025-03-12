import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[30,56,37,57,99]
plt.bar(x=x,height=y,width=0.4)
plt.xticks(x,(1,2,3,4,5))
y2=[i+1 for i in y]
plt.title("abc company")
plt.plot(x,y2,color="black")
plt.scatter(x,y)
plt.xlabel("year")
plt.ylabel("Stock")
plt.show()
