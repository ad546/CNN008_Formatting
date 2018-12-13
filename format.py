#This program is to format
#Script will work with PC files
#Something is wrong with how the log files are saved. Have to open in excel and save as csv
#Todo: group results based on stories / further clean selected, started / fix null byte issue
import openpyxl
import os
import csv
import glob

def loopFiles():
    path = "./*.csv"
    for fname in glob.glob(path):
        runScript(fname)

def runScript(fname):
    cleanData = []
    stringMatchers = ['started', 'Survey', 'selected']
    forbiddenWords = ['test_ads', 'selected undefined']
    print(fname)
    if fname != '.\Book1.csv':
        with open(fname, newline='') as csv_file:
            dataArray = list(csv.reader(csv_file))

        for i in range(len(dataArray)):
            if not any(y in dataArray[i][2] for y in forbiddenWords):
                if any(x in dataArray[i][2] for x in stringMatchers):
                    terribleList = []
                    terribleList.append(dataArray[i][1])
                    terribleList.append(dataArray[i][2])
                    cleanData.append(terribleList)

        writetoFile(cleanData)

def writetoFile(datatoWrite):
    #Book1
    with open('Book1.csv', 'a') as f:
        writer = csv.writer(f, delimiter = ',', lineterminator='\n')
        for value in datatoWrite:
            print(value)
            writer.writerow(value)

def main():
    loopFiles()

main()