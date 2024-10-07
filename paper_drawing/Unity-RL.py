import numpy as np
from matplotlib import pyplot as plt


def draw_pose_waypoints():
    def vis_rotation():
        # 定义读取文件函数
        def read_poses(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            poses = []
            for line in lines:
                pose = np.array(list(map(float, line.strip().split()))).reshape(3, 4)
                poses.append(pose)
            return np.array(poses)

        # 选择一段数据的函数
        def select_segment(poses, indices):
            return poses[indices]

        # 读取 Ground Truth 和 KCANet 数据
        poses_ref = read_poses('F:\Toky\PythonProject\Toky-Personal-Process\Resources\poses_GroundTruth-part1.txt')

        # 定义归一化函数
        def normalize(matrix):
            norm_matrix = matrix.copy()
            for i in range(3):
                norm_matrix[:3, i] /= np.linalg.norm(matrix[:3, i])
            return norm_matrix

        # 可视化函数
        def plot_rotations(poses_ref, segment_indices):
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            # 设置箭头参数
            arrow_params = {'length': 12.0, 'arrow_length_ratio': 0.5, 'linewidth': 2, 'alpha': 0.9}

            for i in segment_indices:
                ref = poses_ref[i]
                # 获取平移部分
                t_ref = ref[:3, 3]
                # 归一化
                ref = normalize(ref)
                # 绘制参考旋转轴
                ax.quiver(t_ref[0], t_ref[1], t_ref[2], ref[0, 0], ref[1, 0], ref[2, 0], color='blue', linestyle='-',
                          label='Ref X' if i == segment_indices[0] else "", **arrow_params)
                ax.quiver(t_ref[0], t_ref[1], t_ref[2], ref[0, 1], ref[1, 1], ref[2, 1], color='magenta', linestyle='-',
                          label='Ref Y' if i == segment_indices[0] else "", **arrow_params)
                ax.quiver(t_ref[0], t_ref[1], t_ref[2], ref[0, 2], ref[1, 2], ref[2, 2], color='red', linestyle='-',
                          label='Ref Z' if i == segment_indices[0] else "", **arrow_params)
                # 在原点添加标记
                ax.scatter(t_ref[0], t_ref[1], t_ref[2], color=(0, 1, 0), marker='o', s=100,
                           label='GT' if i == segment_indices[0] else "")
            # 标记起点和终点
            start_ref = poses_ref[segment_indices[0]][:3, 3]
            end_ref = poses_ref[segment_indices[-1]][:3, 3]

            ax.scatter(start_ref[0], start_ref[1], start_ref[2], color='black', marker='o', s=100)
            ax.scatter(end_ref[0], end_ref[1], end_ref[2], color='black', marker='o', s=100)

            # 设置坐标轴
            ax.set_xlim([-20, 20])
            ax.set_ylim([-20, 20])
            ax.set_zlim([-20, 20])
            ax.set_xlabel('X')
            # ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            # 隐藏坐标轴和网格
            ax.set_axis_off()
            # 添加图例
            handles, labels = ax.get_legend_handles_labels()
            by_label = dict(zip(labels, handles))
            ax.legend(by_label.values(), by_label.keys())
            plt.show()

        # 定义稀疏采样，保留50个姿态，并进行排序
        num_samples = 10
        sampled_indices = np.random.choice(len(poses_ref), size=num_samples, replace=False)
        sampled_indices.sort()  # 将采样的索引进行排序

        # 定义拆分数组，设置每段的长度
        segment_length = num_samples
        num_segments = len(sampled_indices) // segment_length

        for i in range(num_segments):
            segment_indices = sampled_indices[i * segment_length:(i + 1) * segment_length]
            plot_rotations(poses_ref, segment_indices)

    vis_rotation()

if __name__ == '__main__':
    draw_pose_waypoints()