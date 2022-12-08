
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 90, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pid = QtWidgets.QLineEdit(Dialog)
        self.pid.setGeometry(QtCore.QRect(210, 100, 151, 31))
        self.pid.setObjectName("pid")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.accepted.connect(self.which)
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Patient ID:"))
    
    def which(self):
        try:

            pid = self.pid.text()
            
            mydb = mc.connect(
                host = 'localhost',
                user='root',
                password='password',
                database='ohms'

            )

            mycursor = mydb.cursor()
            query = "select * from overflow where pid = " + pid +";"
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            print(query)
            print("Successful")

            

        except mc.Error as e:
            print("smth is wrong i can feel it")
            print(query)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
