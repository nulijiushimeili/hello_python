"""
Script introduction: 
    使用tkinter创建GUI
        -- 顶层窗口
        -- 控件
        -- 布局
        -- 事件回调

@Time :       2018-08-07 20:19
@Author :     nulijiushimeili
@Site :       
@File :       gui1.py
@Software :   PyCharm
"""

import tkinter
import tkinter.messagebox


def func():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') \
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel("温馨提示:", "确定要退出吗?"):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口的大小
    top.geometry("240x160")
    # 设置窗口的标题
    top.title("Game")
    # 创建标签对象
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象
    button1 = tkinter.Button(panel, text="Modify", command=change_label_text)
    button1.pack(side="left")
    button2 = tkinter.Button(panel, text="Quit", command=confirm_to_quit)
    button2.pack(side="right")
    panel.pack(side="bottom")
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == "__main__":
    func()
