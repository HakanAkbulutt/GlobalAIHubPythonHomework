isim = input("Isminiz:")
soyisim = input("Soyisminiz: ")
yas = int(input("Yasiniz:"))
dogumYili = int(input("Dogum Yiliniz:"))

liste = [isim, soyisim, yas, dogumYili]

for i in liste:
  print (i)
if yas <18:
  print("Yasiniz 18'den kucuk oldugu icin disari cikmak sizin icin tehlikelidir!!!")
else:
    print("Disari Cikabilirsiniz..")