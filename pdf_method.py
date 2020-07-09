from PyPDF2 import PdfFileReader, PdfFileWriter
import time

# 分割PDF文件
def PDF_Split(filename, FirstNum, LastNum,path) :
    if filename == "":
        return ("0")
    else:
        # 获取PDF文件
        pdf_input = PdfFileReader(open(file=filename, mode='rb'))
        # 获取该PDF文件的页码
        pdf_count = pdf_input.getNumPages()
        # 需要增加个判断，页码是否在规定的范围内
        # print(pdf_count,FirstNum,LastNum)
        if int(FirstNum) not in range(0,pdf_count) or int(LastNum) not in range(0,pdf_count) :
            return ("1")
        else:
            # 创建一个输出的PDF文件
            pdf_out = PdfFileWriter()
            # 遍历该文件页码，并添加到新的PDF文件中
            for i in range(int(FirstNum), int(LastNum)):
                pdf_out.addPage(pdf_input.getPage(i))
            temp = path +"/分割后的文件" + time.strftime('%Y-%m-%d') + "-"+ str(time.localtime().tm_hour) + "时-" + str(time.localtime().tm_min) \
                   + "分-"+  str(time.localtime().tm_sec) + "秒.pdf"
            # 写入新PDF文件
            pdf_out.write(open(temp, mode='wb'))
            return ("2")


#合并PDF文件
def PDF_Merge(filelist,file_list):
    #filelist是文件列表
    #file_list是文件的长度
    pdf_out = PdfFileWriter()
    #读取文件列表
    for i in (file_list):
        temp = filelist[i]
        pdf_input = PdfFileReader(open(file=temp,mode='rb'))
        pdf_input_count = pdf_input.getNumPages()
        for m in range(pdf_input_count):
            pdf_out.addPage(pdf_input.getPage(m))
        temp1 = "合并后的文件" + time.strftime('%Y-%m-%d') + "-"+ str(time.localtime().tm_hour) + "时-" + str(time.localtime().tm_min) \
                   + "分-"+  str(time.localtime().tm_sec) + "秒.pdf"
        pdf_out.write(open(temp1, mode='wb'))
        return ("1")
