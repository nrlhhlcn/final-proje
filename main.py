from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan     #KÜTÜPHANELERİ VE MODÜLLERİ DAHİL EDİYORUZ....!!!
from MaviYaka import MaviYaka
from BeyazYaka import Beyazyaka
import pandas as pd


                        #NESNELERİ OLUŞTURUYORUZ!!!
insan1=Insan("Nurullah","Hilcan",20,"Erkek👨","Türk",123456789)
insan2=Insan("Sude","Aktürk",20,"kız👩","Türk",987654321)

issiz1=Issiz("dwayne"," johnson",51,"erkek👨","ABD",987654321,7)
issiz2=Issiz("Angelina","Jolie",47,"kız👩","BD",12345678,4)
issiz3=Issiz("Hande","Erçel","29","kız👩","türk",12345678,3)


calisan1=Calisan("Murat","Boz",43,"erkek👨","Türk",123456789,"diğer",3,12000)
calisan2=Calisan("Elon","Musk",32,"Erkek👨","Güney Amerike",123456789,"Teknoloji💻",8,22000)
calisan3=Calisan("scarlett","johansson",38,"kız👩","ABD",123456789,"inşaat🏢",8,23000)



maviYaka1=MaviYaka("Demet","Mutlu",42,"Kız👩","Türk",987654321,"teknoloji💻",4,14000,0.2)
maviYaka2=MaviYaka("Acun","ılıcalı",53,"Erkek👨","Türk",123456789,"diğer",4,13000,0.5)
maviYaka3=MaviYaka("lionel","messi",53,"Erkek👨","arjantin",123456789,"diğer",4,11000,0.5)


beyazYaka1=Beyazyaka("dominic","toretto",55,"erkek👨","ABD",123456789,"diğer",5,14500,500)
beyazYaka2=Beyazyaka("tony","stark",55,"erkek👨","ABD",123456789,"muhasebe🧾",3,13000,1500)
beyazYaka3=Beyazyaka("fahriye","evcen",37,"kız👩","türk",9876543254,"muhasebe🧾",4,12000,2000)


veri={
    "NESNELER":["İnsan","İnsan","Çalışan","Çalışan","Çalışan","Mavi yaka","Mavi yaka","Mavi yaka","Beyaz yaka","Beyaz yaka","Beyaz yaka"],
    "T.C":[insan1.get_tc_numarsi(),insan2.get_tc_numarsi(),calisan1.get_tc_numarsi(),calisan2.get_tc_numarsi(),calisan3.get_tc_numarsi(),maviYaka1.get_tc_numarsi(),maviYaka2.get_tc_numarsi(),maviYaka3.get_tc_numarsi(),beyazYaka1.get_tc_numarsi(),beyazYaka2.get_tc_numarsi(),beyazYaka3.get_tc_numarsi()],
    "İSİM":[insan1.get_isim(),insan2.get_isim(),calisan1.get_isim(),calisan2.get_isim(),calisan3.get_isim(),maviYaka1.get_isim(),maviYaka2.get_isim(),maviYaka3.get_isim(),beyazYaka1.get_isim(),beyazYaka2.get_isim(),beyazYaka3.get_isim()],
    "SOYİSİM":[insan1.get_soyisim(),insan2.get_soyisim(),calisan1.get_soyisim(),calisan2.get_soyisim(),calisan3.get_soyisim(),maviYaka1.get_soyisim(),maviYaka2.get_soyisim(),maviYaka3.get_soyisim(),beyazYaka1.get_soyisim(),beyazYaka2.get_soyisim(),beyazYaka3.get_soyisim()],
    "YAS":[insan1.get_yas(),insan2.get_yas(),calisan1.get_yas(),calisan2.get_yas(),calisan3.get_yas(),maviYaka1.get_yas(),maviYaka2.get_yas(),maviYaka3.get_yas(),beyazYaka1.get_yas(),beyazYaka2.get_yas(),beyazYaka3.get_yas()],
    "CİNSİYET":[insan1.get_cinsiyet(),insan2.get_cinsiyet(),calisan1.get_cinsiyet(),calisan2.get_cinsiyet(),calisan2.get_cinsiyet(),maviYaka1.get_cinsiyet(),maviYaka2.get_cinsiyet(),maviYaka3.get_cinsiyet(),beyazYaka1.get_cinsiyet(),beyazYaka2.get_cinsiyet(),beyazYaka3.get_cinsiyet()],
    "UYRUK":[insan1.get_uyruk(),insan2.get_uyruk(),calisan1.get_uyruk(),calisan2.get_uyruk(),calisan3.get_uyruk(),maviYaka1.get_uyruk(),maviYaka2.get_uyruk(),maviYaka3.get_uyruk(),beyazYaka1.get_uyruk(),beyazYaka2.get_uyruk(),beyazYaka3.get_uyruk()],
    "SEKTÖR":[0,0,calisan1.get_sektor(),calisan2.get_sektor(),calisan3.get_sektor(),maviYaka1.get_sektor(),maviYaka2.get_sektor(),maviYaka3.get_sektor(),beyazYaka1.get_sektor(),beyazYaka2.get_sektor(),beyazYaka3.get_sektor()],
    "TECRÜBE":[0,0,calisan1.get_tecrube(),calisan2.get_tecrube(),calisan3.get_tecrube(),maviYaka1.get_tecrube(),maviYaka2.get_tecrube(),maviYaka3.get_tecrube(),beyazYaka1.get_tecrube(),beyazYaka2.get_tecrube(),beyazYaka3.get_tecrube()],
    "MAAŞ💵":[0,0,calisan1.get_maas(),calisan2.get_maas(),calisan3.get_maas(),maviYaka1.get_maas(),maviYaka2.get_maas(),maviYaka3.get_maas(),beyazYaka1.get_maas(),beyazYaka2.get_maas(),beyazYaka3.get_maas()],
    "YIPRANMA PAYI":[0,0,0,0,0,maviYaka1.get_yipranma_payi(),maviYaka2.get_yipranma_payi(),maviYaka3.get_yipranma_payi(),0,0,0],
    "TEŞVİK PRİMİ":[0,0,0,0,0,0,0,0,beyazYaka1.get_tesvik_primi(),beyazYaka2.get_tesvik_primi(),beyazYaka3.get_tesvik_primi()],
    "YENİ MAAŞ":[0,0,calisan1.zam_hakki()+calisan1.get_maas(),calisan2.zam_hakki()+calisan2.get_maas(),calisan3.zam_hakki(),maviYaka1.Zam_hakki()+maviYaka1.get_maas(),maviYaka2.Zam_hakki()+maviYaka2.get_maas(),maviYaka3.Zam_hakki()+maviYaka1.get_maas(),beyazYaka1.Zam_hakki()+beyazYaka1.get_maas(),beyazYaka2.Zam_hakki()+beyazYaka2.get_maas(),beyazYaka3.Zam_hakki()+beyazYaka3.get_maas()]

}

df=pd.DataFrame(veri,[1,2,3,4,5,6,7,8,9,10,11])

print(df)
onbes_ustu_maas=df[df["MAAŞ💵"]>15000]
print("*"*100,"\n")
print("Maaşı 15000 liranın üzerinde olan kişi sayısı",len(onbes_ustu_maas),"\n")
print("*"*100)

kucuk_df=df.sort_values("YENİ MAAŞ")
print("-"*20,"Yeni Maaşa göre sıralama","-"*20,"\n",kucuk_df)
print("*"*100)


print("*"*100)
print("-"*20,"TECRÜBESİ 3 YILDAN FAZLA OLAN BEYAZ YAKALILAR","-"*20)
tecrube_filtre = df[(df["TECRÜBE"] > 3) & (df["NESNELER"].str.contains("Beyaz yaka"))]
print(tecrube_filtre)
print("*"*100)


gruplandirma = df.groupby("NESNELER")
tecrube_ortalamasi = gruplandirma["TECRÜBE"].mean()
yeni_maas_ortalamasi = gruplandirma["YENİ MAAŞ"].mean()

print("-"*10,"Tecrübe Ortalamaları","-"*10)
print(tecrube_ortalamasi)
print("-"*10,"Yeni Maaş Ortalamaları","-"*10,"\n")
print(yeni_maas_ortalamasi)


yeni_df = df[["İSİM", "SOYİSİM", "SEKTÖR","MAAŞ💵"]]
print("-"*10,"İSİM, SOYİSİM, SEKTÖR ve YENİ MAAŞ'A GÖRE DATAFREME","-"*10)
print(yeni_df)
