from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_ANOVAWindow(object):
    def setupUi(self, ANOVAWindow):
        ANOVAWindow.setObjectName("ANOVAWindow")
        ANOVAWindow.resize(781, 462)
        self.label = QtWidgets.QLabel(ANOVAWindow)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 31))
        self.label.setMinimumSize(QtCore.QSize(71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ANOVAWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 71, 31))
        self.label_2.setMinimumSize(QtCore.QSize(71, 31))
        self.label_2.setObjectName("label_2")
        self.KeywordBox = QtWidgets.QLineEdit(ANOVAWindow)
        self.KeywordBox.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.KeywordBox.setObjectName("KeywordBox")
        self.DataCButton = QtWidgets.QPushButton(ANOVAWindow)
        self.DataCButton.setGeometry(QtCore.QRect(70, 120, 121, 31))
        self.DataCButton.setObjectName("DataCButton")
        self.label_3 = QtWidgets.QLabel(ANOVAWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 71, 31))
        self.label_3.setMinimumSize(QtCore.QSize(71, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ANOVAWindow)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 71, 31))
        self.label_4.setMinimumSize(QtCore.QSize(71, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ANOVAWindow)
        self.label_5.setGeometry(QtCore.QRect(0, 270, 101, 31))
        self.label_5.setMinimumSize(QtCore.QSize(71, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(ANOVAWindow)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 71, 31))
        self.label_6.setMinimumSize(QtCore.QSize(71, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(ANOVAWindow)
        self.label_7.setGeometry(QtCore.QRect(30, 350, 71, 31))
        self.label_7.setMinimumSize(QtCore.QSize(71, 31))
        self.label_7.setObjectName("label_7")
        self.RotueBox = QtWidgets.QLineEdit(ANOVAWindow)
        self.RotueBox.setGeometry(QtCore.QRect(130, 200, 113, 20))
        self.RotueBox.setObjectName("RotueBox")
        self.LineBox = QtWidgets.QLineEdit(ANOVAWindow)
        self.LineBox.setGeometry(QtCore.QRect(130, 240, 113, 20))
        self.LineBox.setObjectName("LineBox")
        self.DefectBox = QtWidgets.QLineEdit(ANOVAWindow)
        self.DefectBox.setGeometry(QtCore.QRect(130, 280, 113, 20))
        self.DefectBox.setObjectName("DefectBox")
        self.AnovaXBox = QtWidgets.QLineEdit(ANOVAWindow)
        self.AnovaXBox.setGeometry(QtCore.QRect(130, 320, 113, 20))
        self.AnovaXBox.setObjectName("AnovaXBox")
        self.AnovaYBox = QtWidgets.QLineEdit(ANOVAWindow)
        self.AnovaYBox.setGeometry(QtCore.QRect(130, 360, 113, 20))
        self.AnovaYBox.setObjectName("AnovaYBox")
        self.VisualizeButton = QtWidgets.QPushButton(ANOVAWindow)
        self.VisualizeButton.setGeometry(QtCore.QRect(70, 400, 121, 31))
        self.VisualizeButton.setObjectName("VisualizeButton")
        self.DateBox = QtWidgets.QDateEdit(ANOVAWindow)
        self.DateBox.setGeometry(QtCore.QRect(130, 80, 111, 22))
        self.DateBox.setObjectName("DateBox")
        self.PicBox = QtWidgets.QLabel(ANOVAWindow)
        self.PicBox.setGeometry(QtCore.QRect(340, 30, 401, 371))
        self.PicBox.setText("")
        self.PicBox.setObjectName("PicBox")

        self.retranslateUi(ANOVAWindow)
        QtCore.QMetaObject.connectSlotsByName(ANOVAWindow)


    def retranslateUi(self, ANOVAWindow):
        _translate = QtCore.QCoreApplication.translate
        ANOVAWindow.setWindowTitle(_translate("ANOVAWindow", "Dialog"))
        self.label.setText(_translate("ANOVAWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Keyword</span></p></body></html>"))
        self.label_2.setText(_translate("ANOVAWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Date</span></p></body></html>"))
        self.DataCButton.setText(_translate("ANOVAWindow", "Data Connection"))
        self.label_3.setText(_translate("ANOVAWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Route</span></p></body></html>"))
        self.label_4.setText(_translate("ANOVAWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Line</span></p></body></html>"))
        self.label_5.setText(_translate("ANOVAWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Defect of interest</span></p></body></html>"))
        self.label_6.setText(_translate("ANOVAWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">ANOVA-X</span></p></body></html>"))
        self.label_7.setText(_translate("ANOVAWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">ANOVA-Y</span></p></body></html>"))
        self.VisualizeButton.setText(_translate("ANOVAWindow", "Data Connection"))

if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    Ui_ANOVAWindow().setupUi(widget)
    widget.show()
    sys.exit(app.exec_())