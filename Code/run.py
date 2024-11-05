import subprocess
import csv

# 定义消息和字母表
message = 'E1a0FVL6md0r6dsMx'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 打开 CSV 文件以写入结果
with open('decryption_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['Key', 'Decrypted_Message']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入CSV的头部
    writer.writeheader()

    # 遍历所有三位数字密钥（000到999）
    for key in range(1000):
        # 格式化密钥为三位数字的字符串
        key_str = str(key).zfill(3)

        # 构建调用 decode2.py 的命令
        command = [
            'python', 'decode2.py', '--decrypt',
            '--message=' + message,
            '--key=' + key_str,
            '--alphabet=' + alphabet
        ]

        # 使用 subprocess 来调用 decode2.py 并捕获输出
        result = subprocess.run(command, capture_output=True, text=True)

        # 获取解密后的消息
        decrypted_message = result.stdout.strip()

        # 将密钥和解密后的消息写入 CSV 文件
        writer.writerow({'Key': key_str, 'Decrypted_Message': decrypted_message})

        print(f"Key: {key_str}, Decrypted Message: {decrypted_message}")
