import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    # 从文件中获取最高温度、最低温度和日期
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)
# 根据最高温度、最低温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形格式
ax.set_title("Highest/Lowest temperature per day in 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度 (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
