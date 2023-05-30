from Calisan import Calisan #kütüphaneyi dahil ediyoruz

class MaviYaka(Calisan):#maviyaka adında sınıf oluşturuyoruz

    def __init__(self,isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas,yipranma_payi):
        super().__init__(isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas)
                ##super().__init__ methodu bizim calışan sınıfından bilgileri almamızı sağlıyor
        self.__yipranma_payi=yipranma_payi

    def get_yipranma_payi(self): #bu fonsiyon bize yipranma payinini döndürecek
        return self.__yipranma_payi
    def set_yipranma_payi(self,yipranma_payi):#bu fonsiyon yeni yıpranma payini eski yipranma payi ile değiştirmemizi sağlıyor
        self.__yipranma_payi=yipranma_payi
        
    def Zam_hakki(self):#bu fonksiyon çalışanın tecrübe, maaş ve yipranma payına göre yeni maaşını hesaplamamızı sağlıyor

        if 2<=self.get_tecrube()<=4 and self.get_maas()<15000:
            zam_hakki=(self.get_maas()%self.get_tecrube())/2+(self.get_yipranma_payi()*10)
            yeni_maas =  self.get_maas() * zam_hakki / 100


            return yeni_maas

        elif self.get_tecrube()>4 and self.get_maas()<25000:
            zam_hakki = (self.get_maas() %self.get_tecrube()) / 3 + (self.get_yipranma_payi() * 10)
            yeni_maas =  (self.get_maas() * zam_hakki) / 100


            return yeni_maas

    def __str__(self): #str methodu ile kullanıcını bilgilerini konsol  ekranını yazdırıyoruz.....
        return f"--------------BİLGİLER--------------------\n" \
               f"isim:{self.get_isim()}\nsoyisim:{self.get_soyisim()}\nTecrübe:{self.get_tecrube()}\nYeni Maaş:{self.get_maas()+self.Zam_hakki()}"




