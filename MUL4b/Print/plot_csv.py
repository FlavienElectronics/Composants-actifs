import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# readVector : containing raw data
# index : number of bit to store
# offset : minimum value of offset
# shift : value of bit's shift (ex 0.5 -> base offset of D0 = offset, base offset of D1 = offset + 0.5)
# start : starting of rising edge
# stop : starting of falling edge
# wide : wide of the high state
# limit : maximum index of the readVector array
def store(readVector,storeVector,index,offset,shift,start,stop,wide,limit):
    vect = []
    for i in range(0,index):
        if readVector[i][start+int(wide/2)]-(shift*i+offset) > 0.4:
            vect.append(1)
        else:
            vect.append(0)
    storeVector.append(vect)
    vect = []

    if stop+int(wide/2) < limit:
        for i in range(0,index):
            if readVector[i][stop+int(wide/2)]-(shift*i+offset) > 0.4:
                vect.append(1)
            else:
                vect.append(0)
        storeVector.append(vect)


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

A_value = []
B_value = []
P_value = []

t_start = 0
t_stop = -1
while (i != len(time)):
    if A[0][i] > 0.4 and t_start == 0:
        t_start = i
        t_stop = 0
    
    if A[0][i] < 0.2 and t_stop == 0:
        t_stop = i
        wide = (t_stop - t_start)
        plt.vlines(x=time[t_start+int(wide/2)], ymin=-0.2, ymax=17.5, color = 'y', linestyle='--', linewidth=0.5)
        if t_stop + int(wide/2) < len(time):
            plt.vlines(x=time[t_stop+int(wide/2)], ymin=-0.2, ymax=17.5, color = 'g', linestyle='--', linewidth=0.5)

        store(A,A_value,len(A),0,1,t_start,t_stop,wide,len(time))
        store(B,B_value,len(B),5,1,t_start,t_stop,wide,len(time))
        store(P,P_value,len(P),10,1,t_start,t_stop,wide,len(time))

        t_start = 0
    
    i+=1
    
plt.show()

plt.figure()
x = np.arange(0,len(A_value))
plt.plot(x,A_value)
plt.show()


