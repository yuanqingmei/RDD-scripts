#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/25 9:09
#@Author: Yuanqing Mei
#@File  : plotKO.py.py

import os
import matplotlib.pyplot as plt
import pandas as pd

workingDirectory = "E:\\RD\\terapromise\\metricBoxplot\\"
# resultDirectory = rd

print(os.getcwd())
os.chdir(workingDirectory)
print(os.getcwd())


# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)


# zerobugmean = [26.9, 1.22, 2.71, 0.55, 1.64, 13.01, 10.38, 0.25, 2.91, 1, 40.82, 1.33, 156.71, 3.08, 0.59, 0.17, 0.57, 3.91, 22.61, 5.63]
#
# data = pd.DataFrame(zerobugmean)
# data.columns = ["zerobugmean"]
# print(data)
# print(data.index)
# print(data.values)

# print(metricData)
zerobugdf = pd.read_csv("E:\\RD\\terapromise\\metricStatistical\\zerobugStatistical.csv")
onebugdf = pd.read_csv("E:\\RD\\terapromise\\metricStatistical\\onebugStatistical.csv")
threebugdf = pd.read_csv("E:\\RD\\terapromise\\metricStatistical\\threebugDataStatistical.csv")
# print(pd.sort_values(by=["mean", "metric"], descending=[True, False]))

# zerobugdf = zerobugdf.sort_index(by='mean')
print(zerobugdf)
# zerobugdf = zerobugdf.sort_values(by='mean')
zerobugdf = zerobugdf.reindex(index=[12, 11, 14, 2, 13, 15, 19, 9, 16, 1, 18, 8, 6, 0, 7, 3, 4, 17, 5, 10])
print(zerobugdf)
# zerobugdf = zerobugdf.drop([1, 9, 13, 14, 15, 4, 5, 10, 17])
# zerobugdf = zerobugdf.drop([1, 9, 13, 14, 15, 4, 5, 10, 3, 17])
print()
# zerobugdf = zerobugdf.drop([1, 9, 13, 14, 15, 4, 5, 10])
# zerobugdf = zerobugdf.drop([1, 9, 13, 14, 15])
zerobugdf = zerobugdf.drop([2, 11, 12, 16, 19, 6, 18, 8, 0, 7, 3, 4, 17, 5, 10])
# zerobugdf = zerobugdf.drop([2, 11, 12, 16, 19, 1, 9, 13, 14, 15])
# zerobugdf = zerobugdf.drop([6, 18, 8, 0, 7, 3, 4, 17, 5, 10])

onebugdf = onebugdf.reindex(index=[12, 11, 14, 2, 13, 15, 19, 9, 16, 1, 18, 8, 6, 0, 7, 3, 4, 17, 5, 10])
# onebugdf = onebugdf.reindex(index=[12, 11, 14, 2, 13, 15, 19, 9, 16, 6, 1, 18, 8, 0, 7, 3, 4, 17, 5, 10])
# onebugdf = onebugdf.sort_values(zerobugdf.sort_values(by='mean'))
# onebugdf = onebugdf.sort_values(by='mean')
# onebugdf = onebugdf.drop([1, 9, 13, 14, 15, 4, 5, 10, 17])
# onebugdf = onebugdf.drop([1, 9, 13, 14, 15, 4, 5, 10, 3, 17])
# onebugdf = onebugdf.drop([1, 9, 13, 14, 15, 4, 5, 10])
onebugdf = onebugdf.drop([2, 11, 12, 16, 19, 6, 18, 8, 0, 7, 3, 4, 17, 5, 10])
# onebugdf = onebugdf.drop([2, 11, 12, 16, 19, 1, 9, 13, 14, 15])
# onebugdf = onebugdf.drop([6, 18, 8, 0, 7, 3, 4, 17, 5, 10])

threebugdf = threebugdf.reindex(index=[12, 11, 14, 2, 13, 15, 19, 9, 16, 1, 18, 8, 6, 0, 7, 3, 4, 17, 5, 10])
# threebugdf = threebugdf.reindex(index=[12, 11, 14, 2, 13, 15, 19, 9, 16, 6, 1, 18, 8, 0, 7, 3, 4, 17, 5, 10])
# threebugdf = threebugdf.sort_values(by='mean')
# threebugdf = threebugdf.drop([1, 9, 13, 14, 15, 4, 5, 10, 17])
# threebugdf = threebugdf.drop([1, 9, 13, 14, 15, 4, 5, 10, 3, 17])
# threebugdf = threebugdf.drop([1, 9, 13, 14, 15, 4, 5, 10])
threebugdf = threebugdf.drop([2, 11, 12, 16, 19, 6, 18, 8, 0, 7, 3, 4, 17, 5, 10])
# threebugdf = threebugdf.drop([2, 11, 12, 16, 19, 1, 9, 13, 14, 15])
# threebugdf = threebugdf.drop([6, 18, 8, 0, 7, 3, 4, 17, 5, 10])


plt.rcParams['savefig.dpi'] = 900  # 图片像素
plt.rcParams['figure.figsize'] = (4.0, 4.0)

# plt.rcParams['figure.figsize'] = (12.0, 4.0)
plt.plot(zerobugdf["metric"], zerobugdf["mean"], marker='o', label="number of bugs = 0")
plt.plot(onebugdf["metric"], onebugdf["mean"], marker='s', linestyle="dashed", label="number of bugs > 0")
plt.plot(threebugdf["metric"], threebugdf["mean"], marker='^', linestyle="dashdot", label="number of bugs > 2")
# 显示图示
plt.legend()
# plt.plot(df["metric"], df["std.Dev"])
# plt.plot(data.index, data.values)
plt.savefig("E:\\RD\\terapromise\\metricBoxplot\\linechart_5metric_3.png")
plt.close()