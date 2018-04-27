
# sheet.write(row_index, col_index, value)  （行指数，列指数，值）

import xlwt as ExcelWrite

def writeXLS(file_name):
    value = [["name", "jim", "hmm", "lilei"], ["sex", "man", "woman", "man"], ["age", 19, 24, 24]]
    xls = ExcelWrite.Workbook()
    sheet = xls.add_sheet("Sheet1")
    # for i in range(0, 3):
    #     for j in range(0, len(value)+1):#取行数
    #         sheet.write(j, i, value[i][j])
    value = range(100, 110)
    xls = ExcelWrite.Workbook()
    sheet = xls.add_sheet("Sheet1")

    for j in range(0, 10):
        sheet.write(j, 0, value[j])

    # for j in range(0,10):
    #     i=100
    #     if i <111:
    #         i = i+1
    #     sheet.write(j,0,i)

    xls.save(file_name)

if __name__ == "__main__":
    writeXLS("./test_write10.xls")