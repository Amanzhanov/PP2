x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)
myfunc()
x = "Cool"
print("Python is " + x)