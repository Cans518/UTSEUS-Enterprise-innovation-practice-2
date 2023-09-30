import tkinter as tk
import subprocess
import tkinter.messagebox as messagebox
import ctypes
import os

# 设置DPI_AWARE选项以提高清晰度
ctypes.windll.shcore.SetProcessDpiAwareness(1)


def open_output_folder():
    output_folder = "output"
    if os.path.exists(output_folder):
        subprocess.Popen(["explorer", output_folder], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        messagebox.showwarning("警告", "找不到output文件夹！")


def run_script1():
    try:
        result = subprocess.run(["python", "date.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                creationflags=subprocess.CREATE_NO_WINDOW)
        if result.returncode == 0:
            messagebox.showinfo("运行成功", "数据读取成功！")
        else:
            messagebox.showerror("运行失败", "数据读取失败！")
    except Exception as e:
        messagebox.showerror("运行错误", str(e))


def run_script2():
    try:
        result = subprocess.run(["python", "draw.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                creationflags=subprocess.CREATE_NO_WINDOW)
        if result.returncode == 0:
            messagebox.showinfo("运行成功", "点图、折线图绘图成功！")
        else:
            messagebox.showerror("运行失败", "绘图失败！")
    except Exception as e:
        messagebox.showerror("运行错误", str(e))


def run_script3():
    try:
        result = subprocess.run(["python", "fonctionfit.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                creationflags=subprocess.CREATE_NO_WINDOW)
        if result.returncode == 0:
            messagebox.showinfo("运行成功", "拟合函数成功！")
        else:
            messagebox.showerror("运行失败", "拟合函数失败！")
    except Exception as e:
        messagebox.showerror("运行错误", str(e))


# 创建主窗口
root = tk.Tk()
root.title("第五组工具")

# 获取屏幕宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口大小
window_width = 510
window_height = 300

# 计算窗口位置使其位于屏幕中心
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# 使用geometry方法设置窗口大小和位置
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 添加标题标签
title_label = tk.Label(root, text="欢迎使用第五组数据处理工具", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

# 添加使用提示标签
tip_label = tk.Label(root, text="请依次单击按钮运行使用\n出现预览，确认无误后关闭窗口即可", font=("Helvetica", 12))
tip_label.grid(row=2, column=0, columnspan=3, padx=20, pady=10)

# 添加作者标签
tip_label = tk.Label(root, text="code by Mzee", font=("Helvetica", 8))
tip_label.grid(row=3, column=2, columnspan=2, padx=10, pady=5, sticky="se")

# 创建按钮
# 按钮一，打开date.py
button1 = tk.Button(root, text="获取数据", command=run_script1)
button1.grid(row=1, column=0, padx=18, pady=12)

# 按钮二，打开draw.py
button2 = tk.Button(root, text="绘制点图", command=run_script2)
button2.grid(row=1, column=1, padx=18, pady=12)

# 按钮三，打开fonctionfit.py
button3 = tk.Button(root, text="拟合函数", command=run_script3)
button3.grid(row=1, column=2, padx=18, pady=12)

# 添加打开输出文件夹按钮
open_folder_button = tk.Button(root, text="打开输出文件夹", command=open_output_folder)
open_folder_button.grid(row=3, column=1, padx=15, pady=10)

# 设置按钮样式
button1.configure(bg="#4CAF50", fg="white", font=("Helvetica", 14))
button2.configure(bg="#FFC107", fg="black", font=("Helvetica", 14))
button3.configure(bg="#FF5722", fg="white", font=("Helvetica", 14))
open_folder_button.configure(bg="#2196F3", fg="white", font=("Helvetica", 12))

# 启动图形化界面
root.mainloop()
