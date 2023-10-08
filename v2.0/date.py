import os
import pandas as pd
import re

# 获取脚本所在目录的路径
script_directory = os.path.dirname(os.path.abspath(__file__))

# 定义输出文件夹路径
output_directory = os.path.join(script_directory, 'output')

# 创建输出文件夹（如果不存在）
os.makedirs(output_directory, exist_ok=True)

# 定义输出Excel文件路径
output_excel_path = os.path.join(output_directory, 'log_data.xlsx')

# 创建一个空的DataFrame来存储数据
df_list = []

# 定义用于提取第四个小数的正则表达式
decimal_pattern = re.compile(r'Aver\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)')

# 遍历当前目录、父目录及其所有子目录中的所有.log文件
log_files = []
for root, dirs, files in os.walk(script_directory):
    for file in files:
        if file.endswith('.log'):
            log_files.append(os.path.join(root, file))

# 读取所有.log文件中的数据
for log_file_path in log_files:
    base_name = os.path.splitext(os.path.basename(log_file_path))[0]
    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()
        fourth_decimal = None
        for line in lines:
            elements = line.split()
            if len(elements) >= 5 and elements[0] == "Aver":
                fourth_decimal = float(elements[4]) / 10.0  # 小数除以10
                break
        df_list.append({'distance': base_name, 'W Width I': fourth_decimal})

# 将数据保存到Excel文件
df = pd.DataFrame(df_list)
df.to_excel(output_excel_path, index=False)

print(f"数据已保存到 {output_excel_path}")
