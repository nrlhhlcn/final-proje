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
    def zam_hakki(self):
        try:
            if self.get_tecrube()<2:
                print("Tecrübeniz iki yıldan az olduğu için yeni maaşınız hesaplanmadi")
                return 0

            elif 2<=self.get_tecrube()<=4  and self.get_maas()<15000:
                zam_hakki=self.get_maas()%self.get_tecrube()
                yeni_maas=self.get_maas() +(self.get_maas()*zam_hakki)/100

                return yeni_maas

            elif self.get_tecrube()>4 and self.get_maas()<25000:
                zam_hakki = (self.get_maas() % self.get_tecrube())/2
                yeni_maas = self.get_maas() + (self.get_maas() * zam_hakki) / 100

                return yeni_maas

            else:
                return "hatalili giris"

        except ValueError:
            print("Hatalı veri girişi!")

    def __str__(self):
        return f"--------------BİLGİLER--------------------\n" \
               f"isim:{self.get_isim()}\nsoyisim:{self.get_soyisim()}\ntecrübe:{self.get_tecrube()}\nYeni Maaş:{+self.zam_hakki()}"



