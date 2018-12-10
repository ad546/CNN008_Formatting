#This program is to format
import openpyxl
import os

def runScript():
    stringMatchers = ['started', 'Survey', 'selected']
    forbiddenWords = ['test_ads', 'selected undefined']
    workbookData = []
    #Open Workbook
    wbName = '23630_ROTATION'
    wb = openpyxl.load_workbook(wbName + '.xlsx')
    sheet = wb[wbName]
    userID = sheet['B3'].value
    
    #Read data from workbook
    print("Reading rows...")
    for row in range(5, sheet.max_row + 1):
        message = sheet['C' + str(row)].value
        if not any(y in message for y in forbiddenWords):
            if any(x in message for x in stringMatchers):
                workbookData.append(message)

    #Save data in workbook
    wb2 = openpyxl.load_workbook('testResults.xlsx')
    sheet2 = wb2['Survey Results']
    for index, data in enumerate(workbookData, start=1):
        sheet2['A' + str(index)] = userID
        sheet2['B' + str(index)] = data

    wb2.save('testResults.xlsx')
    print("DONE!")

runScript()

