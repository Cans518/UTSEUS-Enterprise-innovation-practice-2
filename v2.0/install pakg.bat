@echo off
chcp 65001
echo 正在安装 Python 依赖包...
echo 请稍等...

:: 安装 matplotlib
pip install matplotlib

:: 安装 pandas
pip install pandas

:: 安装 numpy
pip install numpy

:: 安装 openpyxl
pip install openpyxl

:: 安装 subprocess
pip install subprocess

:: 安装 tkinter
pip install tkinter

:: 安装 ctypes
pip install ctypes

:: 安装 os
pip install os

:: 安装 re
pip install re

echo.
echo Python 依赖包安装完成。

:: 暂停以等待用户确认
pause
