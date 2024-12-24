import pandas as pd
import matplotlib.pyplot as plt

dataList = pd.read_csv("MULTIPLIEUR_4_BITS.csv")

print(dataList.info())
print(dataList.head())

time = dataList["Time(s)"]

P = [dataList["P0(V)"],
    dataList["P1(V)"]+1,
    dataList["P2(V)"]+2,
    dataList["P3(V)"]+3,
    dataList["P4(V)"]+4,
    dataList["P5(V)"]+5,
    dataList["P6(V)"]+6,
    dataList["P7(V)"]+7]

A = [dataList["A0(V)"]+8,
    dataList["A1(V)"]+9,
    dataList["A2(V)"]+10,
    dataList["A3(V)"]+11]

B = [dataList["B0(V)"]+12,
    dataList["B1(V)"]+13,
    dataList["B2(V)"]+14,
    dataList["B3(V)"]+15]

for i in range(0,len(P)):
    plt.plot(time,P[i],label ="P"+str(i))

for i in range(0,len(A)):
    plt.plot(time,A[i],label ="A"+str(i))

for i in range(0,len(B)):
    plt.plot(time,B[i],label ="B"+str(i))

    
plt.show()


