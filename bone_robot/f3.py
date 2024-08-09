import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
import textwrap
# 数据
font_path = "/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/fonts/simfang.ttf"  # 替换为您的字体文件路径

events = {
    "2019-11-10": "发改委与工信部和信化部等15部门发布《关于推动先进制造业和现代服务业深度融合发展的实施意见》，提出重点发展个性定制、无人车间、远程运维等新模式新业态。",
    "2020-02-1": "《关于升级和改造工业通信企业复工复产信息化的通知》强调重点强化健康管理设备、智能设备制造，医疗卫生建设、公共卫生预警应急系统等关键产业投入，满足人民群众的健康需求。",
    "2020-11-1": "上海市《关于推动生物医药产业园区特色化发展的实施方案》聚焦生物医药，推动人工智能数据驱动在生物医药产业的商业化应用，聚集有行业研究能力和产业化研发机构。",
    "2021-02-1": "工信部会同有关部门起草的《医疗装备产业发展规划(2021-2025年)》征求意见稿，提出要攻克高端手术机器人、智能化影像设备等高端装备，推进开源设备共性技术的研究和产业化体系建设。创新发展高端装备，智能视觉与语音交互、脑-机接口、人工智能等将成为新型医疗处理装备和系统。",
    "2021-06-04": "国务院办公厅印发的《关于推动公立医院高质量发展的意见》提出要提高新型术后机器人等新装备的应用。推动人工智能与医院医疗信息系统的深度应用。",
    "2021-12-21": "《十四五：医药装备产业发展规划》发布，攻关智能手术机器人、高端影像装备、智慧病房相关以及5G、多人自由手臂控制等关键技术。",
    "2022-01-29": "卫健委《关于进一步完善预约诊疗制度加强智慧医院建设的通知》：推广术后机器人、手术机器人在临床医疗活动中的制约反应性，推行实时诊、协同、共享和视频会诊和智能病历应用，提高医疗服务效率。",
    "2023-01-18": "迎接“机器人+”时代！十七部门联合发布关于印发《机器人+应用行动实施方案》的通知工信部版编号（2022）187号",
    "2023-03-04": "国家医保局解答：创新型耗材DRG，全面支持！"
}

# 转换日期为 datetime
dates = list(events.keys())
descriptions = list(events.values())
date_range = pd.date_range(start='2019-11-10', end='2027-01-01', freq='YS')

# 加载自定义字体
custom_font = fm.FontProperties(fname=font_path)
custom_font_large = fm.FontProperties(fname=font_path, size=12)

# 绘图
fig, ax = plt.subplots(figsize=(14, 8))

# 绘制事件点
ax.scatter(pd.to_datetime(dates), range(len(dates)), marker='o', color='black')

# 注释事件
for i, (date, desc) in enumerate(events.items()):
    wrapped_desc = "\n".join(textwrap.wrap(desc, width=40))
    ax.text(pd.to_datetime(date), i, f'{date}\n{wrapped_desc}', ha='left', va='center', fontsize=10, color='black',
            bbox=dict(facecolor='white', alpha=0.8),fontdict=None, fontproperties=custom_font_large,weight='bold')

# 格式化图表
ax.set_yticks(range(len(dates)))
ax.set_yticklabels(dates, fontproperties=custom_font_large)
ax.set_ylim(-1, len(dates))
ax.set_xlim(pd.to_datetime('2019-11-10'), pd.to_datetime('2027-01-01'))
ax.set_title('发展时间线', fontsize=14, fontproperties=custom_font_large)
ax.grid(True, axis='x', linestyle='--', alpha=0.7)

# 调整 x 轴的刻度
ax.set_xticks(date_range)
ax.set_xticklabels(date_range.strftime('%Y-%m-%d'), rotation=45, ha='right', fontproperties=custom_font_large)

plt.tight_layout()
plt.show()
