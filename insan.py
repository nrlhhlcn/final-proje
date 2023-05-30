class Insan():#Insan isminde bir tane sınıf oluşturduk
    
    #init methodunu kullanarak gerekli özellikleri alıyoruz alıyoruz 
    def __init__(self,isim,soyisim,yas,cinsiyet,uyruk,tc_numarasi):
        self.__isim=isim
        self.__soyisim=soyisim
        self.__yas=yas
        self.__cinsiyet=cinsiyet
        self.__tc_numarasi=tc_numarasi
        self.__uyruk=uyruk

#Her özellik için get ve set fonsiyonları oluşturuyoruz...
#get fonsiyonları bize özellikleri döndürecek
#set fonsiyonları ise o özellikleri değşiştirmemizi sağlayacak
    def get_isim(self):
        return self.__isim
    def set_isim(self,isim):
        self.__isim=isim

    def get_soyisim(self):
        return self.__soyisim
    def set_soyisim(self,soyisim):
        self.__soyisim=soyisim

    def get_yas(self):
        return self.__yas
    def set_yas(self,yas):
        self.__yas=yas

    def get_cinsiyet(self):
        return self.__cinsiyet
    def set_cinsiyet(self,cinsiyet):
        self.__cinsiyet=cinsiyet

    def get_tc_numarsi(self):
        return self.__tc_numarasi
    def set_tc_numarsi(self,tc):
        self.__tc_numarasi=tc

    def get_uyruk(self):
        return self.__uyruk
    def set_uyruk(self,uyruk):
        self.__uyruk=uyruk

    def __str__(self):#str ile istenilen bilgileri konsol ekranına yazdırıyoruz
        print("-----------------------PERSONEL BİLGİLERİ------------------")
        return f"isim:{self.get_isim()}\nsoyisim:{self.get_soyisim()}\nyas:{self.get_yas()}\ncinsiyet:{self.get_cinsiyet()}\ntc:{self.get_tc_numarsi()}\nuyruk:{self.get_uyruk()}"







