print("""

1. Kayıt Ol

2. Giriş Yap

Programdan çıkış yapmak için direkt q 'ya basınız.


""")

while True:
    seçim = input("Alanı seçiniz : ")
    if(seçim  == "1"):
        kayıt_ad = input("Kayıt olmak için adınızı giriniz:")
        kayıt_soyad = input("Kayıt olmak için soyadınızı giriniz:")
        print("Kayıt oldunuz hoşgeldiniz {} {}".format(kayıt_ad,kayıt_soyad))
    if  (seçim == "2"):
        giriş_ad = input("Giriş olmak için adınızı giriniz:")
        giriş_soyad = input("Giriş olmak için soyadınızı giriniz:")
        print("Giriş oldunuz iyi eğlenceler {} {}".format(giriş_ad,giriş_soyad))
    if  (seçim == "q"):
        print("Programdan çıkış yapılıyor bir daha bekleriz :)")
        break