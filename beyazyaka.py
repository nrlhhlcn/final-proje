from Calisan import Calisan#kütüphaneyi dahil ediyoruz
class Beyazyaka(Calisan):# beyaz yaka adında bir sınıf oluşturuyoruz ....
    def __init__(self,isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas,tesvik_primi):
        super().__init__(isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas)
        ##super().__init__ methodu bizim calışan sınıfından bilgileri almamızı sağlıyor

        self.__tesvik_primi=tesvik_primi

    def get_tesvik_primi(self): #bu fonksiyon bize teşvif primini döndüreccek
        return self.__tesvik_primi

    def set_tesvik_primi(self,tesvik_primi):# bu fonsiyon bize yeni teşvik primini eski teşvik primi ile değişmemizi sağlıyor
        self.__tesvik_primi=tesvik_primi

     def Zam_hakki(self):#bu fonksiyon çalışanın tecrübesi,maaşı ve teşvik primine göre yeni maaş hesaplamamızı sağlıyor
        if 2<=self.get_tecrube()<=4 and self.get_maas()<15000:
            zam_hakki=(self.get_maas()%self.get_tecrube())*5+self.get_tesvik_primi()

            return zam_hakki
        elif self.get_tecrube()>4 and self.get_maas() <25000:
            zam_hakki=(self.get_maas()%self.get_tecrube())*4+self.get_tesvik_primi()
            return zam_hakki
        
     
    def __str__(self): #str ile istenilen bilgileri konsol ekranına yazdırıyoruz
        return f"--------------BİLGİLER--------------------\n" \
               f"isim:{self.get_isim()}\nsoyisim:{self.get_soyisim()}\nTecrübe:{self.get_tecrube()}\nYeni Maaş:{self.get_maas()+self.Zam_hakki()}"


