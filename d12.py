# Өгөгдсөн үгэнд а үсэг хэдэн удаа орсон байна вэ
ner = input()
urt= len(ner) -1
too = 0
k=0
while k<=urt:
    if ner[k] == 'a' or ner[k] == 'A':
        too+=1
    k+=1
print(too, "shirheg a useg bichigdsen baina")