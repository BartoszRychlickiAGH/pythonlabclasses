import sys
import numpy as np # do pierwiastka
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
)  # importowanie bibliotek przyciskow PushButton, textbox...


class App(QWidget):
    def __init__(self): # konstruktor główny
        super().__init__() # konstruktor - wywołuje klase QWidget
        self.title = "Kalkulator"
        self.left = 100
        self.top = 100
        self.width = 900
        self.height = 700
        ##################################
        self.a = 1  # wskażnik dodawania
        self.number = 0
        self.live_number = ""

        layout0 = QVBoxLayout()  # definicje layoutów do pozycjonowania przyciskow
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()

        
        
      
        self.textbox = QLineEdit()  # deklaracja textboxa
        self.button0 = QPushButton(
            " 0 ", self
        )  # deklaracja poszczególnych przyciskow z tytułami odpowiednimi do ich funkcji
        self.button1 = QPushButton(" 1 ", self)
        self.button2 = QPushButton(" 2 ", self)
        self.button3 = QPushButton(" 3 ", self)
        self.button4 = QPushButton(" 4 ", self)
        self.button5 = QPushButton(" 5 ", self)
        self.button6 = QPushButton(" 6 ", self)
        self.button7 = QPushButton(" 7 ", self)
        self.button8 = QPushButton(" 8 ", self)
        self.button9 = QPushButton(" 9 ", self)
        self.button10 = QPushButton(" + ", self)
        self.button11 = QPushButton(" - ", self)
        self.button12 = QPushButton(" / ", self)
        self.button13 = QPushButton(" = ", self)
        self.button14 = QPushButton(" + / - ", self)
        self.button15 = QPushButton("  ", self)
        self.button16 = QPushButton(" √ ", self)
        self.button17 = QPushButton(" * ", self)
        self.button18 = QPushButton(" C ", self)
        self.button19 = QPushButton(" . ", self)

        self.button0.clicked.connect(self.On_click0)    # ustawia co się dzieje wykonuje po wciśnięciu przycisku 
        self.button2.clicked.connect(self.On_click2)
        self.button3.clicked.connect(self.On_click3)
        self.button4.clicked.connect(self.On_click4)
        self.button5.clicked.connect(self.On_click5)
        self.button6.clicked.connect(self.On_click6)
        self.button7.clicked.connect(self.On_click7)
        self.button8.clicked.connect(self.On_click8)
        self.button9.clicked.connect(self.On_click9)
        self.button10.clicked.connect(self.Summing)
        self.button13.clicked.connect(self.Calculate)
        self.button18.clicked.connect(self.Reset)
        self.button11.clicked.connect(self.Sub)
        self.button17.clicked.connect(self.Multiply)
        self.button12.clicked.connect(self.Dividing)
        self.button14.clicked.connect(self.Sign)
        self.button19.clicked.connect(self.Point)
        self.button16.clicked.connect(self.Square)

        layout0.addWidget(self.textbox)  # dodawanie przycisków do poszczególnych layoutów
        layout2.addWidget(self.button18)
        layout2.addWidget(self.button16)
        layout2.addWidget(self.button15)
        layout2.addWidget(self.button13)
        layout1.addWidget(self.button1)
        layout1.addWidget(self.button2)
        layout1.addWidget(self.button3)
        layout1.addWidget(self.button10)
        layout3.addWidget(self.button4)
        layout3.addWidget(self.button5)
        layout3.addWidget(self.button6)
        layout3.addWidget(self.button11)
        layout4.addWidget(self.button7)
        layout4.addWidget(self.button8)
        layout4.addWidget(self.button9)
        layout4.addWidget(self.button17)
        layout5.addWidget(self.button14)
        layout5.addWidget(self.button0)
        layout5.addWidget(self.button19)
        layout5.addWidget(self.button12)

        layout0.addLayout(layout2)  # dodawanie layoutów do layouta głównego
        layout0.addLayout(layout1)
        layout0.addLayout(layout3)
        layout0.addLayout(layout4)
        layout0.addLayout(layout5)

        self.setWindowTitle(self.title)  # konfiguracja okna
        self.setGeometry(self.left, self.top, self.height, self.width)
        self.setLayout(layout0)
        self.show()


    # MEtody klasy App
    def On_click0(self):
        
        self.live_number += "0" 
        self.textbox.setText(self.live_number)

    def On_click1(self):
        
        self.live_number = self.live_number + "1" 
        self.textbox.setText(self.live_number)

    def On_click2(self):
        
        self.live_number += "2" 
        self.textbox.setText(self.live_number)

    def On_click3(self):
        
        self.live_number += "3" 
        self.textbox.setText(self.live_number)

    def On_click4(self):
        
        self.live_number += "4" 
        self.textbox.setText(self.live_number)

    def On_click5(self):
        
        self.live_number += "5" 
        self.textbox.setText(self.live_number)

    def On_click6(self):
        
        self.live_number += "6" 
        self.textbox.setText(self.live_number)

    def On_click7(self):
        
        self.live_number += "7" 
        self.textbox.setText(self.live_number)

    def On_click8(self):
        
        self.live_number += "8" 
        self.textbox.setText(self.live_number)

    def On_click9(self):
        
        self.live_number += "9" 
        self.textbox.setText(self.live_number)
    # Alert dzielenia prze z0
    def MessageBox(self):  # metoda wyświetlająca warning
        msg = QMessageBox()  # tworzenie obiektu klasy messageBox
        msg.setIcon(QMessageBox.Information)  # ustawianie ikony okna
        msg.setText(" Nie można dzielić przez 0 !!")  # ustawianie komunikatu
        msg.setWindowTitle("UWAGA!!")  # ustawianie tytułu
        msg.setStandardButtons(QMessageBox.Ok)  # dodawanie przycisku OK
        msg.exec_()  # egzekucja okna

    def Summing(self): # Dodawanie
        self.Calculate()
        self.a = 1

    def Sub(self): # Odejmowanie
        self.Calculate()
        self.a = 2

    def Multiply(self): # Mnożenie
        self.Calculate()
        self.a = 3

    def Dividing(self): # Dzielenie
          self.Calculate()
          self.a = 4
           

    def Reset(self): # C - Reset
        self.number = 0
        self.live_number = ""
        self.a = 1
        self.textbox.setText("0")

    def Sign(self): # zmiana znaku
        if self.live_number != "" :
            if "-"in self.live_number: # sprawdzanie czy '-' zawiera się w zmiennej string
                self.live_number = self.live_number[1:] # wyświetla string od indeksu 1
            else: 
                self.live_number = "-"+self.live_number
            self.textbox.setText(self.live_number)
        else:
            self.number *= -1
            self.textbox.setText(str(self.number))
    
    
    def Point(self): # przecinek
        if "." not in self.live_number:
            if self.live_number == '':
                self.live_number = "0"
            self.live_number += "."
            self.textbox.setText(self.live_number)
        
    def Square(self): # Pierwiastek
        self.Calculate()
        if float(self.number) >=0:
            self.number= np.sqrt(self.number)
            self.textbox.setText(str(self.number))

    
    def Calculate(self): # wybór działania matematycznego
        if self.live_number == '':
            self.live_number = "0.0"
        # print(self.live_number)
        match self.a:
            case 1:
                self.number += float(self.live_number)
            case 2:
                self.number -= float(self.live_number)
            case 3:
                self.number *= float(self.live_number)
            case 4:
                if float(self.live_number) != 0.0:
                  self.number /= float(self.live_number)
                else:
                    self.MessageBox()
                    self.live_number = ""
                    return 0
                  
        self.textbox.setText(str(self.number))
        self.live_number = ""
        self.a = 1



app = QApplication(sys.argv)
ex = App()
app.exec_()
