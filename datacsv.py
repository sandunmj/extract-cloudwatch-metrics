import pandas as pd
fileObject = open("data.txt","r")
fileList = fileObject.readlines()
timeStamps = []
networkOut = []
CPUUtil = []
EBS=[]
metric = [networkOut,CPUUtil,EBS]
newMetric = -1
for line in fileList:
    temp = list(line.split(" ".join("\t")))


    if ((temp[0] == 'TIMESTAMPS') and not (temp[1][:-2] in timeStamps)) :
        timeStamps.append(temp[1][:-2])

    
    if (temp[0] == "METRICDATARESULTS"):
        newMetric += 1

    if (temp[0] == "VALUES"):
        metric[newMetric].append(temp[1])



df = pd.DataFrame(timeStamps, columns=["Time Stamps"])
df["Network Out"] = networkOut
df["CPU Utilization"] = CPUUtil
df["EBS"] = EBS
df.to_csv('data.csv', index=False)