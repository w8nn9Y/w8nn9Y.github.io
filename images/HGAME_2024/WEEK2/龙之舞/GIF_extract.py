#coding=utf-8
from PIL import Image
import os

GIF_name = "dragon.gif"
GIF = Image.open(GIF_name)
GIF_dir = GIF_name[:-4] + "_BreakDown"  #[:-4]返回从开头到倒数第五个字符的内容

if not os.path.exists(GIF_dir):
    os.mkdir(GIF_dir)

try:
    while True:
        GIF_current = GIF.tell()  #开始为0帧 tell()返回当前帧数
        GIF.save(GIF_dir + "\\" + str(GIF_current) + ".png")  #python中两\\表示一\
        GIF.seek(GIF_current + 1)
except EOFError:  #EOFError是Python中的一个异常类型，表示在读取输入时已经到达了文件的末尾
    pass  #pass是空语句，用于保持结构的完整性，不做任何事
