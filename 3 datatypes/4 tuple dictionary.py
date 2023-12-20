#tuple listten farkli olarak degerlerini degistiremeyiz atama yaparak

liste=['o','z','g','u','n','t','e','z','e','r']
print(liste)
tuple=('o','z','g','u','n','t','e','z','e','r')
print(tuple)

liste[0] = 12354
print(liste[0])
# a`yi 12354`e atadik
#ama tuple da bu degeri degistiremiyoruz.
#tuple[0]= 123 gecersiz ve hata verecek

print(tuple.count('e'))
#tuple kumesinde kac defa e var say dedik
print(tuple.count(0))

#index sorgu
print(tuple.index('g'))
print(tuple.index('e'))

#--------------------------------------------------------------------------------

dictionary1 = {
    'isim' : 'Ozgun',
    'yas': 19,
    'dogdugu_sehir':'Akhisar',
    'yasadigi_sehir':'varsova'}
print(dictionary1)
dictionary2 = {
    'isim' : 'Ozgun',
    'yas': 19,
    'lokasyon':{
        'dogdugu_sehir': 'Akhisar',
        'yasadigi_sehir': 'Varsova'}}
print(dictionary2)

print(dictionary2['yas'])
print(dictionary2['lokasyon']['yasadigi_sehir'])

#koseli parantez kullanmadan get ile de deger alinabilir
print(dictionary2.get('yas'))
print(dictionary2.get('lokasyon').get('yasadigi_sehir'))


print(dictionary2.keys())
print(dictionary2.values())
print(dictionary2.items())





