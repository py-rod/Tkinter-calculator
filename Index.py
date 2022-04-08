import tkinter as tk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.frm = tk.Frame(self.root, background="black")
        self.frm.grid()
        self.textwindow = tk.StringVar()
        self.operator = ""
        self.view()
        
        
        
    def cleanwindow(self):
        if self.textwindow:
            self.operator = ""
            self.textwindow.set("")
        
    def click(self, var):
        self.operator += str(var)
        self.textwindow.set(self.operator)
        
    def Result(self):
        try:
            result = str(eval(self.operator))
        except ZeroDivisionError:
            self.textwindow.set("Error!")
        except SyntaxError:
            self.textwindow.set("Agregue numero")
        else:
            return self.textwindow.set(result)
        
        
    def view(self):
        # View number
        tk.Entry(self.frm, font=("Space mono", 25), justify="right", textvariable=self.textwindow).grid(
            column=0, row=0, columnspan=4, sticky="we")

        # Buttons Operator
        tk.Button(self.frm, text="%", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#FFCA33",
                  activebackground="#FFD74D", command=lambda:self.click("%")).grid(column=0, row=1, sticky="we")

        tk.Button(self.frm, text="(", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#FFCA33",
                  activebackground="#FFD74D", command=lambda: self.click("(")).grid(column=1, row=1, sticky="we")

        tk.Button(self.frm, text=")", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#FFCA33",
                  activebackground="#FFD74D", command=lambda: self.click(")")).grid(column=2, row=1, sticky="we")

        tk.Button(self.frm, text="AC", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#FFCA33",
                  activebackground="#FFD74D", command=self.cleanwindow).grid(column=3, row=1, sticky="we")

        tk.Button(self.frm, text="/", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#FFCA33",
                  activebackground="#FFD74D", command=lambda: self.click("/")).grid(column=3, row=2, sticky="we")

        tk.Button(self.frm, text="x", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#FFCA33",
                  activebackground="#FFD74D", command=lambda: self.click("*")).grid(column=3, row=3, sticky="we")

        tk.Button(self.frm, text="-", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#FFCA33",
                  activebackground="#FFD74D", command=lambda: self.click("-")).grid(column=3, row=4, sticky="we")

        tk.Button(self.frm, text="+", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#FFCA33",
                  activebackground="#FFD74D", command=lambda: self.click("+")).grid(column=3, row=5, sticky="we")

        # Numbers
        tk.Button(self.frm, text="7", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda:self.click(7)).grid(column=0, row=2, sticky="we")

        tk.Button(self.frm, text="8", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda:self.click(8)).grid(column=1, row=2, sticky="we")

        tk.Button(self.frm, text="9", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda: self.click(9)).grid(column=2, row=2, sticky="we")

        tk.Button(self.frm, text="4", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda:self.click(4)).grid(column=0, row=3, sticky="we")

        tk.Button(self.frm, text="5", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda:self.click(5)).grid(column=1, row=3, sticky="we")

        tk.Button(self.frm, text="6", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda: self.click(6)).grid(column=2, row=3, sticky="we")

        tk.Button(self.frm, text="1", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda: self.click(1)).grid(column=0, row=4, sticky="we")

        tk.Button(self.frm, text="2", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda: self.click(2)).grid(column=1, row=4, sticky="we")

        tk.Button(self.frm, text="3", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda: self.click(3)).grid(column=2, row=4, sticky="we")

        tk.Button(self.frm, text="0", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda: self.click(0)).grid(column=0, row=5, sticky="we")

        tk.Button(self.frm, text=".", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#DCDCDC", command=lambda: self.click(".")).grid(column=1, row=5, sticky="we")

        tk.Button(self.frm, text="=", font=("Space mono", 15),
                  cursor="hand2", relief="flat", bg="#338AFF", command=self.Result).grid(column=2, row=5, sticky="we")

        self.root.mainloop()


if __name__ == '__main__':
    app = Calculator()
