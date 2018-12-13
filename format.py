#This program is to format
#Script will work with PC files
#Something is wrong with how the log files are saved. Have to open in excel and save as csv
import openpyxl
import os
import csv
import glob

def loopFiles():
    path = "./*.csv"
    line = 0
    for fname in glob.glob(path):
        line += 1
        print(line)
        runScript(fname)

def runScript(fname):
    cleanData = []
    stringMatchers = ['started', 'Survey', 'selected']
    forbiddenWords = ['test_ads', 'selected undefined']
    with open(fname, newline='') as csv_file:
        dataArray = list(csv.reader(csv_file))

    for i in range(len(dataArray)):
        if not any(y in dataArray[i][2] for y in forbiddenWords):
            if any(x in dataArray[i][2] for x in stringMatchers):
                terribleList = []
                terribleList.append(dataArray[i][1])
                terribleList.append(dataArray[i][2])
                cleanData.append(terribleList)

    for data in cleanData:
        print(data)
        print('\n')

loopFiles()

