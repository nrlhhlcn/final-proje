from Calisan import Calisan

class MaviYaka(Calisan):

    def __init__(self,isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas,yipranma_payi):
        super().__init__(isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas)
        self.__yipranma_payi=yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi
    def set_yipranma_payi(self,yipranma_payi):
        self.__yipranma_payi=yipranma_payi


    def __str__(self): 
        return f"--------------BİLGİLER--------------------\n" \
               f"isim:{self.get_isim()}\nsoyisim:{self.get_soyisim()}\nTecrübe:{self.get_tecrube()}\nYeni Maaş:{self.get_maas()+self.Zam_hakki()}"




