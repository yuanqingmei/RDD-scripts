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
    import pandas as pd
    import matplotlib.pyplot as plt

    workingDirectory = wd
    resultDirectory = rd

    print(os.getcwd())
    os.chdir(workingDirectory)
    print(os.getcwd())

    # 新建一个以outcomeFile命名的文件夹，用于存入该文件名下，若干度量的性能和阈值箱线图
    try:
        os.mkdir(workingDirectory + "metricBoxplot")
    except Exception as err:
        print(err)

    with open(workingDirectory + tlist) as l:
        lines = l.readlines()

    alldf = pd.DataFrame()

    # bug为0的度量
    zerobugdf = pd.DataFrame()
    # bug大于零的度量
    onebugdf = pd.DataFrame()
    # bug大于3的度量
    threebugdf = pd.DataFrame()

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

    zerobugdf = alldf[alldf["bug"] == 0]
    onebugdf = alldf[alldf["bug"] > 0]
    threebugdf = alldf[alldf["bug"] >2]

    with open(resultDirectory + "trainigDataStatistical.csv", 'a+', encoding="utf-8", newline='') as f2,\
         open(resultDirectory + "zerobugStatistical.csv", 'a+', encoding="utf-8", newline='') as f0bug,\
         open(resultDirectory + "onebugStatistical.csv", 'a+', encoding="utf-8", newline='') as f1bug,\
         open(resultDirectory + "threebugDataStatistical.csv", 'a+', encoding="utf-8", newline='') as f3bug:
        writer = csv.writer(f2)
        zerobugwriter = csv.writer(f0bug)
        onebugwriter = csv.writer(f1bug)
        threebugwriter = csv.writer(f3bug)
        # 先写入columns_name
        if os.path.getsize(resultDirectory + "trainigDataStatistical.csv") == 0:
            writer.writerow(["metric", "number", "number>0", "min", "1st quartile", "median", "3rd quartile",
                             "max", "mean", "std.Dev", "IQR", "skewness", "kurtosis"])

        if os.path.getsize(resultDirectory + "zerobugStatistical.csv") == 0:
            zerobugwriter.writerow(["metric", "number", "number>0", "min", "1st quartile", "median", "3rd quartile",
                             "max", "mean", "std.Dev", "IQR", "skewness", "kurtosis"])

        if os.path.getsize(resultDirectory + "onebugStatistical.csv") == 0:
            onebugwriter.writerow(["metric", "number", "number>0", "min", "1st quartile", "median", "3rd quartile",
                             "max", "mean", "std.Dev", "IQR", "skewness", "kurtosis"])

        if os.path.getsize(resultDirectory + "threebugDataStatistical.csv") == 0:
            threebugwriter.writerow(["metric", "number", "number>0", "min", "1st quartile", "median", "3rd quartile",
                             "max", "mean", "std.Dev", "IQR", "skewness", "kurtosis"])

        for metric in metricData:

            print("the current metric is ", metric)

            number = len(alldf[metric])
            numberUpZero = alldf[alldf[metric] > 0].loc[:, metric].count()
            # print(numberUpZero)
            min = alldf[metric].min()
            firstQuartile = alldf[metric].quantile(0.25)
            thirdQuartile = alldf[metric].quantile(0.75)
            median = alldf[metric].median()
            max = alldf[metric].max()
            mean = alldf[metric].mean()
            std = alldf[metric].std()
            skewness = alldf[metric].skew()
            kurtosis = alldf[metric].kurt()

            writer.writerow([metric, number, numberUpZero, min, firstQuartile, median, thirdQuartile, max, mean, std,
                             thirdQuartile - firstQuartile, skewness, kurtosis])

            zerobugwriter.writerow([metric, len(zerobugdf), zerobugdf[zerobugdf[metric] > 0].loc[:, metric].count(),
                                    zerobugdf[metric].min(), zerobugdf[metric].quantile(0.25),
                                    zerobugdf[metric].median(), zerobugdf[metric].quantile(0.75),
                                    zerobugdf[metric].max(), zerobugdf[metric].mean(), zerobugdf[metric].std(),
                                    zerobugdf[metric].quantile(0.75) - zerobugdf[metric].quantile(0.25),
                                    zerobugdf[metric].skew(), zerobugdf[metric].kurt()])

            onebugwriter.writerow([metric, len(onebugdf), onebugdf[onebugdf[metric] > 0].loc[:, metric].count(),
                                   onebugdf[metric].min(), onebugdf[metric].quantile(0.25),
                                   onebugdf[metric].median(), onebugdf[metric].quantile(0.75),
                                   onebugdf[metric].max(), onebugdf[metric].mean(), onebugdf[metric].std(),
                                   onebugdf[metric].quantile(0.75)- onebugdf[metric].quantile(0.25),
                                   onebugdf[metric].skew(), onebugdf[metric].kurt()])

            threebugwriter.writerow([metric, len(threebugdf), threebugdf[threebugdf[metric] > 0].loc[:, metric].count(),
                                     threebugdf[metric].min(), threebugdf[metric].quantile(0.25),
                                     threebugdf[metric].median(), threebugdf[metric].quantile(0.75),
                                     threebugdf[metric].max(), threebugdf[metric].mean(), threebugdf[metric].std(),
                                     threebugdf[metric].quantile(0.75) - threebugdf[metric].quantile(0.25),
                                     threebugdf[metric].skew(), threebugdf[metric].kurt()])

            # 画箱线图：一个度量一张图，包含四种类型
            # pd.concat([alldf, zerobugdf, onebugdf, threebugdf], ignore_index=True, axis=1)
            # print(pd.concat([alldf, zerobugdf, onebugdf, threebugdf]))

            # .loc[:, metric].plot.box(title="Box plot of " + metric)
            # plt.grid(linestyle="--", alpha=0.3)
            # plt.savefig('./' + metric + '.jpg')
            # plt.close()

    alldf.to_csv(resultDirectory + "allmetrics.csv")
    zerobugdf.to_csv(resultDirectory + "zerobugmetrics.csv")
    onebugdf.to_csv(resultDirectory + "onebugmetrics.csv")
    threebugdf.to_csv(resultDirectory + "threebugmetrics.csv")


if __name__ == '__main__':
    statistical()
    print("the statistical function is done!")
