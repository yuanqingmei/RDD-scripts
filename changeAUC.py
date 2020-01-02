#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/1/2 9:47
#@Author: Yuanqing Mei
#@File  : changeAUC.py.py

'''

由于AUC出现了0-0.5的数值，而理论上AUC应该介于0.5-1之间，用1-AUC代替原来的值，使之回归正常取值范围

'''

import os
import csv
import pandas as pd

workingDirectory = "E:\\RD\\terapromise\\outcomes\\20191228-3bugs-allprojects\\all-VARL_AUC\\"
# workingDirectory = "E:\\RD\\terapromise\\outcomes\\20191228-3bugs-allprojects\\"
# workingDirectory = "E:\\RD\\terapromise\\outcomes\\20191224-7onebug\\all-VARL_AUC\\"

print(os.getcwd())
os.chdir(workingDirectory)
print(os.getcwd())

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

# df = pd.DataFrame()
df = pd.read_csv(workingDirectory + "auc.csv")
# df = pd.read_csv(workingDirectory + "AUC.csv")

print(type(df))

# print(df.columns)
# print(df.shape[0])
# print(df.shape[1])
# rows = df.shape[0]

for metric in df.columns:
    # print(df[metric])
    # print(type(df[metric]))
    print(metric, end="  ")
    for i in range(df.shape[0]):
        # if isinstance(df[metric][i], str):
        #     continue
        if df[metric][i] < 0.5:     # 此处未做变量类型检查，而是默认把字符转为实数
            df[metric][i] = 1 - df[metric][i]
        print(df[metric][i], end="  ")
    print()
    # break

# pd.to_csv("newAUC.csv")

with open(workingDirectory + "newAUC.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    #先写入columns_name
    writer.writerow(df.columns)
    #写入多行用writerows
    for j in range(df.shape[0]):
        print(j)
        print(df.iloc[j,:])
        print(df.iloc[j,:].tolist())
        # print(type(df.iloc[j,:]))
        writer.writerow(df.iloc[j,:].tolist())