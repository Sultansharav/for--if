# n ээс m тоо хүртэлх сондгой тоонуудын тоог ол
n, m = [int(x) for x in input().split()]
ih = max(n,m)
baga = min(n,m)
while ih>=baga:
    if ih % 2 == 1:
        print(ih)
    ih-=1