#PDF合并
import time
from pdf_method import PDF_Merge
from PyQt5 import QtGui,QtWidgets,QtCore

class PDF_hb(QtWidgets.QMainWindow):
    def __init__(self):
        super(PDF_hb, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PDF合并V1.0 By 澄心元素 QQ：744537385")
        self.setGeometry(550, 350, 540, 130)
        self.P_Qlable1()
        self.P_QButon1()
        self.P_Qbutton2()
        self.P_TextEdit1()


    #请选择需要合并的文件：
    def P_Qlable1(self):
        self.Qlable1 = QtWidgets.QLabel(self)
        #调整大小并允许换行
        self.Qlable1.setText("请选择需要合并的文件：")
        self.Qlable1.setGeometry(QtCore.QRect(10, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Qlable1.setFont(font)
    #开始合并按钮
    def P_QButon1(self):
        self.Qbutton1 = QtWidgets.QPushButton(self)
        self.Qbutton1.setText("开始合并")
        self.Qbutton1.setGeometry(QtCore.QRect(450, 70, 70, 40))
        self.Qbutton1.clicked.connect(self.P_Qbutton1_onclick)
    #浏览文件按钮
    def P_Qbutton2(self):
        self.Qbutton2 = QtWidgets.QPushButton(self)
        self.Qbutton2.setText("浏览文件")
        self.Qbutton2.setGeometry(QtCore.QRect(450, 30, 70, 40))
        self.Qbutton2.clicked.connect(self.P_Qbutton2_onclick)
    #执行浏览文件
    def P_Qbutton2_onclick(self):
        #清空TextEdit1
        self.TextEdit1.clear()
        #打开指定格式的文件（多个文件）
        file = QtWidgets.QFileDialog.getOpenFileNames(self,"打开文件","./",("PDF(*.pdf)"))
        #file[0]时文件的列表
        self.file_list = file[0]
        self.file_list_len = len(self.file_list)
        # self.lineEdit1.setText(str(self.file_list))
        for i in range(self.file_list_len):
            self.TextEdit1.append(str(i+1) + "|" + self.file_list[i])

    #执行合并功能
    def P_Qbutton1_onclick(self):
        P_Text_edit = self.TextEdit1.toPlainText()
        if  P_Text_edit == "":
            self.msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,"警告","未选择文件")
        elif self.file_list_len <=1:
            self.msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "选择文件数值为1")
        else:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"文件正在合并中，请稍后。。。。。。","未选择文件或选择文件数值为1")
            msg_box.show()
            list = []
            for i in range(self.file_list_len):
                list.append(self.file_list[i])
            temp = PDF_Merge(list,self.file_list_len)
            if temp == "1":
                time.sleep(2)
                self.msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"提示","文件合并成功")
        self.msg_box.show()
    #显示选择的文件列表
    def P_TextEdit1(self):
        self.TextEdit1 = QtWidgets.QTextEdit(self)
        self.TextEdit1.setText("")
        self.TextEdit1.setGeometry(190,20,230,100)
        #禁止输入
        self.TextEdit1.setReadOnly(True)

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     pdf_main = PDF_hb()
#     app.exit(app.exec_())