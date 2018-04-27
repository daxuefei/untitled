#-*-coding:utf-8-*-
import xlwt as ExcelWrite
#功能：实现传入某一列的名称及自动在下面的方格中插入100,110之间的数据
#定义一个函数，传入列号和第一行的名称
def writeXLS(file_name,cro_name,col_line=0):
    with open(file_name,'wb+') as f:
        value = range(100, 110)#定义传入列表格的数据
        xls = ExcelWrite.Workbook()
        sheet = xls.add_sheet("Sheet1")#定义下方的名称，默认可不修改
        sheet.write(0, col_line, cro_name)
        for j in range(1, 10):
            sheet.write(j, col_line, value[j-1])
        xls.save(file_name)

if __name__ == "__main__":
    writeXLS("./test_write17.xls","name",2)