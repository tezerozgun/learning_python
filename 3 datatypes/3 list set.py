#[O  Z  G  U  N  T  E  Z  E  R]
# 0  1  2  3  4  5  6  7  8  9
# 0 -9 -8 -7 -6 -5 -4 -3 -2 -1

liste=['o','z','g','u','n','t','e','z','e','r']
print(liste)
# liste= liste + 'f'
#bu komut calismaz liste tipindeki bir kumeye string ekleyemeyiz
liste2=['f']  
liste = liste+liste2
print(liste)
#veya
liste= liste +['f']
print(liste)
print(liste[0:15:2])
liste.append('g')
# append komutu yeni bir harf ekleyebiliyor
print(liste)
liste.pop()
print(liste)
#pop komutu son harfi cikariyor
liste.pop(5)
print(liste)
#pop 5. harfi atmami sagladi

#-------------------------------------------------------------------------------------
#sort siralamaya yariyor
sayilar =[3126454,16546,544467,1,1,314767498,487946,45,45]
print(sayilar.sort())
print(sayilar)

#reverse ters siralamaya yariyor
print(sayilar.reverse())
print(sayilar)

#-----------------------------------------------------------------------

#SET tekrarlayan ifadeleri atiyor
print(set(sayilar))
print(sayilar.sort())
