import re

# Define the input text
input_text = """
5人工智能方法 在本节中，首先回顾了特征提取和工程，然后介绍了不同类别的人工智能方法，即监督学习，无监督学习，半监督学习和强化学习。这些学习方法及其主要子字段如图6所示。手动的，或（iii）手动和自动特征提取的融合。下一步骤是特征选择，其中根据一些特征评分度量来选择所提取特征的子集。然后，基于目标数据集评估所选特征的性能。重复该过程，直到获得满意的结果。 5.2有监督学习 学习算法划分为两大类：有监督学习和无监督学习。在监督学习中，已知训练样本的期望输出，并且使用给定的数据样本及其期望输出来训练模型[33]。一般来说，监督学习用于目标是将输入样本映射到输出标签的分类[34]。它还用于目标是学习从输入到连续输出的映射的回归。在分类和回归中，我们都希望找到输入和输出之间的正确关系。的确，我们正在寻找一种能够有效地产生正确输出数据的模型。如果训练数据有噪声或具有不正确的标签，则训练模型的有效性将明显降低。一些常见的监督学习算法是支持向量机（SVM）[35]、人工神经网络（ANN）[36]、朴素贝叶斯[37，38]和随机森林[39]。 5.3深度学习 深度学习（DL）是基于人工神经网络（NN）的机器学习方法大家...
@article{saadatnejad2019lstm,
  title={LSTM-based ECG classification for continuous monitoring on personal wearable devices},
  author={Saadatnejad, Saeed and Oveisi, Mohammadhosein and Hashemi, Matin},
  journal={IEEE journal of biomedical and health informatics},
  volume={24},
  number={2},
  pages={515--523},
  year={2019},
  publisher={IEEE}
}
...的潜在用途。
@article{amirshahi2019ecg,
  title={ECG classification algorithm based on STDP and R-STDP neural networks for real-time monitoring on ultra low-power personal wearable devices},
  author={Amirshahi, Alireza and Hashemi, Matin},
  journal={IEEE transactions on biomedical circuits and systems},
  volume={13},
  number={6},
  pages={1483--1493},
  year={2019},
  publisher={IEEE}
}
...中可以看到这一点。
@article{acharya2020deep,
  title={Deep neural network for respiratory sound classification in wearable devices enabled by patient specific model tuning},
  author={Acharya, Jyotibdha and Basu, Arindam},
  journal={IEEE transactions on biomedical circuits and systems},
  volume={14},
  number={3},
  pages={535--544},
  year={2020},
  publisher={IEEE}
}
...来证明这一点。
@article{hssayeni2019wearable,
  title={Wearable sensors for estimation of parkinsonian tremor severity during free body movements},
  author={Hssayeni, Murtadha D and Jimenez-Shahed, Joohi and Burack, Michelle A and Ghoraani, Behnaz},
  journal={Sensors},
  volume={19},
  number={19},
  pages={4215},
  year={2019},
  publisher={MDPI}
}
...还显示了这一点。
@article{ahlrichs2016detecting,
  title={Detecting freezing of gait with a tri-axial accelerometer in Parkinson’s disease patients},
  author={Ahlrichs, Claas and Sam{a}, Albert and Lawo, Michael and Cabestany, Joan and Rodr{i}guez-Mart{i}n, Daniel and P{\'e}rez-L{\'o}pez, Carlos and Sweeney, Dean and Quinlan, Leo R and Laighin, Gear{\`o}id {\`O} and Counihan, Timothy and others},
  journal={Medical \& biological engineering \& computing},
  volume={54},
  pages={223--233},
  year={2016},
  publisher={Springer}
}
...等人也提出了类似的观点。
@article{varatharajan2018wearable,
  title={Wearable sensor devices for early detection of Alzheimer disease using dynamic time warping algorithm},
  author={Varatharajan, Ramachandran and Manogaran, Gunasekaran and Priyan, Malarvizhi Kumar and Sundarasekar, Revathi},
  journal={Cluster Computing},
  volume={21},
  pages={681--690},
  year={2018},
  publisher={Springer}
}
...等等。
@article{das2018unsupervised,
  title={Unsupervised heart-rate estimation in wearables with Liquid states and a probabilistic readout},
  author={Das, Anup and Pradhapan, Paruthi and Groenendaal, Willemijn and Adiraju, Prathyusha and Rajan, Raj Thilak and Catthoor, Francky and Schaafsma, Siebren and Krichmar, Jeffrey L and Dutt, Nikil and Van Hoof, Chris},
  journal={Neural networks},
  volume={99},
  pages={134--147},
  year={2018},
  publisher={Elsevier}
}
...中有所体现。
@inproceedings{krause2003unsupervised,
  title={Unsupervised, Dynamic Identification of Physiological and Activity Context in Wearable Computing.},
  author={Krause, Andreas and Siewiorek, Daniel P and Smailagic, Asim and Farringdon, Jonny},
  booktitle={ISWC},
  volume={3},
  pages={88},
  year={2003}
}
...中也有所提及。
@article{janarthanan2020optimized,
  title={Optimized unsupervised deep learning assisted reconstructed coder in the on-nodule wearable sensor for human activity recognition},
  author={Janarthanan, R and Doss, Srinath and Baskar, S},
  journal={Measurement},
  volume={164},
  pages={108050},
  year={2020},
  publisher={Elsevier}
}
...中进行了详细讨论。
@inproceedings{ballinger2018deepheart,
  title={DeepHeart: semi-supervised sequence learning for cardiovascular risk prediction},
  author={Ballinger, Brandon and Hsieh, Johnson and Singh, Avesh and Sohoni, Nimit and Wang, Jack and Tison, Geoffrey and Marcus, Gregory and Sanchez, Jose and Maguire, Carol and Olgin, Jeffrey and others},
  booktitle={Proceedings of the AAAI conference on artificial intelligence},
  volume={32},
  number={1},
  year={2018}
}
...提出了相关方法。
@article{yang2016semi,
  title={Semi-supervised near-miss fall detection for ironworkers with a wearable inertial measurement unit},
  author={Yang, Kanghyeok and Ahn, Changbum R and Vuran, Mehmet C and Aria, Sepideh S},
  journal={Automation in construction},
  volume={68},
  pages={194--202},
  year={2016},
  publisher={Elsevier}
}
...进一步讨论了这一问题。
@inproceedings{stikic2009multi,
  title={Multi-graph based semi-supervised learning for activity recognition},
  author={Stikic, Maja and Larlus, Diane and Schiele, Bernt},
  booktitle={2009 international symposium on wearable computers},
  pages={85--92},
  year={2009},
  organization={IEEE}
}
...中也有相关研究。
@inproceedings{stikic2008exploring,
  title={Exploring semi-supervised and active learning for activity recognition},
  author={Stikic, Maja and Van Laerhoven, Kristof and Schiele, Bernt},
  booktitle={2008 12th IEEE International Symposium on Wearable Computers},
  pages={81--88},
  year={2008},
  organization={IEEE}
}
...进行了深入研究。
@inproceedings{ma2019labelforest,
  title={LabelForest: Non-parametric semi-supervised learning for activity recognition},
  author={Ma, Yuchao and Ghasemzadeh, Hassan},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={33},
  number={01},
  pages={4520--4527},
  year={2019}
}
...中也涉及这一问题。
@inproceedings{wiechert2016evolutionary,
  title={Evolutionary semi-supervised rough categorization of brain signals from a wearable headband},
  author={Wiechert, Glavin and Triff, Matt and Liu, Zhixing and Yin, Zhicheng and Zhao, Shuai and Zhong, Ziyun and Lingras, Pawan},
  booktitle={2016 IEEE Congress on Evolutionary Computation (CEC)},
  pages={3131--3138},
  year={2016},
  organization={IEEE}
}
"""
#
bibtex_pattern = re.compile(r'@[\w]+\{(?:[^{}]|\{[^{}]*\})*\}', re.DOTALL)

# Find all BibTeX entries in the text
bibtex_entries = bibtex_pattern.findall(input_text)

# Save the BibTeX entries to a text file
with open('DataFiles/results/extracted_bibtex.txt', 'w', encoding='utf-8') as file:
    for entry in bibtex_entries:
        file.write(entry + '\n\n')

len(bibtex_entries)  # Output the number of extracted entries
