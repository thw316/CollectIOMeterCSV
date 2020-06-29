import sys, os
pwd = os.path.dirname(os.path.realpath(__file__))+"\\"
sys.path.append(pwd)

import csv

# Constance
C_dataStartRow = 14 # 0 to 13 are iometer info
C_targetNameRow = 2 # row or "Target Name"

# handle input
if len(sys.argv) == 2:
    ifPath = sys.argv[1]
else:
    ifPath = input("Input csv path: ")

contents = []
with open(ifPath, 'r', newline='', encoding='utf-8') as csvf:
    temp = csv.reader(csvf)
    for row in temp:
        contents.append(row)
#workers = ''
#while True:
#    try:
#        workers = int(input("Suspect Workers: "))
#        if isinstance(workers, int) and workers > 0:
#            break
#    except:
#        print("Workers must be positive integers.")
#    print("Workers must be positive integers.")

targetColumn = 0
while True:
    temp = input("Wanted Column: ")
    for idx in reversed(range(len(temp))):
        char = ord(temp[idx])
        if 65 <= char <= 90:
            targetColumn += idx*26+(char-65)
        else:
            print("Column must be larger letters.")
            continue
    break

result = [] 
workerIdx = 1
resultIdx = 0
rowIdx = C_dataStartRow
rowIdxMax = len(contents)
val = 0
while True:
    if rowIdx >= rowIdxMax or contents[rowIdx][C_targetNameRow] == "All":
        break

    currentWorker = int(contents[rowIdx][C_targetNameRow].split()[1])
    targetVal = float(contents[rowIdx][targetColumn])
    if currentWorker == workerIdx:
        val += targetVal
    elif currentWorker < workerIdx:
        # checkout value
        result.append(val)
        # current row handle
        val = targetVal
        workerIdx = 1
    
    workerIdx += 1
    rowIdx+=1

ofPath = ifPath+".result.csv"
with open(ofPath, 'w', newline='', encoding='utf-8') as csvf:
    csvwriter = csv.writer(csvf)
    for val in result:
        csvwriter.writerow([val])
print("Output %s" % ofPath)
