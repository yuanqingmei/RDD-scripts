#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/1/2 15:29
#@Author: Yuanqing Mei
#@File  : boxplot.py
# -*- coding:utf-8 -*-



import os
import pandas as pd
import matplotlib.pyplot as plt

# workingDirectory = "/home/mei/RD/terapromise/outcomes/"
workingDirectory = "E:\\RD\\terapromise\\outcomes\\20200112-3bugs\\20200112-3bugs\\"
# workingDirectory = "E:\\RD\\terapromise\\outcomes\\noRD\\20200106-3bugs-noRD\\"
# workingDirectory = "E:\\RD\\terapromise\\outcomes\\noRD\\20200104-1bug-noRD\\"
# workingDirectory = "E:\\RD\\terapromise\\outcomes\\20191228-3bugs-allprojects\\"
# workingDirectory = "E:\\RD\\terapromise\\outcomes\\20191224-7onebug\\"
# workingDirectory = "E:\\RD\\terapromise\\outcomes\\"
# E:\RD\terapromise\outcomes\20191224-7onebug
# E:\RD\terapromise\outcomes\20191228-3bugs-allprojects
outcomeList = "outcomeList.txt"

print(os.getcwd())
os.chdir(workingDirectory)
print(os.getcwd())


with open(workingDirectory + outcomeList) as L:
    outcomeListLines = L.readlines()

# 依次遍历每一性能结果文件
for outcomeListLine in outcomeListLines:

    outcomeFile = outcomeListLine.replace("\n", "")
    print("the outcome file name is ", outcomeFile)

    # 读入一个项目,由于每一列的度量可能不同名，故，还是每次读两行，取出对应度量的性能指标，再画箱线图
    #    outcomeDf = pd.read_csv(outcomeFile)	
    # 新建一个以outcomeFile命名的文件夹，用于存入该文件名下，若干度量的性能和阈值箱线图
    try:
        os.mkdir(workingDirectory + outcomeFile.replace(".csv", ""))
    except Exception as err:
        print(err)

    with open(workingDirectory + outcomeFile) as F:

        FileLines = F.readlines()
        # num_Lines存入每一行的元素个数
        num_Lines = [len(one.split(",")) for one in FileLines]
    try:
        FileLines[0]
        print(FileLines[0])
    except:
        print("the first item of Line contains ffef!")
        FileLines[0] = FileLines[0].encode('utf-8').decode('utf-8-sig')

    print("the len of FileLines is ", len(FileLines))
    # 定义一个数据框用于存储每个被测项目中各个项目度量的两种阈值，便于画图
    # 先以第一行的list元素作为Dataframe的key值。
    # 定义四个list用于存储考虑类规模效应下度量的性能，该度量的阈值，度量用元分析下的性能及其阈值
    # metric = []
    # metric_threshold = []
    # metric_meta = []                   #计算阈值时考虑的元分析的结果下的预测性能
    # metric_meta_threshold = []

    for line in FileLines:

        # project.GM所在的行为标题栏，检查每一行有没有新增加的标题栏(度量及阈值）
        if line.split(",")[0] == "project.GM" and len(line.split(",")) == max(num_Lines):

            print("column name line is ", line)
            columnName = line.replace("\n", "").split(",")
            print("the repr columnName is ", repr(columnName))
            df = pd.DataFrame(columns = columnName)
            break

    df1 = pd.read_csv(workingDirectory + outcomeFile, header = None, names = columnName)
    print("the cDf is \n", df1)
    print("the column names is ", df1.columns.values.tolist())
    print("the number of columns is ", df1.shape[1])
    print("the number of rows is ", df1.shape[0])

    # 读入每一个字典的key和value，除了project.GM外其他都可以做箱线图,由于每两行都是标题栏和数据，所以第一次读入标题，第二次存入数据
    for line in FileLines:

        if line.replace("\n", "").split(",")[0] == 'project.GM':

            # print("the two items is equal!")
            columnsList = line.replace("\n", "").split(",")
            # print("the columnsList is ", columnsList)

        else:

            i = 0
            row_index = len(df)
            for item in columnsList:

                # print("the item is ", item)
                # print("the len of df is ", len(df[item]))
                df.loc[row_index, item] = line.replace("\n", "").split(",")[i]
                # df.loc[len(df[item]), item] = line.replace("\n", "").split(",")[i]
                i += 1

    print(df)
    print(df.columns)
    os.chdir(workingDirectory + outcomeFile.replace(".csv", ""))
    print(os.getcwd())

    # 需要把所有的度量的性能指标画在一张图上，定义两个空数据框，分别用于存入行数相同的度量性能结果和对应的阈值数据。
    plotDf = pd.DataFrame()
    thresholdDf = pd.DataFrame()
    for c in df.columns:

        print("the ", c, " value is \n", df[c].dropna())	 # code to be executed

        if c == 'project.GM':
            thresholdDf[c] = df[c].dropna()
            continue

        if df[c].dropna().shape[0] != df1.shape[0] / 2:
            df[c].dropna().astype(float).plot.box(title="Box plot of " + c)
            plt.grid(linestyle="--", alpha=0.3)
            plt.savefig('./' + c + '.png')
            plt.close()
            if c[-10:] == "_threshold":
                thresholdDf[c] = df[c].dropna().astype(float)
            else:
                plotDf[c] = df[c].dropna().astype(float)
            continue

        if c[-10:] == "_threshold":

            # thresholdDf = pd.concat([thresholdDf, df[c].dropna().astype(float)], ignore_index = True, axis = 1)
            thresholdDf[c] = df[c].dropna().astype(float)
        else:
            plotDf[c] = df[c].dropna().astype(float)
            print(plotDf)

    print(plotDf)
    plt.rcParams['savefig.dpi'] = 900  # 图片像素
    plt.rcParams['figure.figsize'] = (10.0, 4.0)
    plotDf.plot.box(title="Box plot of all metrics")

    # plt.figure(figsize=(200, 100))

    plt.grid(linestyle="--", alpha=0.3)
    plt.savefig('./' + 'allMetrics.png')
    plt.close()
    print(thresholdDf)
    thresholdDf.to_csv(workingDirectory + outcomeFile.replace(".csv", "") + '/' + outcomeFile.replace(".csv", "")
                       + '_threshold.csv', sep=',', index=True, header=True)

    plotDf.to_csv(workingDirectory + outcomeFile.replace(".csv", "") + '/' + outcomeFile.replace(".csv", "")
                  + '_all.csv', sep=',', index=True, header=True)


#data = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100]
#dataLOC = [0.711135912, 0.571040241,	0.658171448,	0.714956878,	0.730305291,	0.63307761,	0.793492048,
# 0.499173456,	0.500719909,	0.582386248,	0.555375711,	0.8,	0.616166387,	0.612372436,	0.650600049,
# 	0.723417814,	0.767895476,	0.691832696,	0.657644579,	0.69017427,	0.691132821,	0.557588837,
# 0.471404521,	0.727406736,	0.745859441,	0.454256763,	0.655863082,	0.576415288,	0.604716995,
# 0.81167945,	0.547722558,	0.651452411,	0.666666667,	0.663779208,	0.589778614,	0.594669636,
# 0.679098372,	0.450370632,	0.732828109,	0.684934889,	0.756912589,	0.717684417,	0.609256445,
# 0.672297244,	0.681385144,	0.46291005,	0.724706105,	0.679408583,	0.567894807,	0.613090761,
# 0.621609499,	0.472952651,	0.874007373,	0.716627377,	0.614134837,	0.705700708,	0.770153402,
# 0.434407059,	0.64823944,	0.550673722,	0.499350227,	0.75]
#df = pd.DataFrame(dataLOC)
#df.plot.box(title="Box plot of metric LOC")
#plt.grid(linestyle="--", alpha=0.3)
#plt.show()
