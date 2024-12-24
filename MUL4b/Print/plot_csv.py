import pandas as pd
import matplotlib.pyplot as plt

dataList = pd.read_csv("MULTIPLIEUR_4_BITS.csv")

time = dataList["Time(s)"]

A = [dataList["A0(V)"]+0,
    dataList["A1(V)"]+1,
    dataList["A2(V)"]+2,
    dataList["A3(V)"]+3]

B = [dataList["B0(V)"]+5,
    dataList["B1(V)"]+6,
    dataList["B2(V)"]+7,
    dataList["B3(V)"]+8]

P = [dataList["P0(V)"]+10,
    dataList["P1(V)"]+11,
    dataList["P2(V)"]+12,
    dataList["P3(V)"]+13,
    dataList["P4(V)"]+14,
    dataList["P5(V)"]+15,
    dataList["P6(V)"]+16,
    dataList["P7(V)"]+17]

for i in range(0,len(P)):
    plt.plot(time,P[i],label ="P"+str(i))

for i in range(0,len(A)):
    plt.plot(time,A[i],label ="A"+str(i))

for i in range(0,len(B)):
    plt.plot(time,B[i],label ="B"+str(i))

t_start = 0
t_stop = -1
while (i != len(time)):
    if A[0][i] > 0.4 and t_start == 0:
        t_start = i
        t_stop = 0
    
    if A[0][i] < 0.2 and t_stop == 0:
        t_stop = i
        middle = int((t_stop - t_start) / 2)
        plt.vlines(x=time[t_start+middle], ymin=0, ymax=18, color='k', linestyle='-', linewidth=1)
        t_start = 0
    i+=1
    
plt.show()

