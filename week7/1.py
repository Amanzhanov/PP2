mylist = list(map(int,input('Enter the array:\n').split()))
def multiple(*arr):
    first = 1
    for i in arr :
      first *= i
    return first
print(multiple(*mylist))
