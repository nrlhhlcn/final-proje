from Insan import Insan#kütüphaneyi dahil ediyoruz
class Issiz(Insan):#Issiz adında sınıf oluşturuyoruz
    def __init__(self,isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi,tecrube):
        super().__init__(isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi)
        # init methodunu kullanarak gerekli özellikleri alıyoruz alıyoruz
        self.__tecrube=tecrube

    # Her özellik için get ve set fonsiyonları oluşturuyoruz...
    # get fonsiyonları bize özellikleri döndürecek
    # set fonsiyonları ise o özellikleri değşiştirmemizi sağlayacak
    def  get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self,tecrube):
        self.__tecrube=tecrube
        self.statu=self.statü_bul()

    def statü_bul(self):#çalışana en uygun statüyü buluyoruz
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

    def __str__(self):#str ile bilgileri ekrana yazdırıyoruz
        return f"İSİM:{self.get_isim()}\nSOYİSİM:{self.get_soyisim()}\nSTATÜ:{self.statü_bul()}"





