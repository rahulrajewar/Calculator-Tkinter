import tkinter
from tkinter import Frame,Tk, Button
calcu = Tk()
calcu.title("Calculator")
calcu.resizable(0, 0)
class appli(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.widget()
    
    def widget(self):
        self.display = tkinter.Entry(self, font=("Helvetica", 16))
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4)
        
        self.percentage = Button(self, font=("Helvetica", 12), text="%", borderwidth=1)
        self.percentage.grid(row=1,column=0, sticky="NWNESWSE")
        self.sqroot = Button(self, font=("Helvetica", 8), text="SqRoot", borderwidth=1)
        self.sqroot.grid(row=1,column=1, sticky="NWNESWSE")
        self.square = Button(self, font=("Helvetica", 12), text="Sq", borderwidth=1)
        self.square.grid(row=1,column=2, sticky="NWNESWSE")
        self.inverse = Button(self, font=("Helvetica", 12), text="1/x", borderwidth=1)
        self.inverse.grid(row=1,column=3, sticky="NWNESWSE")
        
        self.clear = Button(self, font=("Helvetica", 12), text="C", borderwidth=1)
        self.clear.grid(row=2,column=0, sticky="NWNESWSE", columnspan=2)
        self.back = Button(self, font=("Helvetica", 12), text="<-", borderwidth=1)
        self.back.grid(row=2,column=2, sticky="NWNESWSE")
        self.divide = Button(self, font=("Helvetica", 12), text="/", borderwidth=1)
        self.divide.grid(row=2,column=3, sticky="NWNESWSE")
        
        self.seven = Button(self, font=("Helvetica", 12), text="7", borderwidth=1)
        self.seven.grid(row=3,column=0, sticky="NWNESWSE")
        self.eight = Button(self, font=("Helvetica", 12), text="8", borderwidth=1)
        self.eight.grid(row=3,column=1, sticky="NWNESWSE")
        self.nine = Button(self, font=("Helvetica", 12), text="9", borderwidth=1)
        self.nine.grid(row=3,column=2, sticky="NWNESWSE")
        self.multiply = Button(self, font=("Helvetica", 12), text="*", borderwidth=1)
        self.multiply.grid(row=3,column=3, sticky="NWNESWSE")
        
        self.four = Button(self, font=("Helvetica", 12), text="4", borderwidth=1)
        self.four.grid(row=4,column=0, sticky="NWNESWSE")
        self.five = Button(self, font=("Helvetica", 12), text="5", borderwidth=1)
        self.five.grid(row=4,column=1, sticky="NWNESWSE")
        self.six = Button(self, font=("Helvetica", 12), text="6", borderwidth=1)
        self.six.grid(row=4,column=2, sticky="NWNESWSE")
        self.minus = Button(self, font=("Helvetica", 12), text="-", borderwidth=1)
        self.minus.grid(row=4,column=3, sticky="NWNESWSE")
        
        self.one = Button(self, font=("Helvetica", 12), text="1", borderwidth=1)
        self.one.grid(row=5,column=0, sticky="NWNESWSE")
        self.two = Button(self, font=("Helvetica", 12), text="2", borderwidth=1)
        self.two.grid(row=5,column=1, sticky="NWNESWSE")
        self.three = Button(self, font=("Helvetica", 12), text="3", borderwidth=1)
        self.three.grid(row=5,column=2, sticky="NWNESWSE")
        self.plus = Button(self, font=("Helvetica", 12), text="+", borderwidth=1)
        self.plus.grid(row=5,column=3, sticky="NWNESWSE")
        
        self.twozero = Button(self, font=("Helvetica", 12), text="00", borderwidth=1)
        self.twozero.grid(row=6,column=0, sticky="NWNESWSE")
        self.zero = Button(self, font=("Helvetica", 12), text="0", borderwidth=1)
        self.zero.grid(row=6,column=1, sticky="NWNESWSE")
        self.dot = Button(self, font=("Helvetica", 12), text=".", borderwidth=1)
        self.dot.grid(row=6,column=2, sticky="NWNESWSE")
        self.equal = Button(self, font=("Helvetica", 12), text="=", borderwidth=1)
        self.equal.grid(row=6,column=3, sticky="NWNESWSE")
        

app = appli(calcu).grid()
calcu.mainloop()