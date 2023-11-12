from Level import *
from stack import Stack
from calculate import Calculator

class MainLevel(Level):
    def __init__(self, win):
        super().__init__(win)

    def equal(self):
        '''
        这里要求将式子self.string转为结果self.product
        例如self.string:'1+3*6*(3+2)'转换为结果self.product:'91'
        注意self.product为字符串型
        '''
        while self.if_nonnum.show() :
            self.clear()
            
        while self.if_left_or_right.top!=-1:
            if self.string[-1] == '.':
                self.num0()
            self.string+=')'                    #补充右括号
            self.stringvar.set(self.string)
            self.if_left_or_right.out()
            self.if_right.add(True)

        self.product=Calculator(self.string).calculate_num()
        

        super(MainLevel,self).equal()

    