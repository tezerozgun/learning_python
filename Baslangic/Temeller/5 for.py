isim = 'Ozgun Tezer'
for harfler in isim:
    print(harfler)
#range fonksiyonu 2 deger arasindaki degerleri verir
for i in range(1,17,2):
    print(i)

#2 uzeri 10 hesaplama
sonuc = 1
for i in range(0,10):
    sonuc *= 2
print(sonuc)

liste1 =['a','b','c']
liste2 =[1,2,3]

#ic ice dongu
for harf in liste1:
    for rakam in liste2:
        print(rakam,harf)

#break continue
liste =[1,2,3,4,5,6,7,8,9]
for i in liste:
    if i==3:
        print('3 listeye dahil degil')
        continue
    print(i)

for i in liste:
    if i == 5:
        break
    print(i)

liste3 = range(100)
for i in liste3:
    if i%3 != 0:
        continue
    print(i)
    if i==75:
        break   

isim = ['Ozgun Tezer','Ilayda Cinar','Ozgun','Ilayda']
for i in isim:
    print(i)

kullanici_sayisi = 0

for kullanici in kullanici_sayisi:
    kullanici_sayisi = kullanici_sayisi + 1
    print(kullanici_sayisi , kullanici)









