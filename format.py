#This program is to format
#Script will work with PC files
import openpyxl
import os

'''def loopFiles():
    dirs = os.listdir('./')
    for dir in dirs:
        if dir.endswith(".xlsx"):
            if dir != 'testResults.xlsx':
                print("Running")
                runScript(dir)'''

def runScript():
    stringMatchers = ['started', 'Survey', 'selected']
    forbiddenWords = ['test_ads', 'selected undefined']
    workbookData = []
    wbName = 'combine.xlsx'
    wb = openpyxl.load_workbook(wbName)
    sheet = wb.active
    platform = sheet['B2'].value
    userID = sheet['B3'].value
    
    #Read data from workbook
    print("Reading rows...")
    for row in range(5, sheet.max_row + 1):
        if sheet['A' + str(row)].value == 'Member ID':
            userID = sheet['B' + str(row)].value

        if sheet['C' + str(row)].value == None:
            message = "blank"
        else:
            message = sheet['C' + str(row)].value

        if not any(y in message for y in forbiddenWords):
            if any(x in message for x in stringMatchers):
                workbookData.append(message)
                #need to link messages to ID
    #Save data in workbook
    wb2 = openpyxl.load_workbook('testResults.xlsx')
    sheet2 = wb2['Survey Results']
    row_count = sheet2.max_row
    print(row_count)
    for index, data in enumerate(workbookData, start=1):
        sheet2['A' + str(index+row_count)] = platform
        sheet2['B' + str(index+row_count)] = userID
        sheet2['C' + str(index+row_count)] = data

    wb2.save('testResults.xlsx')
    print('DONE!')

runScript()

