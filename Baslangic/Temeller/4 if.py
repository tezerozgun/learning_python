dolar_kuru = 29
if dolar_kuru < 30:
    print('Dolar dustu')
elif dolar_kuru == 30:
    print('Dolar sabit')    
else :
    print('Dolar yukseldi')



hava_durumu = 'Gunesli'
if hava_durumu == 'Yagmurlu':
    print('Semsiyeni al')
elif hava_durumu == 'Karli':
    print('Siki giyin')
elif hava_durumu == 'Ruzgarli':
    print('Siki giyin')
else:
    print('Sorun yok')


liste=['o','z','g','u','n','t','e','z','e','r']
hedef_harf = 'e'
if hedef_harf in liste:
    print('Isminizde e harfi var')
else:
    print('Isminizde e harfi yok') 

liste2=['i','l','a','y','d','a','c','i','n', 'a','r']
hedef_harf2 = 'ozgun'
if hedef_harf2 in liste2:
    print('Ozgunu seviyorsun')
else:
    liste2.append('Ozgun')
    print('Ozgunu seviyorsun')
    print('Ilayda Ozgunu {}'.format('Seviyor'))

fenerbahce_durumu = '1.sirada'
fenerbahce_durum2 = 'Sampiyon'
if fenerbahce_durumu in '1.sirada' and 'Sampiyon':
    print('Fenerbahce Sampiyon')
else:
    print('Fenerbahce Sampiyon degil')