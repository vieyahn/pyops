import xlsxwriter
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A',20)
bold = workbook.add_format({'bold':True}) #define a overstriking layout obj

worksheet.write('A1',"Hello")
worksheet.write('A2',"World",bold)
worksheet.write('B2',"test chinese",bold)

worksheet.write(2,0,32)
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3:A4)')

worksheet.insert_textbox('B5','rwe.txt')
workbook.close()
