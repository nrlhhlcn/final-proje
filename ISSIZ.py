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
        
     def statü_bul(self):
        maks_etki = 0
        karar_statü = ""
        for statü, yıl in self.__tecrube.items():
            try:
                yıl = int(yıl)

                if statü == "Mavi Yaka":
                    etki = yıl / 5
                elif statü == "Meyaz Yaka":
                    etki = yıl * (35 / 100)
                elif statü == "yönetici":
                    etki = yıl * (45 / 100)

                if etki > maks_etki:
                    maks_etki = etki
                    karar_statü = statü
            except:
                return "Geçersiz bir yıl veya statü, lütfen tekrar deneyiniz."

        if karar_statü == "":
            return "Bilinmiyor ne olduğu"
        else:
            return karar_statü

    

    def __str__(self):
        return f"İSİM:{self.get_isim()}\nSOYİSİM:{self.get_soyisim()}\nSTATÜ:{self.statü_bul()}"



