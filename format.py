#This program is to format
#Script will work with PC files
#Something is wrong with how the log files are saved. Have to open in excel and save as csv
#Todo: group results based on stories / further clean selected, started
#Have to combine PC log files and delete Col D "copy *.csv combine.csv" or whatever name
#mobile have to delete rotation, and last three columns

import pandas #remember to use 'Anaconda Prompt' to run program and not Windows command
import os
import csv
import glob
import codecs

def cleanFiles(fname, username):
    fileData = pandas.read_csv(fname)
    fileData = fileData.fillna(" ")
    fileData.to_csv(r'C:\\Users\\' + username + '\\Desktop\\Programming\\Automation\\CNN008_Files\\fixed.csv', index=False)

def loopFiles(username, condition):
    path = "../CNN008_Files/*.csv"
    for fname in glob.glob(path):
        if condition == 'desktop':
            runScriptDesktop(fname, username)
        elif condition == 'mobile':
            runScriptMobile(fname, username)
        elif condition == 'tv':
            runScriptTV(fname, username)

def runScriptDesktop(fname, username):
    cleanData = []
    stringMatchers = ['started', 'Survey', 'survey', 'selected']
    forbiddenWords = ['test_ads', 'selected undefined']
    print(fname)
    if fname != '../CNN008_Files\Book1.csv':
        cleanFiles(fname, username)
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

def runScriptMobile(fname, username): #need to adjust dataArray indexes
    cleanData = []
    stringMatchers = ['Boring', 'Unexciting', 'Negative', 'Non-Political', 'Selected']
    forbiddenWords = ['test_ads', 'selected undefined']
    print(fname)
    if fname != '../CNN008_Files\Book1.csv':
        cleanFiles(fname, username)
        with open(fname, newline='') as csv_file:
            dataArray = list(csv.reader(csv_file))

        for i in range(len(dataArray)):
            if not any(y in dataArray[i][2] for y in forbiddenWords):
                if any(x in dataArray[i][2] for x in stringMatchers):
                    terribleList = []
                    terribleList.append(dataArray[i][1])
                    terribleList.append(dataArray[i][2])
                    terribleList.append(dataArray[i][3])
                    cleanData.append(terribleList)

        writetoFile(cleanData)

def runScriptTV(fname, username):
    cleanData = []
    stringMatchers = ['Playing Entertainment', 'Playing Political', 'Playing Negative'. 'Playing Positive', 'Boring', 'Unexciting', 'Negative', 'Non-Political']
    forbiddenWords = ['test_ads', 'selected undefined']
    print(fname)
    if fname != '../CNN008_Files\Book1.csv':
        cleanFiles(fname, username)
        with open(fname, newline='') as csv_file:
            dataArray = list(csv.reader(csv_file))

        for i in range(len(dataArray)):
            if not any(y in dataArray[i][2] for y in forbiddenWords):
                if any(x in dataArray[i][2] for x in stringMatchers):
                    terribleList = []
                    terribleList.append(dataArray[i][1])
                    terribleList.append(dataArray[i][2])
                    terribleList.append(dataArray[i][3])
                    cleanData.append(terribleList)

        writetoFile(cleanData)

def writetoFile(datatoWrite):
    #Book1
    with open('../CNN008_Files/Book1.csv', 'a') as f:
        writer = csv.writer(f, delimiter = ',', lineterminator='\n')
        for value in datatoWrite:
            print(value)
            writer.writerow(value)

def main():
    username = input("Please enter your username: ")
    condition = input("Please enter the condition: ")
    if condition == 'desktop':
        loopFiles(username, condition)
    elif condition == 'mobile':
        loopFiles(username, condition)
    elif condition == 'tv':
        loopFiles(username, condition)
    else:
        print("No such condition exists")

main()