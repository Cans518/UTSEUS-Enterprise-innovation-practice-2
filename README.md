# 第五组数据处理工具

## 仓库简述

> 本仓库内容为2023年上海大学中欧工程技术学院23年秋季学期`企业创新项目实战`课程的第二次课题项目的数据处理工具。

> 本工具完全使用`python`进行数据的读取与处理，使用`matplotlib`库做数据可视化，使用`pandas`、`re`和`openpyxl`进行文件的读写，使用`numpy`进行数据的处理，使用`subprocess`、`ctypes`、`tkinter`和`os`进行窗口UI的简单设计

**在使用本工具前请确保您的电脑上已经安装`python`和上面提到的软件包**

## 文件结构

本工具主体包含5个文件：

1. Run.py(集成以及UI实现脚本)
2. fonctionfit.py（函数拟合脚本）~~单词拼写错误~~
3. draw.py（数据点云图与折线图绘制脚本）
4. date.py（读取原始数据脚本）
5. Run me.bat（集成运行脚本）

本软件仅在`Windows 11`下运行测试过，如果是`Linux`或者`Mac`系统下使用，使用`python Run.py`运行脚本

## 使用说明

- 将工具本体的五个文件放到与数据文件同一目录下，双击运行`Run me.bat`依次运行`获取数据`、`绘制点图`和`拟合函数`就可以在同目录下得到一个`output`文件夹。
- 数据读取得到：`log_data.xlsx`；点图绘制得到：`point.jpg`点云图和`line.jpg`折线图；拟合函数得到：`polynomial_fit.jpg`
- 点击打开输出文件，就可以打开`output`文件夹

<div align=center><img src="https://mzee-imge.oss-cn-shanghai.aliyuncs.com/images/202309302353362.png" alt="image-20230930235300290" style="zoom:80%;" /></div>

<div align=center><img src="https://mzee-imge.oss-cn-shanghai.aliyuncs.com/images/202309302353906.png" alt="image-202309302353906" style="zoom:100%;" /></div>


