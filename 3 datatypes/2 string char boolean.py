stringvar = 'Python'
print(stringvar)

# INDEX ALMA
# P  Y  T  H  O  N
# 0  1  2  3  4  5
# 0 -5 -4 -3 -2 -1

print(stringvar[3])
print(stringvar[-6])
#belli bir yerden belli bir yere kadar almak icin de;
print(stringvar[2:])
print(stringvar[:-2])
print(stringvar[0:3])
#[] tek bir elemanin indexi alinir
#[:]bir elemandan sonrakiler alinir
#[x:x] x`ten x`e kadar olanlar alinir
#ilk kisim icerir ikinci kisim parantezde icermez.

#[x:x:x] baslangic ve bitis arasindaki degeler 3. degere gore atlayarak devam eder
print(stringvar[0:4:2])
#0`dan 4`e kadar ikiserli al. PYTHON p ve t icerir

stringtest = 'ozguntezer'
print(stringtest[0:8])   #ozguntez
print(stringtest[0:9:3]) #oue
print(stringtest[0:10:3]) #ouer

#---------------------------------------------------------------------------------------
print(len(stringtest))
print(len(stringvar))
#len komutu uzunluk 

#---------------------------------------------------------------------------------------
#concatenation(birlestirme yontemi)

print(stringvar + stringtest)
stringvar = stringvar + stringtest
print(stringvar)

#---------------------------------------------------------------------------------------

#BUYUK KUCUK HARF VE AYIRMA
print(stringvar.upper())
print(stringvar.lower())
print(stringvar.split())
print(stringvar.split('t'))
#t`den sonrakileri ayir

#---------------------------------------------------------------------------------------

#BOOLEAN

a = True
b = False
c = 'True'   #tirnak icinde olursa string ciktisi ayni islev farkli
print(type(a))
print(type(c))
print(b)

yas = 18
print(yas > 20)
print(yas < 20)
print(yas==18)