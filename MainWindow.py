# Burada yapılan işlemler, bir arayüz oluşturmaya yaramaktadır.
# Arayüzün içerisinde oluşan tıklama olayı(toplama-çıkarma-çarpma-bölme)
# Ekranda görünecek şekilde bu kod bloğundan çıkmaktadır. 
# Kodların içerisindeki isimlendirme durumları da tamamen bununla bağlantılıdır. 


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 61, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 61, 41))
        self.label_2.setObjectName("label_2")
        self.txt_sayi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(80, 100, 200, 32))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.txt_sayi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(80, 50, 200, 32))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.btn_topla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_topla.setGeometry(QtCore.QRect(100, 150, 61, 41))
        self.btn_topla.setObjectName("btn_topla")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(170, 150, 61, 41))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(240, 150, 61, 41))
        self.btn_carpma.setObjectName("btn_carpma")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(310, 150, 61, 41))
        self.btn_bolme.setObjectName("btn_bolme")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(110, 220, 141, 31))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sayı 1:"))
        self.label_2.setText(_translate("MainWindow", "Sayı 2:"))
        self.btn_topla.setText(_translate("MainWindow", "Toplama"))
        self.btn_cikarma.setText(_translate("MainWindow", "Çıkarma"))
        self.btn_carpma.setText(_translate("MainWindow", "Çarpma"))
        self.btn_bolme.setText(_translate("MainWindow", "Bölme"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Sonuç: "))
