import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 搜索查询列表
search_queries = [
    "Camera pose estimation based on feature extraction and description for robotic gastrointestinal endoscopy Xu Y, Feng L, Xia Z, et al.",
    "考虑软组织形变的实时无参考超声图像综合评估方法 李妍 夏泽洋 吴晓君 熊璟",
    "A high-performance dielectric elastomer actuator with programmable actuations Chen L, Gao X, Wang L, et al.",
    "Deep Motion Flow Estimation for Monocular Endoscope Tan M, Feng L, Xia Z, et al.",
    "Design and MLP-based Kinematics Modeling of a Gastrointestinal Endoscopy Robot Jin W, Tan M, Liu Y, et al.",
    "Shape Analysis and Control of a Continuum Objects Dai Y, Li P, Zhang S, et al.",
    "Research on Manipulation of Soft Tissue Based on 3D Vision Sun C, Li P, Wu X, et al.",
    "Nonlinear Dynamics of a Resonant-Impact Dielectric Elastomer Actuator Wu C, Cai A, Gao X, et al.",
    "LSTformer: long short-term transformer for real time respiratory prediction Tan M, Peng H, Liang X, et al.",
    "A dielectric elastomer actuator-driven vibro-impact crawling robot Wu C, Yan H, Cai A, et al.",
    "Respiratory motion estimation of tumor using point clouds of skin surface Li B, Li P, Sun R, et al.",
    "A Quad‐Unit Dielectric Elastomer Actuator for Programmable Two‐Dimensional Trajectories Cao C, Wu C, Li X, et al.",
    "Domain Adaptation for Sensor-Based Human Activity Recognition with a Graph Convolutional Network Yang J, Liao T, Zhao J, et al.",
    "A CAM-based weakly supervised method for surface defect inspection Wu X, Wang T, Li Y, et al."
]

# 从Google Scholar检索BibTeX引用的函数
def fetch_bibtex(query):
    search_url = f"https://scholar.google.com/scholar?q={requests.utils.quote(query)}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找第一个搜索结果
    result = soup.find('div', class_='gs_ri')
    if result:
        # 查找引用按钮
        cite_button = result.find('a', class_='gs_or_cit')
        if cite_button and 'href' in cite_button.attrs:
            cite_href = cite_button['href']
            if cite_href.startswith('/scholar?'):
                cite_url = f"https://scholar.google.com{cite_href}"
                cite_response = requests.get(cite_url)
                cite_soup = BeautifulSoup(cite_response.text, 'html.parser')

                # 查找BibTeX引用
                bibtex_link = cite_soup.find('a', text='BibTeX')
                if bibtex_link and 'href' in bibtex_link.attrs:
                    bibtex_url = f"https://scholar.google.com{bibtex_link['href']}"
                    bibtex_response = requests.get(bibtex_url)
                    return bibtex_response.text
    return None

# 获取每个查询的BibTeX引用
bibtex_list = []
for query in search_queries:
    bibtex = fetch_bibtex(query)
    bibtex_list.append(bibtex)
    time.sleep(1)  # 添加延迟以避免被Google Scholar封锁

# 创建一个数据框架
df = pd.DataFrame({'Query': search_queries, 'BibTeX': bibtex_list})

# 显示更新后的数据框架
print("更新后的数据框架内容:")
print(df.head())

# 保存更新后的数据框架到新的Excel文件
df.to_excel('/Users/mintan/PycharmProjects/Toky-Personal-Process/DataFiles/excels/更新后的论文检索表.xlsx', index=False)
