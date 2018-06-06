# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取日期、最高气温和最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)   # 文件的第一行
    for index,column_header in enumerate(header_row):   # enumerate()获取每个元素的索引及其值
        print(index,column_header)
    dates,highs,lows = [],[],[]
    for row in reader:  #遍历每一行
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        try:
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()