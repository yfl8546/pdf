# 分割
import pdf_method
import os
from PyQt5 import QtWidgets,QtCore,QtGui


class PDF_fg(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    # 图形化UI主界面--
    def setupUI(self):
        self.setWindowTitle("PDF分割器V1.0 By 澄心元素 QQ：744537385")
        self.setGeometry(550,350,540,130)
        #设置QIcon
        self.setWindowIcon(QtGui.QIcon("ico的地址"))
        #---------初始化界面配件----------------------
        self.P_Qlable1()
        self.P_Qlable2()
        self.P_QButon1()
        self.P_QLineEdit1()
        self.P_QlineEdit2()
        self.P_Qlable3()
        self.P_Qbutton2()
        self.P_QLineEdit3()
        #显示界面
        # self.show()
    #--------界面配置------------------------
    #Qlable1的设置选择需要分割的文件：
    def P_Qlable1(self):
        self.Qlable1 = QtWidgets.QLabel(self)
        self.Qlable1.setText("请选择需要分割的文件：")
        self.Qlable1.setGeometry(QtCore.QRect(10, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Qlable1.setFont(font)
    #Qlable2的设置请选择分割文件的范围：
    def P_Qlable2(self):
        self.Qlable2 = QtWidgets.QLabel(self)
        self.Qlable2.setText("请选择分割文件的范围：")
        self.Qlable2.setGeometry(QtCore.QRect(10, 80, 200, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Qlable2.setFont(font)
    #QLineEdit1起始页码
    def P_QLineEdit1(self):
        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setGeometry(QtCore.QRect(190, 80, 110, 30))
        #下面三行限制只能输入数字
        temp = QtGui.QIntValidator(self)
        temp.setRange(1,100000)
        self.lineEdit1.setValidator(temp)
    #QButton开始分割
    def P_QButon1(self):
        self.Qbutton1 = QtWidgets.QPushButton(self)
        self.Qbutton1.setText("开始分割")
        self.Qbutton1.setGeometry(QtCore.QRect(450, 70, 70, 40))
        self.Qbutton1.clicked.connect(self.P_Qbutton1_onclick)
    #QLineEdit2结束页码
    def P_QlineEdit2(self):
        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(330, 80, 110, 30))
        #下面三行限制只能输入数字
        temp = QtGui.QIntValidator(self)
        temp.setRange(1,100000)
        self.lineEdit2.setValidator(temp)
    #Qlbale3的设置---
    def P_Qlable3(self):
        self.Qlabel_3 = QtWidgets.QLabel(self)
        self.Qlabel_3.setGeometry(QtCore.QRect(305, 90, 30, 16))
        self.Qlabel_3.setText("---")
    #“浏览”
    def P_Qbutton2(self):
        self.Qbutton2 = QtWidgets.QPushButton(self)
        self.Qbutton2.setText("浏览")
        self.Qbutton2.setGeometry(QtCore.QRect(450, 30, 70, 40))
        self.Qbutton2.clicked.connect(self.P_Qbutton2_onclick)
    #选择后出现文件所在的地址
    def P_QLineEdit3(self):
        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit3.setGeometry(QtCore.QRect(190, 30, 250, 30))
        #禁止输入内容
        self.lineEdit3.setReadOnly(True)
    #浏览文件
    def P_Qbutton2_onclick(self):
        #打开指定格式的文件
        file = QtWidgets.QFileDialog.getOpenFileName(self,"打开文件","./",("PDF(*.pdf)"))
        if file:
            #获取文件的名字，填入指定的位置
            self.lineEdit3.setText(str(file[0]))
    #分割文件
    def P_Qbutton1_onclick(self):
        #获取输入的内容
        FirstNum = self.lineEdit1.text()
        LastNum = self.lineEdit2.text()
        if FirstNum == "" or LastNum == "" or  FirstNum >= LastNum :
            self.msg_box = QtWidgets.QMessageBox (QtWidgets.QMessageBox.Warning,"警告","未输入页码或页码输入不正确")
        else:
            address = self.lineEdit3.text()
            path = os.path.dirname(address)
            temp = pdf_method.PDF_Split(address, FirstNum, LastNum, path)
            if temp == "1":
                self.msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "输入页码超过分割范围")
            elif temp == "0":
                self.msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "未选择需要分割的文件")
            else:
                self.msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "提示", "文件分割完毕")
        return self.msg_box.show()



# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     pdf_fg = PDF_fg()
#     app.exit(app.exec_())