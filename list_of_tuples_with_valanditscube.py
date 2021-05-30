def val_and_cube(n):
  res=[(i,pow(i,3)) for i in range(1,n+1)]
  return res
n=int(input())
print(val_and_cube(n))
