import tkinter as tk
from tkinter.messagebox import *
from stack import *

class Level:
    def __init__(self,win):

        self.win = win
        self.string = ''                    #输入运算式
        self.stringvar = tk.StringVar()     #绑定self.entry_item
        self.stringvar.set(self.string)
        
        self.product = '0'                  #结果
        self.productvar = tk.StringVar()    #绑定self.product_entry
        self.productvar.set(self.product)

        self.if_nonnum = Stack(100,True)    #建栈，加入元素为是否是运算符
        self.if_left_or_right = Stack(100)  #建栈，加入元素为左右括号
        self.if_right = Stack(100,False)    #建栈，是否为右括号

    def win_item(self):
        self.entry().button()

        return self

    def entry(self):
        self.entry_item = tk.Entry(self.win,textvariable=self.stringvar,bd=5)
        self.entry_item.place(x=20,y=10,width=140,height=40)
        self.product_entry = tk.Entry(self.win,textvariable=self.productvar,bd=5)
        self.product_entry.place(x=170,y=10,width=40,height=40)
        return self

    def button(self):
        #加减乘除键
        self.times_button = tk.Button(self.win,text='*',command=self.times).place(x=20,y=70,width=40,height=40)
        self.divide_button = tk.Button(self.win,text='/',command=self.divide).place(x=70,y=70,width=40,height=40)
        self.puls_button = tk.Button(self.win,text='+',command=self.plus).place(x=120,y=70,width=40,height=40)
        self.subtruct_button = tk.Button(self.win,text='-',command=self.subtruct).place(x=170,y=70,width=40,height=40)

        #数字键
        self.num1_button = tk.Button(self.win,text='1',command=self.num1).place(x=20,y=220,width=40,height=40)
        self.num2_button = tk.Button(self.win,text='2',command=self.num2).place(x=70,y=220,width=40,height=40)
        self.num3_button = tk.Button(self.win,text='3',command=self.num3).place(x=120,y=220,width=40,height=40)
        self.num4_button = tk.Button(self.win,text='4',command=self.num4).place(x=20,y=170,width=40,height=40)
        self.num5_button = tk.Button(self.win,text='5',command=self.num5).place(x=70,y=170,width=40,height=40)
        self.num6_button = tk.Button(self.win,text='6',command=self.num6).place(x=120,y=170,width=40,height=40)
        self.num7_button = tk.Button(self.win,text='7',command=self.num7).place(x=20,y=120,width=40,height=40)
        self.num8_button = tk.Button(self.win,text='8',command=self.num8).place(x=70,y=120,width=40,height=40)
        self.num9_button = tk.Button(self.win,text='9',command=self.num9).place(x=120,y=120,width=40,height=40)
        self.num0_button = tk.Button(self.win,text='0',command=self.num0).place(x=70,y=270,width=40,height=40)
        
        self.dot_button = tk.Button(self.win,text='.',command=self.dot).place(x=170,y=220,width=40,height=40)

        #左右括号
        self.left_button = tk.Button(self.win,text='(',command=self.left).place(x=20,y=270,width=40,height=40)
        self.right_button = tk.Button(self.win,text=')',command=self.right).place(x=120,y=270,width=40,height=40)

        '''
        ac清除键
        del删除键
        =输出结果
        '''
        self.ac_button = tk.Button(self.win,text='AC',command=self.ac).place(x=170,y=170,width=40,height=40)
        self.deleter_button = tk.Button(self.win,text='del',command=self.deleter).place(x=170,y=120,width=40,height=40)
        self.equal_button = tk.Button(self.win,text='=',command=self.equal).place(x=170,y=270,width=40,height=40)

        return self
    
    def dot(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '.'
            self.if_right.add(False)
            self.stringvar.set(self.string)
            if self.if_nonnum.show():
                self.num0()

        return

    def equal(self):
        '''
        这里将式子self.string转为结果self.product
        还要求将结果输入给self.product_entry
        '''

        if self.string[-1] == '.':
                self.num0()
        self.productvar.set(self.product)

        return 

    def clear(self):
        if self.if_nonnum.show() :
            self.string = self.string[:len(self.string)-1]

        return self

    def deleter(self):
        self.if_right.out()
        self.string = self.string[:len(self.string)-1]
        self.if_left_or_right = Stack(100)
        for i in self.string:
            if i=='(':
                self.if_left_or_right.add('(')
            elif i==')':
                self.if_left_or_right.out()
        self.if_nonnum.out()
        self.stringvar.set(self.string)

    def ac(self):
        self.if_nonnum = Stack(100,True)
        self.if_left_or_right = Stack(100)
        self.if_right = Stack(100,False)
        self.string = ''
        self.stringvar.set(self.string)

        return

    def times(self):
        self.string = self.entry_item.get()
        self.clear()
        self.if_nonnum.add(True)
        self.if_right.add(False)
        if self.string[-1] == '.':
            self.num0()
        self.string += '*'
        
        if self.string == '':
            self.clear()
        
        self.stringvar.set(self.string)

        return
    
    def divide(self):
        self.string = self.entry_item.get()
        self.clear()
        self.if_nonnum.add(True)
        self.if_right.add(False)
        if self.string[-1] == '.':
            self.num0()
        self.string += '/'
        
        if self.string == '':
            self.clear()
            
        self.stringvar.set(self.string)

        return
    
    def plus(self):
        self.string = self.entry_item.get()
        self.clear()
        self.if_nonnum.add(True)
        self.if_right.add(False)
        if self.string[-1] == '.':
            self.num0()
        self.string += '+'
        
        if self.string == '':
            self.clear()
            
        self.stringvar.set(self.string)

        return
    
    def subtruct(self):
        self.string = self.entry_item.get()
        self.clear()
        self.if_nonnum.add(True)
        self.if_right.add(False)
        if self.string[-1] == '.':
            self.num0()
        self.string += '-'
        
        if self.string == '':
            self.clear()
            
        self.stringvar.set(self.string)

        return
    
    def left(self):
        if self.if_nonnum.show() or self.if_left_or_right.show()=='(':
            self.string = self.entry_item.get()
            self.if_left_or_right.add('(')
            self.if_nonnum.add(False)
            self.string += '('
            self.stringvar.set(self.string)
            self.if_right.add(False)

        return
    
    def right(self):
        if not self.if_nonnum.show() and self.if_left_or_right.show()=='(':
            self.string = self.entry_item.get()
            self.if_left_or_right.out()
            self.if_nonnum.add(False)
            if self.string[-1] == '.':
                self.num0()
            self.string += ')'
            self.stringvar.set(self.string)
            self.if_right.add(True)

        return
    
    def num1(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '1'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num2(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '2'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num3(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '3'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num4(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '4'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num5(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '5'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num6(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '6'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num7(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '7'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num8(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '8'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num9(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '9'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
    def num0(self):
        if not self.if_right.show():
            self.string = self.entry_item.get()
            self.if_nonnum.add(False)
            self.string += '0'
            self.if_right.add(False)
            self.stringvar.set(self.string)

        return
    
      