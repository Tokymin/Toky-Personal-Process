import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
font_path = "/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/fonts/simfang.ttf"  # 替换为您的字体文件路径
# 数据
# 图表 20: 2020 年脊柱和关节植入手术例数
countries = ['中国', '英国', '美国', '日本', '法国', '德国']
spine = [0.7, 2.5, 3.1, 3.1, 3.2, 4.5]
joint = [0.5, 2.5, 3.1, 3.2, 3.1, 4.9]

# 图表 21: 2020 年中美关节市场差距
categories = ['人口(千万人)', '平均年龄(岁)', '膝关节置换手术室(万例)', '膝关节置换植入率(例/十万人)', '髋关节置换手术室(万例)', '髋关节置换植入率(例/十万人)']
china_data = [14.5, 37.4, 19.5, 13.6, 39.7, 28]
us_data = [32.8, 37.9, 84.7, 25, 50.7, 154.9]

# 图表 22: 2020 年中美骨科植入物渗透率对比
implant_types = ['关节', '创伤', '脊柱']
china_rate = [43, 21.9, 1.5]
us_rate = [0.6, 4.9, 3.8]

# 加载自定义字体
custom_font = fm.FontProperties(fname=font_path)
custom_font_large = fm.FontProperties(fname=font_path, size=12)

# 设置图形和坐标轴
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# 图表 20: 2020 年脊柱和关节植入手术例数
x = np.arange(len(countries))
width = 0.35

ax1 = axs[0, 0]
rects1 = ax1.bar(x - width/2, spine, width, label='脊柱', color='#66c2a5')
rects2 = ax1.bar(x + width/2, joint, width, label='关节', color='#fc8d62')

ax1.set_ylabel('手术例数（千人）', fontproperties=custom_font_large)
ax1.set_title('2020 年脊柱和关节植入手术例数（千人）', fontproperties=custom_font_large)
ax1.set_xticks(x)
ax1.set_xticklabels(countries, fontproperties=custom_font_large)
ax1.legend(prop=custom_font_large)

# 图表 21: 2020 年中美关节市场差距
y = np.arange(len(categories))

ax2 = axs[0, 1]
rects3 = ax2.barh(y - width/2, china_data, width, label='中国', color='#66c2a5')
rects4 = ax2.barh(y + width/2, us_data, width, label='美国', color='#fc8d62')

ax2.set_xlabel('数量', fontproperties=custom_font_large)
ax2.set_title('2020 年中美关节市场差距', fontproperties=custom_font_large)
ax2.set_yticks(y)
ax2.set_yticklabels(categories, fontproperties=custom_font_large)
ax2.legend(prop=custom_font_large)

# 图表 22: 2020 年中美骨科植入物渗透率对比
x2 = np.arange(len(implant_types))

ax3 = axs[1, 0]
rects5 = ax3.bar(x2 - width/2, china_rate, width, label='中国', color='#66c2a5')
rects6 = ax3.bar(x2 + width/2, us_rate, width, label='美国', color='#fc8d62')

ax3.set_ylabel('渗透率（%）', fontproperties=custom_font_large)
ax3.set_title('2020 年中美骨科植入物渗透率对比', fontproperties=custom_font_large)
ax3.set_xticks(x2)
ax3.set_xticklabels(implant_types, fontproperties=custom_font_large)
ax3.legend(prop=custom_font_large)

# 隐藏右上角的空白子图
axs[1, 1].axis('off')

# 添加注释

plt.tight_layout()
plt.show()
