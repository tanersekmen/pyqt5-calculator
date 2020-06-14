# Kütüphaneler ve içerisinden alınan fonksiyonlar

from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow 

class HesapMakinesi(QtWidgets.QMainWindow): #Ana class ataması yaptığım yer

    def __init__(self):
        super(HesapMakinesi,self).__init__()
        #Buton Tıklama İşlemleri yapılacak olan Kodlar

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_topla.clicked.connect(self.toplama)
        self.ui.btn_cikarma.clicked.connect(self.cikarma)
        self.ui.btn_carpma.clicked.connect(self.carpma) 
        self.ui.btn_bolme.clicked.connect(self.bolme)



    def toplama(self):  # toplama işlevi için oluşturulan definition
        result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text()) # öncelikle sayı 1 ve sayı 2 kısımlarını text dosyası ile alıyoruz sonrasında da int komutu ekliyoruz. Sayı değeri taşıması için
        self.ui.lbl_sonuc.setText('sonuç: ' + str(result)) # result olarak alınan değeri sonuç kısmına yazdırmak için bu metodu kullanıyoruz.

    def cikarma(self):# çıkarma işlevi için oluşturulan definition
        result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text()) # öncelikle sayı 1 ve sayı 2 kısımlarını text dosyası ile alıyoruz sonrasında da int komutu ekliyoruz. Sayı değeri taşıması için
        self.ui.lbl_sonuc.setText('sonuç :' + str(result)) #  result olarak alınan değeri sonuç kısmına yazdırmak için bu metodu kullanıyoruz.

    def bolme(self): # bölme işlevi için oluşturulan definition
        result = int( self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text()) # öncelikle sayı 1 ve sayı 2 kısımlarını text dosyası ile alıyoruz sonrasında da int komutu ekliyoruz. Sayı değeri taşıması için
        self.ui.lbl_sonuc.setText('sonuç : ' + str(result)) #  result olarak alınan değeri sonuç kısmına yazdırmak için bu metodu kullanıyoruz.

    def carpma(self):  # çarpma işlevi için oluşturulan definition
        result=int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text()) #  öncelikle sayı 1 ve sayı 2 kısımlarını text dosyası ile alıyoruz sonrasında da int komutu ekliyoruz. Sayı değeri taşıması için
        self.ui.lbl_sonuc.setText('sonuç : ' + str(result) ) #  result olarak alınan değeri sonuç kısmına yazdırmak için bu metodu kullanıyoruz.


    
def app(): # uygulama çalıştırmak için def app tanımlıyoruz
    app= QtWidgets.QApplication(sys.argv) # uygulama başlatma komutu ile def kısmını bağlıyoruz
    win=HesapMakinesi() # tanımladığımız mainform class'ını burada win komutu ile eşleştiriyoruz.
    win.show() # win kısmının görünmesi için 'show' metodunu kullanıyoruz
    sys.exit(app.exec_()) # sys.exit ile uygulama sonrasında çıkmak istediğimizde çarpı ile cıkıyoruz


app() #app() çağırarak uygulama çalıştırma fonksiyonunu ekranda oluşturuyoruz.
