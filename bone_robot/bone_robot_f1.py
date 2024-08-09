import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 数据
labels_2018 = ["关节类", "脊柱类", "创伤类", "运动医学", "骨科修复植材", "其他"]
sizes_2018 = [37, 18, 14, 11, 10, 10]

labels_2019 = ["创伤类", "脊柱类", "关节类", "其他"]
sizes_2019 = [29.8, 28.23, 27.77, 14.20]

labels_2022 = ["脊柱", "关节", "创伤", "运动医学", "其他"]
sizes_2022 = [117, 74, 47, 45, 21]

# 颜色
colors = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f"]

# 加载自定义字体
font_path = "/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/fonts/simfang.ttf"  # 替换为您的字体文件路径
custom_font = fm.FontProperties(fname=font_path)
custom_font_large = fm.FontProperties(fname=font_path, size=20)

# 绘制饼图
fig, axs = plt.subplots(2, 2, figsize=(12, 12))

# 2018 年饼图
axs[0, 0].pie(sizes_2018, labels=labels_2018, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'fontproperties': custom_font_large})
axs[0, 0].set_title(' 2018 年全球骨科器械细分领域占比', fontproperties=custom_font_large)

# 2019 年饼图
axs[0, 1].pie(sizes_2019, labels=labels_2019, autopct='%1.2f%%', startangle=140, colors=colors, textprops={'fontproperties': custom_font_large})
axs[0, 1].set_title(' 2019 年我国骨科器械细分领域占比', fontproperties=custom_font_large)

# 2022 年饼图
axs[1, 0].pie(sizes_2022, labels=labels_2022, autopct=lambda p: f'{p * sum(sizes_2022) / 100:.0f}亿', startangle=140, colors=colors, textprops={'fontproperties': custom_font_large})
axs[1, 0].set_title(' 2022 年我国骨科器械细分领域占比', fontproperties=custom_font_large)

# 隐藏右下角的空白子图
axs[1, 1].axis('off')


plt.tight_layout()
plt.show()
