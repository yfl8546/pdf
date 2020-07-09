#程序主界面
import sys
from pdf_fg import PDF_fg
from pdf_hb import PDF_hb
from PyQt5 import QtWidgets,QtCore


class PDF_Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(PDF_Main, self).__init__()
        self.setupUI()
        self.pdf_fg = PDF_fg()
        self.pdf_hb = PDF_hb()

    #主视图
    def setupUI(self):
        self.setWindowTitle("PDF分割合并器V1.0 By 澄心元素 QQ：744537385")
        self.setGeometry(400,400,500,200)
        # self.setWindowIcon(QtGui.QIcon("ICO图片的地址"))
        self.M_Button1()
        self.M_Button2()
        self.show()

    #分割
    def M_Button1(self):
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(QtCore.QRect(30,30,205,140))
        self.button1.setText("分割")
        self.button1.clicked.connect(self.M_Button1_click)

    #M_button1的事件
    def M_Button1_click(self):
        self.pdf_fg.setupUI()
        self.pdf_fg.show()
    # 合并
    def M_Button2(self):
        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setGeometry(QtCore.QRect(265, 30, 205,140))
        self.button2.setText("合并")
        self.button2.clicked.connect(self.M_Button2_click)

    # M_button2的事件
    def M_Button2_click(self):
        self.pdf_hb.setupUI()
        self.pdf_hb.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pdf_main = PDF_Main()
    app.exit(app.exec_())