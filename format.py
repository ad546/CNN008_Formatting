#This program is to format
import openpyxl
import os

def openWorkbook():
    wbName = '23630_ROTATION'
    #input("What is the name of your workbook?")
    wb = openpyxl.load_workbook(wbName + '.xlsx')
    sheet = wb.get_sheet_by_name(wbName)
    workbookData = []
    stringMatchers = ["started", "Survey"]
    userID = sheet['B3'].value

    print("Reading rows...")
    for row in range(5, sheet.max_row + 1):
        message = sheet['C' + str(row)].value
        if any(x in message for x in stringMatchers):
            workbookData.append(message)
        '''if "started" in sheet['C' + str(row)].value:
            message = sheet['C' + str(row)].value
            workbookData.append(message)
        elif "Survey answers" in sheet['C' + str(row)].value:
            message = sheet['C' + str(row)].value
            workbookData.append(message)'''

    print("Here is your data for " + str(userID))
    print(workbookData)

openWorkbook()