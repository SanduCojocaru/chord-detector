# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chorde-detector.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Simulation = QtWidgets.QPushButton(self.centralwidget)
        self.Simulation.setGeometry(QtCore.QRect(70, 440, 101, 23))
        self.Simulation.setObjectName("Simulation")
        self.Microphone = QtWidgets.QPushButton(self.centralwidget)
        self.Microphone.setGeometry(QtCore.QRect(70, 470, 101, 23))
        self.Microphone.setObjectName("Microphone")
        self.Quitter = QtWidgets.QPushButton(self.centralwidget)
        self.Quitter.setGeometry(QtCore.QRect(70, 500, 101, 23))
        self.Quitter.setObjectName("Quitter")
        self.VFrequence = QtWidgets.QTextEdit(self.centralwidget)
        self.VFrequence.setGeometry(QtCore.QRect(380, 400, 91, 31))
        self.VFrequence.setObjectName("VFrequence")
        self.Frequence = QtWidgets.QLabel(self.centralwidget)
        self.Frequence.setGeometry(QtCore.QRect(300, 400, 81, 31))
        self.Frequence.setObjectName("Frequence")
        self.Amplitude = QtWidgets.QLabel(self.centralwidget)
        self.Amplitude.setGeometry(QtCore.QRect(570, 450, 81, 31))
        self.Amplitude.setObjectName("Amplitude")
        self.Bruit = QtWidgets.QLabel(self.centralwidget)
        self.Bruit.setGeometry(QtCore.QRect(570, 500, 81, 31))
        self.Bruit.setObjectName("Bruit")
        self.Note = QtWidgets.QLabel(self.centralwidget)
        self.Note.setGeometry(QtCore.QRect(310, 330, 81, 31))
        self.Note.setObjectName("Note")
        self.VAmplitude = QtWidgets.QTextEdit(self.centralwidget)
        self.VAmplitude.setGeometry(QtCore.QRect(650, 450, 91, 31))
        self.VAmplitude.setObjectName("VAmplitude")
        self.VBruit = QtWidgets.QTextEdit(self.centralwidget)
        self.VBruit.setGeometry(QtCore.QRect(650, 500, 91, 31))
        self.VBruit.setObjectName("VBruit")
        self.Vnote = QtWidgets.QTextEdit(self.centralwidget)
        self.Vnote.setGeometry(QtCore.QRect(380, 330, 91, 31))
        self.Vnote.setObjectName("Vnote")
        self.Visualisation = MplWidget(self.centralwidget)
        self.Visualisation.setGeometry(QtCore.QRect(30, 10, 721, 301))
        self.Visualisation.setObjectName("Visualisation")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 370, 621, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Quitter.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Simulation.setText(_translate("MainWindow", "Simulation"))
        self.Microphone.setText(_translate("MainWindow", "Microphone"))
        self.Quitter.setText(_translate("MainWindow", "Quitter"))
        self.Frequence.setText(_translate("MainWindow", "Fréquence"))
        self.Amplitude.setText(_translate("MainWindow", "Amplitude"))
        self.Bruit.setText(_translate("MainWindow", "Bruit"))
        self.Note.setText(_translate("MainWindow", "Note"))


from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
