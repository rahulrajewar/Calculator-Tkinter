import tkinter
import math
from tkinter import Frame,Tk, Button, Entry, END, messagebox
calcu = Tk()
calcu.title("Calculator")
calcu.resizable(0, 0)
class appli(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.widget()
    
    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)
        
    def calculate(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/100")
        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("ERROR!", "INVALID INPUT")

    def squareroot(self):
        self.x = self.display.get()
        self.result = math.sqrt(float(self.x))
        self.replaceText(self.result)
    
    def SQ(self):
        self.x = self.display.get()
        self.result = float(self.x) * float(self.x)
        self.replaceText(self.result)
    
    def INV(self):
        self.x = self.display.get()
        self.result = 1/float(self.x)
        self.replaceText(self.result)
    
    def appenddisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)
        
        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)
    
    def clearText(self):
        self.replaceText("0")
    
    def widget(self):
        self.display = Entry(self, font=("Helvetica", 16))
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4)
        
        self.percentage = Button(self, font=("Helvetica", 12), text="%", borderwidth=0.5, command=lambda: self.appenddisplay("%"))
        self.percentage.grid(row=1,column=0, sticky="NWNESWSE")
        self.sqroot = Button(self, font=("Helvetica", 8), text="SqRoot", borderwidth=0.5, command=lambda: self.squareroot())
        self.sqroot.grid(row=1,column=1, sticky="NWNESWSE")
        self.square = Button(self, font=("Helvetica", 12), text="Sq", borderwidth=0.5, command=lambda: self.SQ())
        self.square.grid(row=1,column=2, sticky="NWNESWSE")
        self.inverse = Button(self, font=("Helvetica", 12), text="1/x", borderwidth=0.5, command=lambda: self.INV())
        self.inverse.grid(row=1,column=3, sticky="NWNESWSE")
        
        self.clear = Button(self, font=("Helvetica", 12), text="C", borderwidth=0.5, command=lambda: self.clearText())
        self.clear.grid(row=2,column=0, sticky="NWNESWSE", columnspan=2)
        self.divide = Button(self, font=("Helvetica", 12), text="/", borderwidth=0.5,  command=lambda: self.backspace())
        self.divide.grid(row=2,column=3, sticky="NWNESWSE")
        self.multiply = Button(self, font=("Helvetica", 12), text="*", borderwidth=0.5, command=lambda: self.appenddisplay("*"))
        self.multiply.grid(row=2,column=2, sticky="NWNESWSE")
        
        self.seven = Button(self, font=("Helvetica", 12), text="7", borderwidth=0.5, command=lambda: self.appenddisplay("7"))
        self.seven.grid(row=3,column=0, sticky="NWNESWSE")
        self.eight = Button(self, font=("Helvetica", 12), text="8", borderwidth=0.5,  command=lambda: self.appenddisplay("8"))
        self.eight.grid(row=3,column=1, sticky="NWNESWSE")
        self.nine = Button(self, font=("Helvetica", 12), text="9", borderwidth=0.5, command=lambda: self.appenddisplay("9"))
        self.nine.grid(row=3,column=2, sticky="NWNESWSE")
        self.minus = Button(self, font=("Helvetica", 12), text="-", borderwidth=0.5, command=lambda: self.appenddisplay("-"))
        self.minus.grid(row=3,column=3, sticky="NWNESWSE")
        
        
        self.four = Button(self, font=("Helvetica", 12), text="4", borderwidth=0.5, command=lambda: self.appenddisplay("4"))
        self.four.grid(row=4,column=0, sticky="NWNESWSE")
        self.five = Button(self, font=("Helvetica", 12), text="5", borderwidth=0.5, command=lambda: self.appenddisplay("5"))
        self.five.grid(row=4,column=1, sticky="NWNESWSE")
        self.six = Button(self, font=("Helvetica", 12), text="6", borderwidth=0.5, command=lambda: self.appenddisplay("6"))
        self.six.grid(row=4,column=2, sticky="NWNESWSE")
        self.plus = Button(self, font=("Helvetica", 12), text="+", borderwidth=0.5, command=lambda: self.appenddisplay("+"))
        self.plus.grid(row=4,column=3, sticky="NWNESWSE", rowspan=2)
        
        
        self.one = Button(self, font=("Helvetica", 12), text="1", borderwidth=0.5, command=lambda: self.appenddisplay("1"))
        self.one.grid(row=5,column=0, sticky="NWNESWSE")
        self.two = Button(self, font=("Helvetica", 12), text="2", borderwidth=0.5, command=lambda: self.appenddisplay("2"))
        self.two.grid(row=5,column=1, sticky="NWNESWSE")
        self.three = Button(self, font=("Helvetica", 12), text="3", borderwidth=0.5, command=lambda: self.appenddisplay("3"))
        self.three.grid(row=5,column=2, sticky="NWNESWSE")
        
        
        self.twozero = Button(self, font=("Helvetica", 12), text="00", borderwidth=0.5, command=lambda: self.appenddisplay("00"))
        self.twozero.grid(row=6,column=0, sticky="NWNESWSE")
        self.zero = Button(self, font=("Helvetica", 12), text="0", borderwidth=0.5, command=lambda: self.appenddisplay("0"))
        self.zero.grid(row=6,column=1, sticky="NWNESWSE")
        self.dot = Button(self, font=("Helvetica", 12), text=".", borderwidth=0.5, command=lambda: self.appenddisplay("."))
        self.dot.grid(row=6,column=2, sticky="NWNESWSE")
        self.equal = Button(self, font=("Helvetica", 12), text="=", borderwidth=0.5, command=lambda: self.calculate())
        self.equal.grid(row=6,column=3, sticky="NWNESWSE")
        

app = appli(calcu).grid()
calcu.mainloop()