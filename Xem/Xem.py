# 自用的文献管理工具
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os

import sys
import subprocess


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

window = tk.Tk()
# 设置窗口大小
winWidth = 1200
winHeight = 800
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

labels = [item for item in label_d]
vars = []
menus = []
path = tk.StringVar()
path.set('D:/jianguoyun/works/zotero')
row_ = 2


# 添加下拉菜单
def addMenu():
    global row_
    var = tk.StringVar()
    var.set('选择分类')
    row_ += 1
    menu = tk.OptionMenu(window, var, *labels).grid(row=row_,column=0)
    vars.append(var)
    menus.append(menu)

# 选择路径
def selectPath():
    path_ = askdirectory()
    path.set(path_)

# 点击打开文献
def clickTable(event, tree):
    for item in tree.selection():
        row = tree.item(item, 'values')
        pdfPath = row[-1]
        # exePath = r'C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe'
        os.startfile(pdfPath)

def sortTable(tree, col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    l.sort(reverse=reverse)
    for index,(val, k) in enumerate(l):
        tree.move(k, '', index)


# 根据条件检索论文
def catchMenu():
    global row_
    path_ = path.get()
    titles = []
    date_create = []
    date_find = []
    survey = []
    pathes = []
    for file in os.listdir(path_):
        if os.path.splitext(file)[1] == '.pdf':
            pdfPath = os.path.normpath(os.path.join(path_, file))
            split_ = file.split(' ')
            pref = split_[0]
            title = ' '.join(split_[1:])
            attrs = pref.split('-')
            flag = True
            for var in vars:
                label = var.get()
                if not label_d[label] in attrs[0]:
                    flag = False
                    break
            if flag:
                # 符合要求的文献
                titles.append(title)
                date_create.append(attrs[1])
                date_find.append(attrs[2])
                pathes.append(pdfPath)
                if len(attrs) > 3:
                    survey.append('是')
                else:
                    survey.append('否')
    columns = ('序号', '发表时间', '搜集时间', '标题', '是否综述', '路径')
    ybar = tk.Scrollbar(window, orient='vertical')
    treeview = ttk.Treeview(window, height=18, show='headings', columns=columns, yscrollcommand=ybar.set)
    ybar['command'] = treeview.yview
    treeview.column(columns[0], width=30, anchor='center')
    treeview.column(columns[1], width=100, anchor='center')
    treeview.column(columns[2], width=100, anchor='center')
    treeview.column(columns[3], width=600, anchor='center')
    treeview.column(columns[4], width=100, anchor='center')
    treeview.column(columns[5], width=10, anchor='center')
    for item in columns:
        treeview.heading(item, text=item)
    tk.Label(window, text='共计{}篇文献'.format(len(titles))).grid(row=row_+1, column=1)
    treeview.grid(row=row_+2, column=1)
    ybar.grid(row=row_+2, column=2, sticky='ns')
    tk.Button(window, text='发表时间', width=10, pady=5, command=lambda:sortTable(treeview, '发表时间', False)).grid(row=row_+3, column=1)
    tk.Button(window, text='搜集时间', width=10, pady=5, command=lambda:sortTable(treeview, '搜集时间', False)).grid(row=row_+4, column=1)
    for i in range(len(titles)):
        treeview.insert('', i, values=(i+1, date_create[i], date_find[i], titles[i], survey[i], pathes[i]))
    treeview.bind('<ButtonRelease-1>', lambda event:clickTable(event, treeview))
                    


tk.Label(window, text='目标路径：').grid(row=0, column=0)
tk.Entry(window, textvariable=path).grid(row=0, column=1)
tk.Button(window, text='选择路径', width=10, pady=5, command=selectPath).grid(row=0, column=2)
tk.Button(window, text='新增条件', width=10, pady=5, command=addMenu).grid(row=2, column=0)
tk.Button(window, text='搜索', width=10, pady=5, command=catchMenu).grid(row=1, column=0)   

window.mainloop()