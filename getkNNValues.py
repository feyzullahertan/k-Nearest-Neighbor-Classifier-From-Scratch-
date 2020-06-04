import pandas as pd
import xlrd
import math

location=r"C:\Users\FeyzullahErtan\Desktop\Knn\KNNData.xlsx"

myList=[]
wb = xlrd.open_workbook(location) 
sheet = wb.sheet_by_index(0) 
for i in range(sheet.nrows):
    myList.append(sheet.row_values(i)) 
#for x in myList[1:]:

#print(myList[1][0])
#print(myList[-1][0])
main=myList[1]


u=[]
for y in myList[1:]:
    if main[6] == y[6]:
        u.append(y)
myResults=[]
for allData in u[1:]:
    firstColumn=(float(main[0])-float(allData[0]))**2
    secondColumn=(float(main[1])-float(allData[1]))**2
    thirdColumn=(float(main[2])-float(allData[2]))**2
    forthColumn=(float(main[3])-float(allData[3]))**2
    fifthColumn=(float(main[4])-float(allData[4]))**2
    result=firstColumn+secondColumn+thirdColumn+forthColumn+fifthColumn
    result=math.sqrt(result)
    myResults.append(result)
#print(myResults)


minValue=min(myResults)

u=u[1:]

print("Sayi:  " + str(minValue) +"  -||- Index:  "+ str(myResults.index(minValue))+ "  Sinif Etiketi:  " + str(u[myResults.index(minValue)][7]))
