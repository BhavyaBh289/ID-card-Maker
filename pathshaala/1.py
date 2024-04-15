import xlsxwriter
import code128

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

for i in range(1,251):
    roll = "23P%03d" %i
    print(roll)
    img = code128.image(roll)
    filename= roll+".png"
    img.save(filename)
    worksheet.write("A"+str(2*i), roll)
    worksheet.insert_image("A"+str(2*i-1), filename)
workbook.close()
