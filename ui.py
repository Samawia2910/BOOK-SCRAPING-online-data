# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\BSCS\Semester 3\DSA lab\Solution\DSA LAB\Mid Term\CS261F21PID35\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class Ui_TheBookTown(object):
    def setupUi(self, TheBookTown):
        TheBookTown.setObjectName("TheBookTown")
        TheBookTown.resize(805, 617)
        TheBookTown.setMinimumSize(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        TheBookTown.setFont(font)
        TheBookTown.setStyleSheet("alternate-background-color: rgb(166, 166, 166);")
        self.centralwidget = QtWidgets.QWidget(TheBookTown)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(310, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 80, 47, 13))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(240, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(630, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(510, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(510, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(260, 120, 171, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(260, 170, 171, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 230, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(570, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(670, 570, 101, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 510, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(220, 510, 491, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.tableView.setGeometry(QtCore.QRect(50, 290, 701, 192))
        self.tableView.setObjectName("tableView")
        TheBookTown.setCentralWidget(self.centralwidget)

        self.retranslateUi(TheBookTown)
        QtCore.QMetaObject.connectSlotsByName(TheBookTown)

    def retranslateUi(self, TheBookTown):
        _translate = QtCore.QCoreApplication.translate
        TheBookTown.setWindowTitle(_translate("TheBookTown", "BookTown"))
        self.label_1.setText(_translate("TheBookTown", "The BookTown"))
        self.label_9.setText(_translate("TheBookTown", "Search Book"))
        self.pushButton_7.setText(_translate("TheBookTown", "Start"))
        self.pushButton_8.setText(_translate("TheBookTown", "Pause"))
        self.pushButton_9.setText(_translate("TheBookTown", "Stop"))
        self.pushButton_10.setText(_translate("TheBookTown", "Resume"))
        self.pushButton_11.setText(_translate("TheBookTown", "Search"))
        self.pushButton_12.setText(_translate("TheBookTown", "Scrap"))
        self.label_10.setText(_translate("TheBookTown", "Enter URL"))
        self.comboBox.setItemText(0, _translate("TheBookTown", "Searching Algorithms"))
        self.comboBox.setItemText(1, _translate("TheBookTown", "Starts with"))
        self.comboBox.setItemText(2, _translate("TheBookTown", "Ends with"))
        self.comboBox.setItemText(3, _translate("TheBookTown", "Contains"))
        self.comboBox_2.setItemText(0, _translate("TheBookTown", "Sorting Algorithms"))
        self.comboBox_2.setItemText(1, _translate("TheBookTown", "Insertion Sort"))
        self.comboBox_2.setItemText(2, _translate("TheBookTown", "Merge Sort"))
        self.comboBox_2.setItemText(3, _translate("TheBookTown", "Selection Sort"))
        self.comboBox_2.setItemText(4, _translate("TheBookTown", "Bubble Sort"))
        self.comboBox_2.setItemText(5, _translate("TheBookTown", "Quick Sort"))
        self.comboBox_2.setItemText(6, _translate("TheBookTown", "Counting Sort"))
        self.comboBox_2.setItemText(7, _translate("TheBookTown", "Radix Sort"))
        self.comboBox_2.setItemText(8, _translate("TheBookTown", "Bucket Sort"))
        self.comboBox_3.setItemText(0, _translate("TheBookTown", "Features"))
        self.comboBox_3.setItemText(1, _translate("TheBookTown", "Price, low to high"))
        self.comboBox_3.setItemText(2, _translate("TheBookTown", "Price, high to low"))
        self.comboBox_3.setItemText(3, _translate("TheBookTown", "Alphabetically, A-Z"))
        self.comboBox_3.setItemText(4, _translate("TheBookTown", "Alphabetically, Z-A"))
        self.pushButton_13.setText(_translate("TheBookTown", "Close"))
        self.label_11.setText(_translate("TheBookTown", "Scrapped Data"))

    def loadCsv(self, Data):
        with open(Data, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

class SortingAlgo:
    def mergeSort():
        print("Merge Sort")

    def insertionSort():
        print("Insertion Sort")

    def SelectionSort():
        print("Selection Sort")

    def bubbleSort():
        print("Bubble Sort")

    def QuickSort():
        print("Quick Sort")

    def CountingSort():
        print("Counting Sort")

    def RadixSort():
        print("Radix Sort")

    def BucketSort():
        print("Bucket Sort")

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TheBookTown = QtWidgets.QMainWindow()
    ui = Ui_TheBookTown()
    ui.setupUi(TheBookTown)
    TheBookTown.show()
    path = "E:\BSCS\Semester 3\DSA lab\Solution\DSA LAB\Mid Term\CS261F21PID35\Data.csv"
    ui.loadCsv(path)
    p1 = SortingAlgo()
    print(p1.bubbleSort)
    sys.exit(app.exec_())
