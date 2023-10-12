@echo off
chcp 65001
echo 正在安装 Python 包...
echo 请稍等...

:: 安装 matplotlib
pip install matplotlib

:: 安装 pandas
pip install pandas

:: 安装 numpy
pip install numpy

echo.
echo Python 包安装完成。

:: 暂停以等待用户确认
pause
