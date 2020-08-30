import xlrd
import json

wb=xlrd.open_workbook("test_user_data.xlsx")
sh=wb.sheet_by_name("TestUserReg")
#print(sh.nrows)
#print(sh.ncols)
#print(sh.cell(0,0).value)
#print(sh.row_values(1))



d=dict(zip(sh.row_values(0), sh.row_values(1)))
data=d['data']

print(data)
d1=json.loads(data) 
print(d1['phone'])
