from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow 


class HesapMakinesi(QtWidgets.QMainWindow): 

    def __init__(self):
        super(HesapMakinesi,self).__init__()
        #Buton tıklama işlemleri yapılacak olan kodlar ve arayüz.

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_topla.clicked.connect(self.toplama)
        self.ui.btn_cikarma.clicked.connect(self.cikarma)
        self.ui.btn_carpma.clicked.connect(self.carpma) 
        self.ui.btn_bolme.clicked.connect(self.bolme)



    def toplama(self): 
        result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text()) # toplama işlmeminin yapıldığı dizin 
        self.ui.lbl_sonuc.setText('sonuç: ' + str(result)) 

    def cikarma(self):
        result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text()) # çıkarma işlemini yaptığım dizin
        self.ui.lbl_sonuc.setText('sonuç :' + str(result)) 

    def bolme(self):
        result = int( self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text()) # bölme işlemi lokasyonu
        self.ui.lbl_sonuc.setText('sonuç : ' + str(result)) 

    def carpma(self): 
        result=int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text()) # çarpma işlemi yapılan dizin
        self.ui.lbl_sonuc.setText('sonuç : ' + str(result) ) 


# uygulama çalıştırmak için app tanımlıyoruz   
def app(): 
    app= QtWidgets.QApplication(sys.argv)
    win=HesapMakinesi() 
    win.show() #
    sys.exit(app.exec_()) 


app() 
