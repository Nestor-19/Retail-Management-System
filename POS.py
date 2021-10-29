from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import os
import random 
import math

path = os.path.abspath("STR.db")
conn = sqlite3.connect(path)
c = conn.cursor()

date = datetime.datetime.now().date()
list_prod = []
ID_prod = []
price_prod = []
quantity_prod = []

Labels_list = []

class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.left = Frame(master , width = 800, bg="white", height=768)
        self.left.pack(side=LEFT)

        self.right = Frame(master , width = 566, bg="DeepSkyBlue2", height=768)
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text = "Store", bg = "white" ,font=('arial 40 bold'))
        self.heading.place(x=0,y=0)

        self.date_l = Label(self.right, text = "Today's date: " + str(date) , bg = "DeepSkyBlue2", fg = "black" , font=('arial 15 bold'))
        self.date_l.place(x=0,y=0)

        # Table for invoice
        self.tProduct = Label(self.right, text = "Products", font = ("arial 17 bold"), bg = "DeepSkyBlue2" , fg = "black")
        self.tProduct.place(x=0,y=50)

        self.tQuantity = Label(self.right, text = "Quantity", font = ("arial 17 bold"), bg = "DeepSkyBlue2" , fg = "black")
        self.tQuantity.place(x=200,y=50)

        self.tAmount = Label(self.right, text = "Amount", font = ("arial 17 bold"), bg = "DeepSkyBlue2" , fg = "black")
        self.tAmount.place(x=400,y=50)

        #Entering items 

        self.EnterID = Label(self.left, text = "Enter ID Of Product: ", font=('arial 17 bold'), bg="white")
        self.EnterID.place(x=0,y=80)

        self.EnterID_e = Entry(self.left, width = 25, bg = "lightpink", font=('arial 17 bold'))
        self.EnterID_e.place(x=230,y=80)
        self.EnterID_e.focus()

        #Buttons

        self.search_btn = Button(self.left, text = "Search", width = 25, height = 2, bg = "DeepSkyBlue2", command = self.get_product)
        self.search_btn.place(x=290,y=120)

        self.ProductName = Label(self.left, text="", font=('arial 26 bold'), bg = "white")
        self.ProductName.place(x=0,y=250)

        self.PPrice = Label(self.left, text="", font=('arial 26 bold'), bg = "white")
        self.PPrice.place(x=0,y=290)

        #Total Label
        self.Total_l =Label(self.right, text = "", bg = "DeepSkyBlue2", fg = "black" , font=('arial 33 bold'))
        self.Total_l.place(x=0,y=630)
        



    def get_product(self, *args, **kwargs):
        """
        Gets the Product's details according to their ID
        """
        self.get_ID = self.EnterID_e.get()
        query = "SELECT * FROM Inventory WHERE ID=?"
        result = c.execute(query, self.get_ID, )
        for self.r in result:
            self.get_ID = self.r[0]
            self.get_Name = self.r[1]
            self.get_Price = self.r[4]
            self.get_Stock = self.r[2]
        self.ProductName.configure(text = "Product's Name:" +  str(self.get_Name))        
        self.PPrice.configure(text = "Price: $ " + str(self.get_Price))

        #Creating Quantity Label
        self.Quantity_l = Label(self.left, text = "Enter Quantity: ", bg = "white", font=('arial 17 bold'))
        self.Quantity_l.place(x=0,y=370)

        self.Quantity_e = Entry(self.left, width = 25, bg = "lightpink", font=('arial 17 bold'))
        self.Quantity_e.place(x=200,y=370)
        self.Quantity_e.focus()

        #Discount Label
        self.Discount_l = Label(self.left, text = "Enter Discount: ", bg = "white", font=('arial 17 bold'))
        self.Discount_l.place(x=0,y=400)

        self.Discount_e = Entry(self.left, width = 25, bg = "lightpink", font=('arial 17 bold'))
        self.Discount_e.place(x=200,y=400)
        self.Discount_e.insert(END , 0) 

        #Adding to Cart
        self.Cart_btn = Button(self.left, text = "Add to Cart", width = 25, height = 2, bg = "DeepSkyBlue2", command = self.Add_2_Cart)
        self.Cart_btn.place(x=290,y=450)

        #Bill
        self.Change_l = Label(self.left, text = "Given Amount: " , bg = "white", font=('arial 17 bold'))
        self.Change_l.place(x=0,y=530)

        self.Change_e = Entry(self.left, width = 25, bg = "lightpink", font=('arial 17 bold'))
        self.Change_e.place(x=170,y=530)

        self.Change_btn = Button(self.left, text = "Determine Change", width = 25, height = 2, bg = "DeepSkyBlue2", command = self.Change_func)
        self.Change_btn.place(x=290,y=570)

        #Generate Bill Button
        self.Bill_btn = Button(self.left, text = "Generate Bill", width = 120, height = 2, bg = "navy", fg = "white", command = self.Generate_Bill)
        self.Bill_btn.place(x=0,y=640)


    def Add_2_Cart(self, *args, **kwargs):
        #Determining Quantity from Database
        self.Quantity_v = int(self.Quantity_e.get())
        if self.Quantity_v > int(self.get_Stock):
            tkinter.messagebox.showinfo("Error", "Don't have sufficicent products in Stock")
        else:
            self.FinalPrice = (float(self.Quantity_v) * float(self.get_Price)) - (float(self.Discount_e.get()))
            list_prod.append(self.get_Name)
            ID_prod.append(self.get_ID)
            price_prod.append(self.FinalPrice)
            quantity_prod.append(self.Quantity_v)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.p in list_prod:
                self.temp_Name = Label(self.right, text = str(list_prod[self.counter]), bg = "navy" , fg = "white" , font=('arial 17 bold'))
                self.temp_Name.place(x = 0, y = self.y_index)
                Labels_list.append(self.temp_Name)

                self.temp_Quantity = Label(self.right, text = str(quantity_prod[self.counter]), bg = "navy" , fg = "white" , font=('arial 17 bold'))
                self.temp_Quantity.place(x = 300, y = self.y_index)
                Labels_list.append(self.temp_Quantity)

                self.temp_Price = Label(self.right, text = str(price_prod[self.counter]), bg = "navy" , fg = "white" , font=('arial 17 bold'))
                self.temp_Price.place(x = 500, y = self.y_index)
                Labels_list.append(self.temp_Price)

                self.y_index += 40
                self.counter += 1

                self.Total_l.configure(text = "Total: $" + str(sum(price_prod)))

               
                self.Quantity_l.place_forget()
                self.Quantity_e.place_forget()
                self.Discount_l.place_forget()
                self.Discount_e.place_forget()
                self.ProductName.configure(text="")
                self.PPrice.configure(text="")
                self.Cart_btn.destroy()


                self.EnterID_e.focus()
                self.EnterID_e.delete(0, END)
        


    def Change_func(self, *args, **kwargs):
        """
        Calculates the corresponding change.
        """
        self.AmountGiven = float(self.Change_e.get())
        self.Total = float(sum(price_prod))

        self.Change = self.AmountGiven - self.Total

        self.c_amount = Label(self.left, text = "Change: $" + str(self.Change), fg = "white", bg = "navy", font=('arial 17 bold'))
        self.c_amount.place(x=500,y=570)
    

    def Generate_Bill(self, *args, **kwargs):
        """
        Generates the current bill.
        """
        self.x = 0
        initial = "SELECT * FROM Inventory WHERE ID=?"
        result = c.execute(initial, (ID_prod[self.x], ))
        for i in list_prod:
            for r in result:
                self.OldStock = r[2]
            self.NewStock = int(self.OldStock) - int(quantity_prod[self.x])
            sql = "UPDATE Inventory SET Stock=? WHERE ID=?"
            c.execute(sql, (self.NewStock, ID_prod[self.x]))
            conn.commit()

            sql_insert = "INSERT INTO Transactions (ProductName, Quantity, Amount, Date) VALUES(?,?,?,?)"
            c.execute(sql_insert, (list_prod[self.x], quantity_prod[self.x], price_prod[self.x], date))
            conn.commit()
            self.x += 1


        tkinter.messagebox.showinfo("Success", "Generated Bill!")
            
                         
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.mainloop()

        
        
