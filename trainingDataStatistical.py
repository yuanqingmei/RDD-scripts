#!/usr/bin/env python
# encoding:utf-8
"""
Author : Yuanqing Mei
Date : 2020
HomePage : http://github.com/yuanqingmei
Email : njumyq@outlook.com

功能：对terapromise92个项目的数据做描述性统计
"""


# 参数说明：
#    (1) wd： 用于存放被训练的项目路径，默认值为"/home/mei/RD/JURECZKO/"；
#    (2) rd： 用于存放为断点回归数据（按各个度量名形成文件 ）以及 metricThresholds.csv用入存入LOGIT回归变量的系数协方差，
#             用于计算调整后的阈值计算其方差，为元分析提供数据,默认值是"/home/mei/RD/JURECZKO/thresholds/"。
#    (3) trainl:  训练集的文件列表，即wd路径下文件名。默认值是："TrainingList.txt"

def statistical(wd="E:\\RD\\terapromise\\",
                rd="E:\\RD\\terapromise\\thresholds\\",
                tlist="List.txt"):
    import os
    import csv
    import numpy as np
    from sklearn.model_selection import StratifiedKFold
    import pandas as pd
    import statsmodels.api as sm
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix

    workingDirectory = wd
    resultDirectory = rd

    print(os.getcwd())
    os.chdir(workingDirectory)
    print(os.getcwd())

    with open(workingDirectory + tlist) as l:
        lines = l.readlines()

    alldf = pd.DataFrame()

    for line in lines:
        file = line.replace("\n", "")
        # print(file)

        # 分别处理文件中的每一个项目:f1取出要被处理的项目
        with open(workingDirectory + file, 'r', encoding="ISO-8859-1") as f1:

            reader = csv.reader(f1)

            fieldnames = next(reader)  # 获取数据的第一行，作为后续要转为字典的键名生成器，next方法获取
            # 对每个项目文件查看一下，把属于metric度量的字段整理到metricData
            metricData = fieldnames[3:24]  # 对fieldnames切片取出所有要处理的度量,一共20个
            # print(metricData)
            df = pd.read_csv(file)
            alldf = pd.concat([alldf, df])


    with open(resultDirectory + "trainigDataStatistical.csv", 'a+', encoding="utf-8", newline='') as f2:
        writer = csv.writer(f2)
        # 先写入columns_name
        if os.path.getsize(resultDirectory + "trainigDataStatistical.csv") == 0:
            writer.writerow(["metric", "number", "number>0", "min", "median", "max", "mean", "std.Dev",
                             "skewness", "kurtosis"])

        for metric in metricData:

            print("the current metric is ", metric)

            number = len(alldf[metric])
            numberUpZero = alldf[alldf[metric] > 0].loc[:, metric].count()
            # print(numberUpZero)
            min = alldf[metric].min()
            median = alldf[metric].median()
            max = alldf[metric].max()
            mean = alldf[metric].mean()
            std = alldf[metric].std()
            skewness = alldf[metric].skew()
            kurtosis = alldf[metric].kurt()

            writer.writerow([metric, number, numberUpZero, min, median, max, mean, std, skewness, kurtosis])

    alldf.to_csv(resultDirectory + "allmetrics.csv")


if __name__ == '__main__':
    statistical()
    print("the statistical function is done!")
