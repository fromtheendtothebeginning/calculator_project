from Level import *
from stack import Stack

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

        self.product=self.run_num(self.string)

        super(MainLevel,self).equal()

    def cut(self,string):
        # 分割string为数字+符号
        list=[]
        st=''
        for i in string:
            if '0'<=i<='9' or i=='.':
                st+=i
            else:
                list.append(float(st))
                list.append(i)
                st = ''
        list.append(float(st))

        return list

    def run_num(self,string):
        #运算函数
        while self.find_least(string):
            apart_string = string[self.least[0]+1:self.least[1]]
            print(self.calculator(apart_string))
            if self.calculator(apart_string) != '#' :
                apart_string = self.calculator(apart_string)
            else:
                print('error:there is a 0 under the /')
                return '0'
            string=self.instad(string,apart_string)
            print(apart_string)
            print(string)

        if self.calculator(string) != '#' :
            string = self.calculator(string)
            return string
        else:
            print('error:there is a 0 under the /')
            return '0'
        

    def calculator(self,string):
        #运算最小式
        list = self.cut(string)
            
        while len(list) != 1 :
            
            newlist=[]
            newlist_point=-1
            i=0
            while i<len(list):
                if list[i] == '*':
                    newlist[newlist_point]=list[i-1]*list[i+1]
                    i+=2
                
                elif list[i] == '/':
                    if list[i+1] == 0 :
                        return '#'
                    newlist[newlist_point]=list[i-1]/list[i+1]
                    i+=2
                else:
                    newlist.append(list[i])
                    newlist_point+=1
                    i+=1
            list=newlist
                
            newlist=[]
            newlist_point=-1
            i=0
            while i<len(list):
                if list[i] == '+':
                    newlist[newlist_point]=list[i-1]+list[i+1]
                    i+=2
                elif list[i] == '-' :
                    newlist[newlist_point]=list[i-1]-list[i+1]
                    i+=2
                else :
                    newlist.append(list[i])
                    newlist_point+=1
                    i+=1

            list = newlist
            
                    
        restring = str(list[0])
        print(restring)

        return restring
        
    def instad(self,string,apart_string):
        #将string的一部分替换为apart_string
        restring=''
        i=0
        while i<len(string):
            if i<self.least[0] or i>self.least[1]:
                restring+=string[i]
                i+=1
            else :
                restring+=apart_string
                i+=self.least[1]-self.least[0]+1
        
        return restring

    def find_least(self,string):
        # 寻找最小括号
        if string == '':
            return False
        
        stack_left=Stack(none_type=0)
        stack_right=Stack(none_type=0)
        for i in range(len(string)):
            if string[i]=='(' or string[i]==')' :
                stack_left.add(i)
        
        while string[stack_left.show()]!='(' and (not stack_left.if_none()) :
            stack_right.add(stack_left.out())

        if stack_left.if_none() : 
            return False
        else:
            self.least = [stack_left.show(),stack_right.show()]
            return True 

            

        