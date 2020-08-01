






print("Enter no of elements")
n=int(input())
a=[];b=[]

for i in range(n):
    el=int(input())
    a.append(el)
    if el not in b:
        b.append(el)
        

c=sorted(b,reverse=False)
print("The Runnerup/Secod Maximum value: "+str(c[len(c)-2]))
