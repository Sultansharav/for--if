# Өгөгдсөн тооны хуваагчдын тоог ол
n = int(input())
s = n
too = 0
while n>0:
    if s % n ==0:
        print(n)
        too+=1
    n-=1
print("Huvaagchdiin too ni: ", too)