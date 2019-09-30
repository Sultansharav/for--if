# a болон b тооны үржвэр ол
a, b=[int(x) for x in input().split()]
n = 0
while b > 0:
    n+=a
    b-=1
print(n)