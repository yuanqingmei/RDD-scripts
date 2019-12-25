#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/25 16:26
#@Author: Yuanqing Mei
#@File  : boxplot.py.py

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

workingDirectory = "E:\\RD\\terapromise\\metricBoxplot\\"

print(os.getcwd())
os.chdir(workingDirectory)
print(os.getcwd())

# # 显示所有列
pd.set_option('display.max_columns', None)
# # 显示所有行
pd.set_option('display.max_rows', None)

zerobugdf = pd.read_csv("E:\\RD\\terapromise\\metricStatistical\\zerobugmetrics.csv", low_memory=False)
onebugdf = pd.read_csv("E:\\RD\\terapromise\\metricStatistical\\onebugmetrics.csv")
threebugdf = pd.read_csv("E:\\RD\\terapromise\\metricStatistical\\threebugmetrics.csv")

# print(zerobugdf)

plt.rcParams['savefig.dpi'] = 900  # 图片像素
plt.rcParams['figure.figsize'] = (8.0, 4.0)

# totaldf = pd.concat(zerobugdf["loc"], onebugdf["loc"], threebugdf["loc"], axis=1)
# totaldf = pd.concat([zerobugdf["loc"], onebugdf["loc"], threebugdf["loc"]], axis=1)
# totaldf = pd.concat([zerobugdf["rfc"], onebugdf["rfc"], threebugdf["rfc"]], axis=1)



plt.boxplot([zerobugdf["loc"], onebugdf["loc"], threebugdf["loc"]], showfliers=False, vert=False,
            labels = ['zerobug','onebug','threebugs'],
            showmeans=True, meanprops = {'marker':'D','markerfacecolor':'indianred'} )

# plt.boxplot([zerobugdf["rfc"], onebugdf["rfc"], threebugdf["rfc"]], showfliers=False, vert=False,
#             labels = ['zerobug','onebug','threebugs'],
#             showmeans=True, meanprops = {'marker':'D','markerfacecolor':'indianred'} )

# plt.boxplot([zerobugdf["lcom"], onebugdf["lcom"], threebugdf["lcom"]], showfliers=False, vert=False,
#             labels = ['zerobug','onebug','threebugs'],
#             showmeans=True, meanprops = {'marker':'D','markerfacecolor':'indianred'} )

# plt.boxplot([zerobugdf["amc"], onebugdf["amc"], threebugdf["amc"]], showfliers=False, vert=False,
#             labels = ['zerobug','onebug','threebugs'],
#             showmeans=True, meanprops = {'marker':'D','markerfacecolor':'indianred'} )

# plt.boxplot(zerobugdf["loc"], showfliers=False, vert=False, positions="0")
# plt.boxplot(onebugdf["loc"], showfliers=False, vert=False, positions="1")
# plt.boxplot(threebugdf["loc"], showfliers=False, vert=False, positions="2")
# plt.yticks(np.arange(5), ('', 'zerobug', 'onebug', 'threebugs', ''))
# plt.yticks(np.arange(3), ('zerobug', 'onebug', 'threebugs'))

# plt.yticks([1],["zerobugs"])
# plt.yticks([3],["zerobug", "onebug", "threebug"])
plt.title("loc difference in zerobug-onebug-threebugs")

plt.savefig("E:\\RD\\terapromise\\metricBoxplot\\boxplot_loc.png")
plt.close()