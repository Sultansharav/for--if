# Өгөгдсөн тооны хуваагчдыг ол
n = int(input())
s = n
while n>0:
    if s % n == 0:
        print(n)
    n-=1