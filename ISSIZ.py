from Insan import Insan
class Issiz(Insan):
    def __init__(self,isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,tecrube):
        super().__init__(isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi)
        self.__tecrube=tecrube


    def  get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self,tecrube):
        self.__tecrube=tecrube
        self.statu=self.statü_bul()

    

    def __str__(self):
        return f"İSİM:{self.get_isim()}\nSOYİSİM:{self.get_soyisim()}\nSTATÜ:{self.statü_bul()}"



