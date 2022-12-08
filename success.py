from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Ui_success(QMainWindow):

    def setupUi(self, success):
        success.setObjectName("success")
        success.resize(400, 300)
        self.ok = QtWidgets.QPushButton(success)
        self.ok.setGeometry(QtCore.QRect(130, 200, 121, 41))
        self.ok.setObjectName("ok")

        self.ok.clicked.connect(self.quitapp)

        self.label = QtWidgets.QLabel(success)
        self.label.setGeometry(QtCore.QRect(80, 70, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(success)
        QtCore.QMetaObject.connectSlotsByName(success)

    def retranslateUi(self, success):
        _translate = QtCore.QCoreApplication.translate
        success.setWindowTitle(_translate("success", "success"))
        self.ok.setText(_translate("success", "OK"))
        self.label.setText(_translate("success", "Successful!"))

    def quitapp(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    success = QtWidgets.QMainWindow()
    ui = Ui_success()
    ui.setupUi(success)
    success.show()
    sys.exit(app.exec_())

