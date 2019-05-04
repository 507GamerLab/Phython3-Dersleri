# python'da listeleri belirlemek için [] işareti kullanılır
l=[11,22,33,"Tayfun"]

print(l)

l1=[12,23,45,"Yakut"]

print(l1)

print(l[0]) # listelerdeki indeksleme 0'dan başlar
# print(l[0]) komutunu yazarsak l listesinin 0. elemanını ekrana yazdırır

print(l[:3]) # :3 yazarsak 3. elemana kadar (3. eleman hariç) olanları sıralar

print(len(l)) # bir listenin uzunluğu len komutu ile bulunabilir

öğrenci=["Tayfun", "Yakut", "29", "1.78"]

print(öğrenci)

print(öğrenci[1])

öğrenci[0]="TYFN"

print(öğrenci[0]) # öğrenci listesinde ki 0. elemanı TYFN ile değiştirip ekrana basabiliyorum

öğrenci.append("Python")

print(öğrenci) # .append ile listeye bir eleman ekleyebiliriz

öğrenci=öğrenci+["Bir başka ekleme metodu"]

print(len(öğrenci))

print(öğrenci)

öğrenci[:2]=["tayfun","YKT"]

print(öğrenci) # :2 ile listenin ilk iki elemanını değiştirebilir

öğrenci[:2]=[]                # ya da silebiliriz

print(öğrenci)











