import xlrd
import math
import pandas as pd


location=r"KNNData.xlsx"
data=[]
def calculate():
    wb = xlrd.open_workbook(location) 
    sheet = wb.sheet_by_index(0) 
    for i in range(sheet.nrows):
        data.append(sheet.row_values(i)) 
    main=data[1]


    separatedData=[] 
    for subset in data[1:]:
        if main[6] == subset[6]:
            separatedData.append(subset)
    results=[]

    for allData in u[1:]:
        firstColumn=(float(main[0])-float(allData[0]))**2
        secondColumn=(float(main[1])-float(allData[1]))**2
        thirdColumn=(float(main[2])-float(allData[2]))**2
        forthColumn=(float(main[3])-float(allData[3]))**2
        fifthColumn=(float(main[4])-float(allData[4]))**2
        result=firstColumn+secondColumn+thirdColumn+forthColumn+fifthColumn
        result=math.sqrt(result)
        results.append(result)

        minValue=min(results)

        u=u[1:]
    return str(minValue),str(results.index(minValue)),str(separatedData[results.index(minValue)][7])
    # Number = minValue
    # Index = results.index(minValue)
    # Tag = separatedData[results.index(minValue)][7]
    
