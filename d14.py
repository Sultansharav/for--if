# Өгөгдсөн тооны цифрүүдийн нийлбэрийг ол print(sum(int(i) for i in str(input())))
n = input()
k = len(n) - 1
niilber = 0
while k>=0:
    niilber += int(n[k])
    k-=1
print("Tsifruudiin niilber ni: ", niilber)