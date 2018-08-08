"""
Script introduction: 
    使用tkinter创建GUI
        -- 使用画布绘图
        -- 处理鼠标事件

    绘制五子棋的棋盘

@Time :       2018-08-07 20:55
@Author :     nulijiushimeili
@Site :       
@File :       gui2.py
@Software :   PyCharm
"""

import tkinter as tk


def window():
    def mouse_evt_handler(evt=None):
        row = round((evt.y - 20) / 40)
        col = round((evt.x - 10) / 40)
        pos_x = 40 * col
        pos_y = 40 * row
        canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill="black")

    top = tk.Tk()
    # 设置窗口的尺寸
    top.geometry("620x620")
    # 设置窗口标题
    top.title("Chessboard")
    # 设置窗口的大小不可改变
    top.resizable(False, False)
    # 设置窗口置顶
    top.wm_attributes("-topmost", 1)
    canvas = tk.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
    canvas.bind("<Button-1>", mouse_evt_handler)
    canvas.create_rectangle(0, 0, 600, 600, fill="#aaa", outline="white")
    for index in range(15):
        canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill="black")
        canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill="black")
    canvas.create_rectangle(15, 15, 585, 585, outline="black", width=4)
    canvas.pack()
    tk.mainloop()


if __name__ == "__main__":
    window()
