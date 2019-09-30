# a тоог b зэрэгт дэвшүүл
a, b = [int(x) for x in input().split()]
n = 1
while b>0:
    n=n*a
    b-=1
print(n)