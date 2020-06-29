import sys, os
pwd = os.path.dirname(os.path.realpath(__file__))+"\\"
sys.path.append(pwd)

import csv

def GetWantedColumn():
    targetColumn = 0
    err = 1;
    while err:
        temp = input("Wanted Column: ")
        for idx in reversed(range(len(temp))):
            char = ord(temp[idx])
            if 65 <= char <= 90:
                targetColumn += idx*26+(char-65)
                err = 0
            else:
                print("Column must be capital letters.")
                err = 1
                break

    return targetColumn

# Constance
C_dataStartRow = 14 # 0 to 13 are iometer info
C_targetNameCol = 2 # row or "Target Name"

# handle input
if len(sys.argv) == 2:
    ifPath = sys.argv[1]
else:
    ifPath = input("Input csv path: ")

targetColumn = GetWantedColumn()


csvfin = open(ifPath, 'r', newline='', encoding='utf-8')
source = csv.reader(csvfin)

ofPath = ifPath+".result.csv"
csvfout = open(ofPath, 'w', newline='', encoding='utf-8')
result = csv.writer(csvfout)

letch = 0
workerIdx = 1
val = 0
for row in source:

    if letch:
        if row[C_targetNameCol] == 'All':
            break

        currentWorker = int(row[C_targetNameCol].split()[1])
        targetVal = float(row[targetColumn])
        
        if currentWorker == workerIdx:
            val += targetVal
        elif currentWorker < workerIdx:
            # checkout value
            result.writerow([val])
            # current row handle
            val = targetVal
            workerIdx = 1
        
        workerIdx += 1

    if row[0] == 'TimeStamp':
        letch = 1

print("Output %s" % ofPath)
