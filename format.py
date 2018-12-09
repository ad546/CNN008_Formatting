#This program is to format
import openpyxl
import os

stringMatchers = ["started", "Survey"]

def openWorkbook():
    wbName = '23630_ROTATION'
    #input("What is the name of your workbook?")
    wb = openpyxl.load_workbook(wbName + '.xlsx')
    sheet = wb.get_sheet_by_name(wbName)
    return sheet

def readFiles(sheet):
    workbookData = []
    userID = sheet['B3'].value
    print("Reading rows...")
    for row in range(5, sheet.max_row + 1):
        message = sheet['C' + str(row)].value
        if any(x in message for x in stringMatchers):
            workbookData.append(message)
    return workbookData, userID

def printData(workbookData, userID):
    print("Here is your data for " + str(userID))
    print(workbookData)

def main():
    workingSheet = openWorkbook()
    workbookData, userID = readFiles(workingSheet)
    printData(workbookData, userID)

main()
