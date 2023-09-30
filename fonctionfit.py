import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# 获取当前脚本所在目录的路径
script_directory = os.path.dirname(os.path.abspath(__file__))

# 定义输出文件夹路径
output_directory = os.path.join(script_directory, 'output')

# 创建输出文件夹（如果不存在）
os.makedirs(output_directory, exist_ok=True)

# 读取Excel文件
file_path = "output/log_data.xlsx"
df = pd.read_excel(file_path)

# 获取第一列和第二列数据
x = df.iloc[:, 0].values
y = df.iloc[:, 1].values

# 设置差距过大的阈值（可根据实际情况调整）
threshold = 20.0

# 找到差距过大的点的索引并删除
valid_indices = np.where(np.abs(y - np.polyval(np.polyfit(x, y, 3), x)) < threshold)
x_filtered = x[valid_indices]
y_filtered = y[valid_indices]

# 多项式拟合
degree = 8  # 设置多项式的阶数，可以根据需要调整 ，这里设置为8
coeffs = np.polyfit(x_filtered, y_filtered, degree)  # 利用现有库进行多项式拟合

# 创建多项式对象
polynomial = np.poly1d(coeffs)

# 生成拟合后的 y 值
y_fit = polynomial(x_filtered)

# 绘制原始数据的散点图
plt.figure(figsize=(10, 6), num="拟合结果预览")
plt.scatter(x_filtered, y_filtered, label="date", color='c', marker='o', s=10, alpha=0.8)

# 绘制折线图
plt.plot(x, y, marker=',', linestyle='-', label='Line', linewidth=1)

# 绘制多项式拟合的函数曲线
x_curve = np.linspace(min(x_filtered), max(x_filtered), 10000)  # 生成更多点以绘制平滑的曲线
y_curve = polynomial(x_curve)
plt.plot(x_curve, y_curve, label=f"polynomial-fit", color='red', linewidth=1.3)

# 添加标签和图例
plt.xlabel("distance")
plt.ylabel("Power(mW)")
plt.title(f"polynomial-fit (degree = {degree})")
plt.legend()

# 处理数组，保留两位小数
coeffs = np.round(coeffs, decimals=2)

# 创建一个新的数组，其中正数前面添加加号
coeffs = np.array(["+" + str(x) if x > 0 else str(x) for x in coeffs])

# 使用Latex渲染输出拟合的多项式
plt.text(0.03, 0.04,
         fr"$y={coeffs[0]}x^{8}{coeffs[1]}x^{7}{coeffs[2]}x^{6}{coeffs[3]}x^{5}{coeffs[4]}x^{4}{coeffs[5]}x^{3}{coeffs[6]}x^{2}{coeffs[7]}x{coeffs[8]}$",
         transform=plt.gca().transAxes, color='r', fontsize=13, usetex=True)

# 保存图形为.jpg文件
plt.savefig("output/polynomial_fit.jpg", dpi=1000)

# 显示图形
plt.show()
