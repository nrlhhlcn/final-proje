from Insan import Insan
class Calisan(Insan):
    def __init__(self,isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas):
        super().__init__(isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi)
        self.__sektor=sektor
        self.__tecrube=tecrube
        self.__maas=maas
    def get_sektor(self):
        return self.__sektor
    def set_sektor(self,sektor):
        self.__sektor=sektor
    def get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self,tecrube):
        self.__tecrube=tecrube
    def get_maas(self):
        return self.__maas
    def set_maas(self,maas):
        self.__maas=maas
    

    def __str__(self):
        return f"--------------BİLGİLER--------------------\n" \
               f"isim:{self.get_isim()}\nsoyisim:{self.get_soyisim()}\ntecrübe:{self.get_tecrube()}\nYeni Maaş:{+self.zam_hakki()}"



