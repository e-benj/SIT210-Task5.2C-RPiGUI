from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.LOW)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(184, 208)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 110, 89))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnRed = QtWidgets.QRadioButton(self.layoutWidget, toggled = lambda: self.red_clicked())
        self.btnRed.setObjectName("btnRed")
        self.verticalLayout.addWidget(self.btnRed)
        self.btnGreen = QtWidgets.QRadioButton(self.layoutWidget, toggled = lambda: self.green_clicked())
        self.btnGreen.setObjectName("btnGreen")
        self.verticalLayout.addWidget(self.btnGreen)
        self.btnBlue = QtWidgets.QRadioButton(self.layoutWidget,  toggled = lambda: self.blue_clicked())
        self.btnBlue.setObjectName("btnBlue")
        self.verticalLayout.addWidget(self.btnBlue)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.close_app())
        self.btnClose.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.btnClose.setObjectName("btnClose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LED Selector"))
        self.btnRed.setText(_translate("MainWindow", "Red LED"))
        self.btnGreen.setText(_translate("MainWindow", "Green LED"))
        self.btnBlue.setText(_translate("MainWindow", "Blue LED"))
        self.btnClose.setText(_translate("MainWindow", "Close"))

    def red_clicked(self):
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.HIGH)

    def green_clicked(self):
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.HIGH)

    def blue_clicked(self):
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.HIGH)

    def close_app(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

