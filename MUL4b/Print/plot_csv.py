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

# readArray : array containing the binary vectors
# storeArray : array containing the converted binary value
# size : number of bits coding the binary vectors
def vectorToDec(readArray,storeArray,size):
    for i in range(0,len(readArray)):
        res = 0
        for j in range(0,size):
            res += int(readArray[i][j]) << j
        storeArray.append(res)


# A : operand 1
# B : operant 2
# res : supposed result of A × B
def affiche_A_MUL_B_Equal_res(A,B,res):
    valid = "false"
    if (A * B == res):
        valid = "true"
    print(str(A) + " * " + str(B) + " = " + str(res)+ " -> " + str(valid) + "\n")
    with open("resultat.txt", "a") as file:
        file.write(str(A) + " * " + str(B) + " = " + str(res)+ " -> " + str(valid) + "\n\n")

def afficheEqu(vectA,vectB,vectRes):
    if len(vectA) == len(vectB) and len(vectB) == len(vectRes):
        for i in range(0,len(vectA)):
            print("Line : " + str(i))
            with open("resultat.txt", "a") as file:
                file.write("Line : " + str(i) + "\n")
            affiche_A_MUL_B_Equal_res(vectA[i],vectB[i],vectRes[i])

def plotLine(x,col):
    plt.vlines(x, ymin=-0.2, ymax=18, color = col, linestyle='--', linewidth=0.5)


# time : vector containing time information
# clock : vector containing the base vector that varies the most
# A_res,B_res,P_res : vector that will contain the results
# A,B,P : vector that contain the raw input
def readGraphic(time,clock,A,B,P,A_res,B_res,P_res):
    t_start = 0
    t_stop = -1
    i = 0
    while (i != len(time)):
        if clock[i] > 0.4 and t_start == 0:
            t_start = i
            t_stop = 0
        
        if clock[i] < 0.2 and t_stop == 0:
            t_stop = i
            wide = (t_stop - t_start)
            plotLine(time[t_start+int(wide/2)],'y')
            if t_stop + int(wide/2) < len(time):
                plotLine(time[t_start+int(wide/2)],'g')

            store(A,A_res,len(A),0,1,t_start,t_stop,wide,len(time))
            store(B,B_res,len(B),5,1,t_start,t_stop,wide,len(time))
            store(P,P_res,len(P),10,1,t_start,t_stop,wide,len(time))

            t_start = 0
        
        i+=1
        


dataList = pd.read_csv("MULTIPLIEUR_4_BITS.csv")

with open("resultat.txt", "w") as file:
    file.write("\t\t\tResulats : \n")

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

readGraphic(time,A[0],A,B,P,A_value,B_value,P_value)
    

decA = []
decB = []
decP = []

vectorToDec(A_value,decA,4)
vectorToDec(B_value,decB,4)
vectorToDec(P_value,decP,8)

afficheEqu(decA,decB,decP)

plt.show()





