#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/1/2 11:06
#@Author: Yuanqing Mei
#@File  : boxplot_single.py

'''
read a dataframe, then draw a box plot
'''
import matplotlib.pyplot as plt
import os
import pandas as pd

# workingDirectory = "E:\\RD\\terapromise\\outcomes\\20191228-3bugs-allprojects\\all-VARL_AUC\\"
workingDirectory = "E:\\RD\\terapromise\\outcomes\\20191224-7onebug\\all-VARL_AUC\\"

print(os.getcwd())
os.chdir(workingDirectory)
print(os.getcwd())

plotDf = pd.read_csv(workingDirectory + "newAUC.csv")
plt.rcParams['savefig.dpi'] = 900  # 图片像素
plt.rcParams['figure.figsize'] = (10.0, 4.0)
plotDf.plot.box(title="Box plot of all metrics")

# plt.figure(figsize=(200, 100))

plt.grid(linestyle="--", alpha=0.3)
plt.savefig('./' + 'allNewAucMetrics.png')
plt.close()