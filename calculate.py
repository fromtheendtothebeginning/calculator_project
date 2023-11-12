
class Calculator():
    def __init__(self,Str):
        
        if Str[0]=='-':                     #整个程序的点睛之笔，处理算式的第一个字符是减号
            self.equation='0'+Str
        else:                                           
            self.equation=Str

    def calculate_num(self):
        
        def remove_parenthesis(Str):
            head_p=0
            tail_p=0
            lenth=len(Str)
            no_parenthesis_equation=''
            while tail_p!=lenth:
                if (Str[tail_p]!="(")and(Str[tail_p]!=")"):         #去括号的函数
                    tail_p+=1
                elif Str[tail_p]=="(":
                    head_p=tail_p
                    tail_p+=1
                elif Str[tail_p]==")":
                    no_parenthesis_equation=Str[head_p+1:tail_p]
                    return (no_parenthesis_equation,head_p,tail_p+1)
                
        def Local_calculate(local_str):

            def Deal_with_numbers(local_str):
                lst=[]
                head_num_p=0
                tail_num_p=0
                i=0
                while i<len(local_str):
                  
                    if ((local_str[i]=="-")and('0'<=local_str[i+1]<='9')
                        and local_str[i-1]in['*','/','+','-'])or('0'<=local_str[i]<="9" or local_str[i]=='.'):
                        head_num_p=tail_num_p=i#史上最长的if语句!(^_^)!
                        a=i
                        while ('0'<=local_str[a+1]<="9" or local_str[a+1]=='.' )if a+1<len(local_str) else False:
                            tail_num_p+=1
                            a+=1
                        lst.append(float(local_str[head_num_p:tail_num_p+1]))
                        i=tail_num_p+1
                    else:
                        lst.append(local_str[i])
                        i+=1
                return lst
            def find_Multiplication_Division_replace(lst):#处理乘法和除法

                    for i in range(len(lst)):
                        if lst[i]=="*":
                            if i+2<len(lst):
                                lst[i-1:i+2]=[lst[i-1]*lst[i+1]]
                            else:
                                lst[i-1:]=[lst[i-1]*lst[i+1]]
                            return lst
                        elif lst[i]=="/":
                            if i+2<len(lst):
                                lst[i-1:i+2]=[lst[i-1]/lst[i+1]]
                            else:
                                if lst[i+1]!=0:
                                    lst[i-1:]=[lst[i-1]/lst[i+1]]
                                else :
                                    lst[i-1:]=0
                                    print('Error:0 under /')
                            return lst

            def find_Addition_Subtraction_replace(lst):
                for i in range(len(lst)):
                        if lst[i]=="+":
                            if i+2<len(lst):
                                lst[i-1:i+2]=[lst[i-1]+lst[i+1]]
                            else:
                                lst[i-1:]=[lst[i-1]+lst[i+1]]
                            return lst
                        elif lst[i]=="-":
                            if i+2<len(lst):
                                lst[i-1:i+2]=[lst[i-1]-lst[i+1]]
                            else:
                                lst[i-1:]=[lst[i-1]-lst[i+1]]
                            return lst
            lst=Deal_with_numbers(local_str)
            while "*"in lst  or "/"in lst:                      #先算乘除再算加减 !-_-
                lst=find_Multiplication_Division_replace(lst)
            while "+"in lst or "-"in lst:
                lst=find_Addition_Subtraction_replace(lst)
            return str(lst)[1:-1]
        while "(" in self.equation:
            no_parenthesis_equation,left_p,right_p=remove_parenthesis(self.equation)
            # print(self.equation)
            self.equation=self.equation[:left_p]+Local_calculate(no_parenthesis_equation)+self.equation[right_p:]
        self.equation=Local_calculate(self.equation)
        # print(self.equation)
        
        return self.equation
        
# if __name__=='__main__':         
#     Str="-1+5*(1+2*(1+2*(5+-16)+(1+7*9)+40)+(50*40+1))*4+12*4/(1+2.534)-1*(1-2.1)/21.43" #<----------算式
#     a=Calculator(Str)
#     a.calculate_num()

