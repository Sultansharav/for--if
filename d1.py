# a ээс b хүртэлх тооний нийлбэр ол
a, b = [int(x) for x in input().split()]
ih = max(a,b)
baga = min(a,b)
niilber = 0
while ih >= baga:
    niilber += ih
    print(ih)
    ih-=1
print("niilber: ", niilber)