import pandas as pd
import matplotlib.pyplot as plt
import os

# 获取当前脚本所在目录的路径
script_directory = os.path.dirname(os.path.abspath(__file__))

# 定义输出文件夹路径
output_directory = os.path.join(script_directory, 'output')

# 创建输出文件夹（如果不存在）
os.makedirs(output_directory, exist_ok=True)

# 读取Excel文件
file_path = "output/log_data.xlsx"
df = pd.read_excel(file_path)

# 获取X轴和Y轴数据
x = df.iloc[:, 0]  # 第一列数据
y = df.iloc[:, 1]  # 第二列数据

# 创建点图
plt.figure(figsize=(10, 6), num="点图效果预览")
plt.scatter(x, y, marker='o', label='date', color='c')

# 设置标题和标签
plt.title('point for distance and Power(mW)')
plt.xlabel('distance')  # 设置X轴标签
plt.ylabel('Power(mW)')  # 设置Y轴标签

# 添加坐标轴标签（小字体）
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# 保存点图为.jpg格式
plt.savefig('output/point.jpg', dpi=1000)

# 显示图
plt.show()

# 创建折线图
plt.figure(figsize=(10, 6), num="折线图效果预览")
plt.plot(x, y, marker='*', linestyle='-', label='Line', linewidth=1)

# 设置标题和标签
plt.title('Line for distance and Power(mW)')
plt.xlabel('distance')  # 设置X轴标签
plt.ylabel('Power(mW)')  # 设置Y轴标签

# 添加坐标轴标签（小字体）
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# 保存折线图为.jpg格式
plt.savefig('output/line.jpg', dpi=1000)

# 显示图像
plt.show()
