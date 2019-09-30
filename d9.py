# n ээс m тоо хүртэлх тэгш тоонуудын тоог ол
n, m = [int(x) for x in input().split()]
ih = max(n,m)
baga = min(n,m)
too = 0
while ih >= baga:
    if ih % 2 == 0:
        print(ih)
        too +=1
    ih-=1
print( n, "ba", m, "hoorondoh tegsh toonuudyn too ni: ", too)