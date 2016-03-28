import sys
from tkinter import *



class GUIDemo(Frame):

    state='number'

    def __init__(self, master=None):

        #setup frame size
        Frame.__init__(self, master)
        master.minsize(width=200,height=300)
        master.maxsize(width=500,height=500)
        #initial grid
        self.grid(sticky=N+S+E+W)
        for x in range(60):
            Grid.columnconfigure(master, x, weight=1)
        for y in range(30):
            Grid.rowconfigure(master, y, weight=1)

        #load components
        self.createWidgets()

    #components
    def createWidgets(self):

        def numberbuttonhit(number):
            print(str(number))

        #output
        self.outputField = Entry(self)
        self.outputField['width']=50
        self.outputField.grid(row=0, column=1, columnspan=3)

        #buttons
        self.button9 = Button(self,width=6,height=1,command=numberbuttonhit(9))
        self.button9["text"] = "9"
        self.button9.grid(row=1, column=3,sticky="NSEW")
        self.button8 = Button(self,width=6,height=1)
        self.button8["text"] = "8"
        self.button8.grid(row=1, column=2,sticky="NSEW")
        self.button7 = Button(self,width=6,height=1)
        self.button7["text"] = "7"
        self.button7.grid(row=1, column=1,sticky="NSEW")
        self.button6 = Button(self,width=6,height=1)
        self.button6["text"] = "6"
        self.button6.grid(row=2, column=3,sticky="NSEW")
        self.button5 = Button(self,width=6,height=1)
        self.button5["text"] = "5"
        self.button5.grid(row=2, column=2,sticky="NSEW")
        self.button4 = Button(self,width=6,height=1)
        self.button4["text"] = "4"
        self.button4.grid(row=2, column=1,sticky="NSEW")
        self.button3 = Button(self,width=6,height=1)
        self.button3["text"] = "3"
        self.button3.grid(row=3, column=3,sticky="NSEW")
        self.button2 = Button(self,width=6,height=1)
        self.button2["text"] = "2"
        self.button2.grid(row=3, column=2,sticky="NSEW")
        self.button1 = Button(self,width=6,height=1)
        self.button1["text"] = "1"
        self.button1.grid(row=3, column=1,sticky="NSEW")

        '''
        for x in range(3):
          Grid.columnconfigure(self, x, weight=1)

        for y in range(1,3):
          Grid.rowconfigure(self, y, weight=1)
        '''




if __name__ == '__main__':
    root = Tk()
    app = GUIDemo(master=root)
    app.mainloop()
