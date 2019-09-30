# Өгүүлбэрийн үгүүдээс b үсгийг хас
ner = input()
urt = len(ner) - 1
k = 0
shine=""
while k<=urt:
    if ner[k] != 'b' and ner[k] != 'B':
        shine += ner[k]
    k+=1
print(shine)