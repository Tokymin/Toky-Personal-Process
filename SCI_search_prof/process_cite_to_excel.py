import pandas as pd

# 加载 Excel 文件
file_path = '/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/excels/论文检索表-模板.xls'

# 使用 xlrd 引擎读取 .xls 文件
excel_data = pd.ExcelFile(file_path, engine='xlrd')

# 显示工作表名称
print("工作表名称:", excel_data.sheet_names)

# 假设你的目标工作表是第一个，读取第一个工作表
df = pd.read_excel(file_path, sheet_name=0, engine='xlrd')

# 显示数据框架的前几行以确保读取正确
print("数据框架内容:")
print(df.head())

# 你的论文列表内容
papers = [
    "Xu Y, Feng L, Xia Z, et al. Camera pose estimation based on feature extraction and description for robotic gastrointestinal endoscopy[C]//International Conference on Intelligent Robotics and Applications. Cham: Springer International Publishing, 2021: 113-122. （EI收录会议论文）",
    "李妍；夏泽洋；吴晓君；熊璟*；考虑软组织形变的实时无参考超声图像综合评估方法，生物医学工程学杂志，2022，39(03): 480-487（EI收录期刊论文）",
    "Chen L, Gao X, Wang L, et al. A high-performance dielectric elastomer actuator with programmable actuations[C]//2022 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM). IEEE, 2022: 409-414. （EI收录会议论文）",
    "Tan M, Feng L, Xia Z, et al. Deep Motion Flow Estimation for Monocular Endoscope[C]//International Conference on Intelligent Robotics and Applications. Cham: Springer International Publishing, 2022: 367-377. （EI收录会议论文）",
    "Jin W, Tan M, Liu Y, et al. Design and MLP-based Kinematics Modeling of a Gastrointestinal Endoscopy Robot[C]//2023 IEEE International Conference on Robotics and Biomimetics (ROBIO). IEEE, 2023: 1-6. （EI收录会议论文）",
    "Dai Y, Li P, Zhang S, et al. Shape Analysis and Control of a Continuum Objects[C]//2023 IEEE International Conference on Robotics and Biomimetics (ROBIO). IEEE, 2023: 1-6. （EI收录会议论文）",
    "Sun C, Li P, Wu X, et al. Research on Manipulation of Soft Tissue Based on 3D Vision[C]//2022 IEEE International Conference on Cyborg and Bionic Systems (CBS). IEEE, 2023: 374-379. （EI收录会议论文）",
    "Wu C, Cai A, Gao X, et al. Nonlinear Dynamics of a Resonant-Impact Dielectric Elastomer Actuator[J]. Applied System Innovation, 2022, 5(6): 122. （ESCI收录期刊论文）",
    "Tan M, Peng H, Liang X, et al. LSTformer: long short-term transformer for real time respiratory prediction[J]. IEEE Journal of Biomedical and Health Informatics, 2022, 26(10): 5247-5257. （SCI收录期刊论文）",
    "Wu C, Yan H, Cai A, et al. A dielectric elastomer actuator-driven vibro-impact crawling robot[J]. Micromachines, 2022, 13(10): 1660. （SCI收录期刊论文）",
    "Li B, Li P, Sun R, et al. Respiratory motion estimation of tumor using point clouds of skin surface[J]. IEEE Transactions on Instrumentation and Measurement, 2023. （SCI收录期刊论文）",
    "Cao C, Wu C, Li X, et al. A Quad‐Unit Dielectric Elastomer Actuator for Programmable Two‐Dimensional Trajectories[J]. Advanced Intelligent Systems, 2024, 6(5): 2300865. （SCI收录期刊论文）",
    "Yang J, Liao T, Zhao J, et al. Domain Adaptation for Sensor-Based Human Activity Recognition with a Graph Convolutional Network[J]. Mathematics, 2024, 12(4): 556. （SCI收录期刊论文）",
    "Wu X, Wang T, Li Y, et al. A CAM-based weakly supervised method for surface defect inspection[J]. IEEE Transactions on Instrumentation and Measurement, 2022, 71: 1-10. （SCI收录期刊论文）"
]

# 提取论文信息并将其添加到数据框的对应列中
df['题名'] = [paper.split('.')[1].strip() for paper in papers]
df['责任者'] = [paper.split('.')[0].strip() for paper in papers]
df['来源名称'] = [paper.split('[')[1].split(']')[0].strip() if '[' in paper else '' for paper in papers]
df['出版年'] = [paper.split(',')[1].strip() if ',' in paper else '' for paper in papers]
df['其它信息'] = [paper.split('（')[1].split('）')[0].strip() if '（' in paper else '' for paper in papers]
df['Doi'] = ["" for _ in papers]  # 如果有 Doi 信息，可以在此填充

# 显示更新后的数据框
print("更新后的数据框内容:")
print(df.head())

# 保存更新后的数据框到新的 Excel 文件
output_file_path = '/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/excels/更新.xlsx'
df.to_excel(output_file_path, index=False)
