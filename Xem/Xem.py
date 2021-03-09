# 自用的文献管理工具
import tkinter as tk
from tkinter import ttk
label_d = {
    '零样本': 'Z',
    '多模态': 'M',
    '文本': 't',
    '图像': 'i',
    '音频': 'a',
    '情感计算': 'E',
    '视频': 'v',
    '分类': 'C',
    '机器学习': 'L',
    '检索': 'R',
    '风格转换': 'N',
    '预训练': 'P',
}
labels = [item for item in label_d]
# 下拉菜单列表
menus = []

window = tk.Tk()
# 设置窗口大小
winWidth = 600
winHeight = 400
# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
# 设置主窗口标题
window.title("Xem")
# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口宽高固定
window.resizable(0, 0)

# 添加下拉菜单
def addMenu():
    var = tk.StringVar()
    var.set('选择分类')
    menu = tk.OptionMenu(window, var, *labels).pack()
    menus.append(var)

# 根据条件检索论文
def catchMenu():
    


tk.Button(window, text='新增条件', width=10, pady=5, command=addMenu).pack()
tk.Button(window, text='搜索', width=10, pady=5, command=catchMenu).pack()   

window.mainloop()