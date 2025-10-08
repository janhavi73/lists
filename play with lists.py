L=[4,5,1,2,9,7,10,8]
print("orginal list: ",L)
count=0
for i in L:
    count+=i

avg=count/len(L)    

print("sum =", count)
print("average = ", avg)

L.sort()
print("smallest value is: ",L[0])
print("largest value is: ",L[-1])


