n = int(input())
def check(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0 :
         print(i)
check(n)