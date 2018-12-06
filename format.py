#This program is to format
import openpyxl
import os

def openWorkbook():
    wbName = '23630_ROTATION'
    #input("What is the name of your workbook?")
    wb = openpyxl.load_workbook(wbName + '.xlsx')
    sheet = wb.get_sheet_by_name(wbName)
    workbookData = []
    userID = sheet['B3'].value

    print("Reading rows...")
    for row in range(5, sheet.max_row + 1):
        message = sheet['C' + str(row)].value
        workbookData += [message]

    print("Here is your data for " + str(userID))
    print(workbookData)

openWorkbook()