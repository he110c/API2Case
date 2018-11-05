# -*- coding: UTF-8 -*-
from Tkinter import *

class CasetoAPI(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("APItoCase".decode('gbk').encode('utf8'))
        self.root.geometry('960x540')
        self.frame_main = Frame(self.root)
        ##frame_top
        self.frame_top = Frame(self.frame_main)
        self.frame_top.pack(side = TOP)

        ##frame_top——左侧文字描述框
        self.frame_top_filepath = Frame(self.frame_top)
        self.frame_top_filepath.pack(side = TOP)
        self.label_filepath = Label(self.frame_top_filepath, text="文件路径:".decode('utf-8','replace').encode('utf-8'), bg="green", font=("Arial", 12), width=8, height=2)
        self.label_filepath.pack(side = LEFT) 
        self.var_filepath = StringVar()
        self.entry_filepath = Entry(self.frame_top_filepath, textvariable=self.var_filepath, width=50, font =("Arial", 12))
        self.entry_filepath.pack(side = RIGHT)
        ##frame_top——右侧输入框
        self.frame_top_regular = Frame(self.frame_top)
        self.frame_top_regular.pack(side = BOTTOM)
        self.label_regular = Label(self.frame_top_regular, text="URL 正则:".decode('utf-8','replace').encode('utf-8'), bg="green", font=("Arial", 12), width=8, height=2)
        self.label_regular.pack(side = LEFT) 
        self.var_regular = StringVar()
        self.entry_regular = Entry(self.frame_top_regular, textvariable=self.var_regular, width=50, font =("Arial", 12))
        self.entry_regular.pack(side = RIGHT)

        ##frame_middle
        self.frame_middle = Frame(self.frame_main)
        self.frame_middle.pack()
        
        ##frame_bottom
        self.frame_bottom = Frame(self.frame_main)
        self.frame_bottom.pack(side = BOTTOM)

        ##frame_main
        self.frame_main.pack()

def main():
    d = CasetoAPI()
    mainloop()
if __name__== "__main__":
    main()
