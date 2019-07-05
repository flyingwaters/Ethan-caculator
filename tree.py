import tkinter as tk
# 导入tkinter库
root = tk.Tk()
root.title("Ethan's Calculator")
root.resizable(0, 0)
root.geometry('320x420')
# 设置界面


class GUICal:
    def __init__(self, cal):
        self.root = Tk()
        self.cal = cal
        self.root.title("Ethan的计算器")
        self.showInfo = StringVar()
        self.showInfo.set("0")
        self.showResult = StringVar()
        self.showResult.set("0")
        fm1 = Frame(self.root)
        Entry(fm1, textvariable=self.showInfo).grid(row=0,column=0, columnspan=4)
        Entry(fm1, textvariable=self.showResult).grid(row=1, column=0, columnspan=4)

    def getnum(num):
        temp = equation.get()
        temp2 = result.get()
        print(temp)
        print(temp2)
        if temp2 != ' ':
            temp = '0'
            temp2 = ' '
            result.set(temp2)
        if (temp == '0'):
            temp = ''
        temp = temp + num
        equation.set(temp)
        print(equation)

    def clear(self):
        self.showInfo = ""
        self.showResult = ""
        return[self.showInfo, self.showResult]

    def percent(self):
        s = self.showInfo[::-1]
        if s[0] in self.symbols:
            return [self.showText, "错误"]
        self.showInfo += "%"
        for i in range(len(s)):
          if s[i]in self.symbols:
            temp = s[i - 1::-1]
            temp = temp.replace("%", "/100")
            value = eval(temp)*0.01
            temp2 = s[:i:-1]
            info = temp2 + s[i] + str(value)
            return[self.showText, str(eval(info))]
          else:
              num = self.showInfo[:len(self.showInfo):-1]
              if self.isNum(num) == True:
                return[self.showInfo, str(float(num)*0.01)]
              else:
                return[self.showInfo,'错误']

    def symbol(self):
        self.symbols = ["+", "-", "×", "÷"]
        return[self.symbols]

    def back(self):
        temp = equation.get()
        equation.set(temp[:-1])

    def run():
        temp = equation.get()
        temp = temp.replace('x', '*')
        temp = temp.replace('÷', '/')
        print(temp)
        answer = caculator.caculator(temp)
        answer = '%.2f' % answer
        result.set(str(answer))


button_back = tk.Button(root, text='←', bg='DarkGray', command=back)
button_back.place(x='10', y='150', width='60', height='40')
button_lbracket = tk.Button(root, text='(', bg='DarkGray', command=lambda: getnum('('))
button_lbracket.place(x='90', y='150', width='60',height='40')
button_rbracket = tk.Button(root, text=')', bg='DarkGray',command=lambda: getnum(')'))
button_rbracket.place(x='170', y='150', width='60', height='40')
button_division = tk.Button(root, text='÷', bg='DarkGray', command=lambda: getnum('÷'))
button_division.place(x='250', y='150', width='60', height='40')
# 第二行按钮
button_7 = tk.Button(root, text='7', bg='DarkGray', command=lambda: getnum('7'))
button_7.place(x = '10',y='205',width = '60',height='40')
button_8 = tk.Button(root,text='8',bg='DarkGray',command= lambda : getnum('8'))
button_8.place(x = '90',y='205',width = '60',height='40')
button_9 = tk.Button(root,text='9',bg='DarkGray',command= lambda : getnum('9'))
button_9.place(x = '170',y='205',width = '60',height='40')
button_multiplication =TK.Button(root,text='X',bg='DarkGray',command= lambda : getnum('x'))
button_multiplication.place(x = '250',y='205',width = '60',height='40')
# 第三行按钮
button_4 = tk.Button(root,text='4',bg='DarkGray',command= lambda : getnum('4'))
button_4.place(x = '10',y='260',width = '60',height='40')
button_5 = tk.Button(root,text='5',bg='DarkGray',command= lambda : getnum('5'))
button_5.place(x = '90',y='260',width = '60',height='40')
button_6 = tk.Button(root,text='6',bg='DarkGray',command= lambda : getnum('6'))
button_6.place(x = '170',y='260',width = '60',height='40')
button_minus = tk.Button(root,text='—',bg='DarkGray',command= lambda : getnum('-'))
button_minus.place(x = '250',y='260',width = '60',height='40')
# 第四行按钮
button_1 = tk.Button(root,text='1',bg='DarkGray',command= lambda :getnum('1'))
button_1.place(x = '10',y='315',width = '60',height='40')
button_2 = tk.Button(root,text='2',bg='DarkGray',command= lambda : getnum('2'))
button_2.place(x = '90',y='315',width = '60',height='40')
button_3 = tk.Button(root,text='3',bg='DarkGray',command= lambda : getnum('3'))
button_3.place(x = '170',y='315',width = '60',height='40')
button_plus = tk.Button(root,text='+',bg='DarkGray',command= lambda : getnum('+'))
button_plus.place(x = '250',y='315',width = '60',height='40')
# 第五行按钮
button_MC = tk.Button(root,text='MC',bg='DarkGray',command = clear)
button_MC.place(x = '10',y='370',width = '60',height='40')
button_0 = tk.Button(root,text='0',bg='DarkGray',command= lambda : getnum('0'))
button_0.place(x = '90',y='370',width = '60',height='40')
button_point = tk.Button(root,text='.',bg='DarkGray',command= lambda : getnum('.'))
button_point.place(x = '170',y='370',width = '60',height='40')
button_equal = tk.Button(root,text='=',bg='DarkGray',command= run)
button_equal.place(x = '250',y='370',width = '60',height='40')


root.mainloop()

