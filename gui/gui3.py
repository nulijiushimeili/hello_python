"""
Script introduction: 
    使用tkinter创建GUI
        -- 在窗口上制作动画

@Time :       2018-08-07 21:21
@Author :     nulijiushimeili
@Site :       
@File :       gui3.py
@Software :   PyCharm
"""

import tkinter as tk


# 播放动画效果的函数
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    top.after(50, play_animation)


x = 10
y = 10
top = tk.Tk()
top.geometry("600x600")
top.title("动画")
top.resizable(False, False)
top.wm_attributes("-topmost", 1)
canvas = tk.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 600, 600, fill="gray")
oval = canvas.create_oval(10, 10, 60, 60, fill="red")
canvas.pack()
top.update()
play_animation()
tk.mainloop()
