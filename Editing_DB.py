from tkinter import *
import tkinter.messagebox
import sqlite3
import os

path = os.path.abspath("STR.db")
conn = sqlite3.connect(path)
c = conn.cursor()

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text = "Add to database",fg = "red", font = ("Calibri 40 bold"))
        self.heading.place(x=400, y=0)

        self.Name_l = Label(master, text = "Add Product name", font = ("Calibri 20 bold"), fg = "blue")
        self.Name_l.place(x=0, y=70)

        self.Stock_l = Label(master, text = "Add Stock", font = ("Calibri 20 bold"), fg = "blue")
        self.Stock_l.place(x=0, y=120)

        self.CostPrice_l = Label(master, text = "Add Cost Price", font = ("Calibri 20 bold"), fg = "blue")
        self.CostPrice_l.place(x=0, y=170)

        self.SellingPrice_l = Label(master, text = "Add Selling Price", font = ("Calibri 20 bold"), fg = "blue")
        self.SellingPrice_l.place(x=0, y=210) 

        #Entries for the labels above

        self.Name_e = Entry(master, width = 25, font = ("Calibri 18 bold"))
        self.Name_e.place(x=250, y=70)

        self.Stock_e = Entry(master, width = 25, font = ("Calibri 18 bold"))
        self.Stock_e.place(x=250, y=120)

        self.CostPrice_e = Entry(master, width = 25, font = ("Calibri 18 bold"))
        self.CostPrice_e.place(x=250, y=170)

        self.SellingPrice_e = Entry(master, width = 25, font = ("Calibri 18 bold"))
        self.SellingPrice_e.place(x=250, y=210)


        #Add buttons
        self.btn_add = Button(master,text = "Add to database", height=2, width=25, bg = "yellow", fg = "blue", command = self.Get_items)
        self.btn_add.place(x=520, y=300)

        #Text box
        self.TextBox = Text(master, height=10, width=50)
        self.TextBox.place(x=800, y=70)

      
    def Get_items(self,*args,**kwargs):
        '''
        Gets corresponding user inputs and inserts into database
        '''
        self.Name = self.Name_e.get()
        self.Stock = self.Stock_e.get()
        self.CostPrice = self.CostPrice_e.get()
        self.SellingPrice = self.SellingPrice_e.get()
        

        self.TotalCostPrice = float(self.CostPrice) * float(self.Stock)
        self.TotalSellingPrice = float(self.SellingPrice) * float(self.Stock)
        self.ProfitMargin = (float(self.SellingPrice) - float(self.CostPrice))

        if self.Name == "" or self.Stock == "" or self.CostPrice == "" or self.SellingPrice == "":
            tkinter.messagebox.showinfo("Error","Please fill in all the entries")
        else:
            sql = "INSERT INTO Inventory (Name,Quantity,CostPrice,SellingPrice,TotalCostPrice,ProfitMargin,TotalSellingPrice) VALUES(self.Name, self.Stock, self.CostPrice, self.SellingPrice, self.TotalCostPrice, self.ProfitMargin, self.TotalSellingPrice)"
            c.execute(sql)
            link.commit()

            tkinter.messagebox.showinfo("Success", "Successfuly added to database") 
            
root = Tk()        
b = Database(root)


root.geometry("1366x768+0+0")
root.title("Add to database")
root.mainloop()



 




