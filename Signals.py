import math

#TODO import os y trabajar con las carpetas del OneDrive

def readAndWrite(RowData,NameFile):
    DataLine = Lines[RowData].split()
    DataPoints = int(DataLine[0])
    Dt = float(DataLine[8])
    DataMaxLen = int(DataLine[12][DataLine[12].find('f')+1:DataLine[12].find('.')])
    Units = DataLine[11].rstrip('.')
    ColPerRow = int(DataLine[12][1])

    Data = []
    RowEnd = RowData + math.ceil(DataPoints/ColPerRow)

    for i in range(RowData+1,RowEnd+1):
        data = [Lines[i][j:j+DataMaxLen] for j in range(0, len(Lines[i])-1, DataMaxLen)]
        Data = Data + data

    f = open(NameFile+".txt", "w")
    f.write(str(DataPoints)+' points')
    f.write('\n'+ str(Dt) +' sec. intervals')
    f.write('\n'+'Units: '+ str(Units) )
    for i in Data:
        f.write('\n'+str(float(i)))
    f.close()
    return RowEnd+1

NameChannel = "CHAN001"
NameAcc = "A1"
NameVel = "V1"
NameDisp = "D1"

f = open(NameChannel+".V2", "r")
Lines = f.readlines()
f.close()

RowAccData = 45
RowVelData = readAndWrite(RowAccData,NameAcc)
RowDispData = readAndWrite(RowVelData,NameVel)
readAndWrite(RowDispData,NameDisp)