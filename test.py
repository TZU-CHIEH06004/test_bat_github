from PyQt5.QtWidgets import *    #*表示把所有東西都import進來
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow import Ui_Dialog       #import mainwindow 的 Ui_Dialog
import sys

def clicked_press_me():
    #用戶輸入方格
    x = ui.lineEdit.text()

    #跳出彈跳視窗
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText(x)
    message.exec_()


def click_hello():
    ui.label.setText("Hello")
    print("hello")


app = QApplication(sys.argv)
widge = QWidget()

t = QTranslator()
t.load("chinese.qm")
app.installTranslator(t)


ui = Ui_Dialog()
ui.setupUi(widge)




#callback function
ui.pressMeButton.clicked.connect(clicked_press_me)
ui.helloButton.clicked.connect(click_hello)



widge.show()
sys.exit(app.exec_())     #顯示成功執行結束，還是失敗執行結束




