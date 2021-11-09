t=(1,2,3,4,5,6,7,8,9)
e=0
o=0
for i in range(0,len(t)):
    if i%2==0:
        e+=1
    else:
        o+=1
print("Number of even numbers :",e)
print("Number of odd numbers :",o)
