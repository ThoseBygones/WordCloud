# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 10:11:46 2018

@author: Sherlock Holmes
"""

# 导入处理图像的库
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import os

# 程序图形化窗体类
class GraphicInterface(Frame):
    # 构造函数
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    # 图片大小调整函数
    def resize(self, widget_w, widget_h, image):
        #获取图片的原始大小 
        w, h = image.size
        f1 = 1.0 * widget_w / w   
        f2 = 1.0 * widget_h / h      
        factor = min([f1, f2])     
        width = int(w * factor)      
        height = int(h * factor)      
        return image.resize((width, height), Image.ANTIALIAS)
    
    # 创建窗体的函数
    def createWidgets(self):
        # 窗体标题
        self.master.title('《全球通史》词云图')
        # 设置窗体的几何大小
        self.master.geometry('800x600')
        # 设置窗体不可被改变大小
        self.master.resizable(width=False, height=False)
        # 加载图片
        self.img = Image.open(r'wc.png')
        self.reszimg = self.resize(800, 600, self.img)
        self.img = ImageTk.PhotoImage(self.reszimg)    
        
        # 提示文本
        self.label = Label(self.master, text="《全球通史》词云图")
        self.label.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        # 显示图片
        self.image = Label(self.master, image=self.img)
        self.image.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        self.pack(expand=1, fill="both")

# 解析背景图片
bgpic = imread('bgpic.jpg')

wc = WordCloud(
        # 设置背景颜色
        background_color = 'white',
        # 设置最大词数
        max_words = 1000,
        # 以该背景图作图绘制词云
        mask = bgpic,
        # 显示字体的最大值
        max_font_size = 80,
        # 选定字体，解决乱码问题
        font_path = "C:/Windows/Fonts/msyh.ttc",
        # 为每个词返回一个PIL颜色
        random_state = 42
        )

# 打开词源的文本文件
text = open('qqts.txt').read()
# 制作词云
wc.generate(text)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(bgpic)
# 以原图颜色重新绘制词云
wc.recolor(color_func=image_colors)
# 显示图片
#plt.imshow(wc)
# 关闭坐标轴
#plt.axis('off')
# 绘制词云
#plt.figure()
# 以原图颜色重新绘制词云
#plt.imshow(wc.recolor(color_func=image_colors))
# 关闭坐标轴
#plt.axis('off')
# 导出到文件
wc.to_file('wc.png')
print("制作完成！")
# 实例化窗体类
gui = GraphicInterface()
# 主消息循环:
gui.mainloop()