import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# 数据
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
market_size = np.array([300, 320, 350, 380, 360, 370, 390, 400, 410, 420, 450])
growth_rate = np.array([np.nan, -2.5, 3, 5, 3, 4, 2, 3, 2.5, 3.5, 5])
# 加载自定义字体
font_path = "/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/fonts/simfang.ttf"  # 替换为您的字体文件路径
custom_font = fm.FontProperties(fname=font_path)
custom_font_large = fm.FontProperties(fname=font_path, size=16)

# 设置图形和坐标轴
fig, ax1 = plt.subplots(figsize=(10, 6))

# 更改颜色
bar_color = '#72cfb1'  # 新的柱状图颜色
line_color = '#e15759'  # 新的折线图颜色

# 绘制市场规模柱状图
ax1.bar(years, market_size, color=bar_color, label='市场规模（亿美元）')
ax1.set_xlabel('年份', fontproperties=custom_font_large)
ax1.set_ylabel('市场规模（亿美元）', color=bar_color, fontproperties=custom_font_large)
ax1.tick_params(axis='y', labelcolor=bar_color)

# 绘制增长率折线图
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, color=line_color, marker='o', label='增长率')
ax2.set_ylabel('增长率', color=line_color, fontproperties=custom_font_large)
ax2.tick_params(axis='y', labelcolor=line_color)
ax2.set_ylim(-3, 6)

# 添加图例
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1), ncol=2, prop=custom_font_large)
# 设置标题并显示图表
plt.title('市场规模和增长率', fontproperties=custom_font_large)
plt.tight_layout(rect=[0, 0, 1, 0.85])  # 增加顶部空白以显示标题和图例
plt.show()