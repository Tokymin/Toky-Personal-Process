def openning_plan():
    import pandas as pd

    # Creating a structured data for the research plan in CSV format
    data = {
        "时间节点": ["2024年9月", "2024年12月", "2025年6月", "2025年12月", "2026年5月"],
        "任务": [
            "调研相关论文，完成开题报告，开始腔道预测部分的数据集准备工作",
            "完成腔道预测部分的模型搭建与实验实施，撰写Diffusion深度估计小论文，申请专利等",
            "完成技术路线第三阶段的导航模型部署工作，准备中期答辩",
            "撰写论文，在老师指导下修改论文",
            "论文定稿，答辩"
        ],
        "目标": [
            "为Diffusion深度估计研究打好基础",
            "完成腔道方向预测模型构建，进一步完善导航模型",
            "推进导航模型的实际部署，并准备答辩",
            "确保论文质量，按时完成论文撰写",
            "通过答辩，顺利毕业"
        ]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Saving the DataFrame as a CSV file
    file_path = "研究计划.csv"
    df.to_csv(file_path, encoding='utf-8', index=False)


def jijin_results():
    import pandas as pd

    # Creating a structured data for the research plan in CSV format
    data = {
        "研究内容": ["算法创新", "大模型参数量化优化", "模型推理加速策略", "多模态导航具身智能平台"],
        "预期成果": [
            "建立端侧高效的多模态数据特征对齐与融合算法不少于2种。",
            "量化后的端侧模型内存占用减少20%至30%。",
            "自适应推理加速，使推理时间缩短15%至30%。",
            "申请发明专利5项，发表高水平论文5篇。"
        ]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Saving the DataFrame as a CSV file
    file_path = "研究成果计划.csv"
    df.to_csv(file_path, encoding='utf-8', index=False)


if __name__ == '__main__':
    # openning_plan()
    jijin_results()