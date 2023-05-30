from Calisan import Calisan
class Beyazyaka(Calisan):
    def __init__(self,isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas,tesvik_primi):
        super().__init__(isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,sektor,tecrube,maas)


        self.__tesvik_primi=tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self,tesvik_primi):
        self.__tesvik_primi=tesvik_primi


    def __str__(self): 
        return f"--------------BİLGİLER--------------------\n" \
               f"isim:{self.get_isim()}\nsoyisim:{self.get_soyisim()}\nTecrübe:{self.get_tecrube()}\nYeni Maaş:{self.get_maas()+self.Zam_hakki()}"


