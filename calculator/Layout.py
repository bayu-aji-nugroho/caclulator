from PyQt5.QtWidgets import  QMainWindow, QPushButton,QLabel
from PyQt5 import uic
from logic import operation



class layout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.operasi = operation()
        uic.loadUi("mycalculator_project.ui",self)
        self.definition()
        self.click()
        self.show()

    def definition(self):
        self.label = self.findChild(QLabel,name="label")
        tombol1 = self.findChild(QPushButton,name="tombol1")
        tombol2 = self.findChild(QPushButton,name="tombol2")
        tombol3 = self.findChild(QPushButton,name="tombol3")
        tombol4 = self.findChild(QPushButton,name="tombol4")
        tombol5 = self.findChild(QPushButton,name="tombol5")
        tombol6 = self.findChild(QPushButton,name="tombol6")
        tombol7 = self.findChild(QPushButton,name="tombol7")
        tombol8 = self.findChild(QPushButton,name="tombol8")
        tombol9 = self.findChild(QPushButton,name="tombol9")
        tombol0 = self.findChild(QPushButton,name="tombol0")
        tombolplus = self.findChild(QPushButton,name="tombolplus")
        tombolminus = self.findChild(QPushButton,name="tombolminus")
        tombolkali = self.findChild(QPushButton,name="tombolkali")
        tombolbagi = self.findChild(QPushButton,name="tombolbagi")
        tombolce = self.findChild(QPushButton,name="tombolce")
        tombolsamadengan = self.findChild(QPushButton,name="tombolequ")
        tombolkurang = self.findChild(QPushButton,name="tombol9_3")
        self.child = {tombol0:0,tombol1:1,tombol2:2,
                      tombol3:3,tombol4:4,tombol5:5,
                      tombol6:6,tombol7:7,tombol8:8,
                      tombol9:9,tombolplus:"+",tombolminus:"-",
                      tombolkali:"x",tombolbagi:"/",tombolce:"CE",
                      tombolsamadengan:"=",tombolkurang:"<-"}


    def onclick(self,value):
        self.operasi.onclick(value)
        self.label.setText(f"{self.operasi.valueInLabel}")

    def click(self):
        for i in (self.child):
            i.pressed.connect(lambda i=i: self.onclick(self.child.get(i)))



