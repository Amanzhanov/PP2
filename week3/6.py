def myfunc(n):
  return lambda a : a * n

m1 = myfunc(2)
m2 = myfunc(3)
print(m1(11))
print(m2(11))
print(myfunc(5)(11))