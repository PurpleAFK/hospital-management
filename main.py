from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
from new import Ui_new
from view import Ui_view
from edit import Ui_edit
from success import Ui_success

class Ui_MainWindow(object):

    def openWindow(self):                                               #New Window
         self.window = QtWidgets.QMainWindow()                      
         self.ui = Ui_new()
         self.title = "Overflow"
         self.ui.setupUi(self.window)
         self.window.show()

    def openWindow2(self):                                              #View Window                                          
         self.window = QtWidgets.QMainWindow()
         self.ui = Ui_view()
         self.title = "Overflow"
         self.ui.setupUi(self.window)
         self.window.show()
<<<<<<< HEAD
    def openWindow3(self):
=======

    def openWindow3(self):                                              #Edit Window                                          
>>>>>>> 7f97d12ec9ef9ecbff44e3a5675e065a89d84362
         self.window = QtWidgets.QMainWindow()
         self.ui = Ui_edit()
         self.title = "Overflow"
         self.ui.setupUi(self.window)
         self.window.show()
<<<<<<< HEAD
=======

>>>>>>> 7f97d12ec9ef9ecbff44e3a5675e065a89d84362

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1041, 91))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.new_2 = QtWidgets.QPushButton(self.centralwidget)
        self.new_2.setGeometry(QtCore.QRect(410, 140, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        self.new_2.setFont(font)
        self.new_2.setObjectName("new_2")

        self.new_2.clicked.connect(self.openWindow)

        self.edit = QtWidgets.QPushButton(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(410, 250, 191, 71))

        self.edit.clicked.connect(self.openWindow3)

        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        self.edit.setFont(font)
        self.edit.setObjectName("edit")
        self.view = QtWidgets.QPushButton(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(410, 360, 191, 71))

        self.view.clicked.connect(self.openWindow2)

        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        self.view.setFont(font)
        self.view.setObjectName("view")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 26))
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
        self.label.setText(_translate("MainWindow", "HOSPITAL MANAGEMENT"))
        self.new_2.setText(_translate("MainWindow", "New"))
        self.edit.setText(_translate("MainWindow", "Edit"))
        self.view.setText(_translate("MainWindow", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
