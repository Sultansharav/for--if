# n ээс m тоо хүртэлх сондгой тооны нийлбэр ол
n, m = [int(x) for x in input().split()]
ih = max(n,m)
baga = min(n,m)
niilber = 0
while ih >= baga:
    if ih % 2 == 1:
        print(ih)
        niilber+=ih
    ih-=1
print(niilber)