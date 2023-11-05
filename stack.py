class Stack:
    '''
    lenth为栈长度
    none_type为栈没有元素时show和out输出元素
    add为入栈
    show显示栈最上方元素
    out出栈并且输出元素
    '''
    def __init__(self,lenth=20,none_type='#'):
        self.list = ['#']*lenth
        self.top = -1
        self.none_type = none_type

    def add(self,x):
        self.top+=1
        self.list[self.top] = x

        return self

    def show(self):
        if self.top!=-1:
            return self.list[self.top]
        else:
            return self.none_type

    def out(self):
        if self.top!=-1:
            x = self.list[self.top]
            self.list[self.top] = '#' 
            self.top-=1
            return x
        else:
            return self.none_type

    def if_none(self):
        if self.top==-1 :
            return True
        else :
            return False
