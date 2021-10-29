from tkinter import *
import sqlite3
import tkinter.messagebox
import os

path = os.path.abspath("STR.db")
conn = sqlite3.connect(path)
c = conn.cursor()

result = c.execute("SELECT Max(ID) from Inventory")
for i in result:
    ID = i[0]
    


class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text = "Update the Database", font = ("arial 40 bold"), fg = "orange")
        self.heading.place( x = 350 , y = 0)

        self.ID_le = Label(master,text = "Enter ID of product", font = ("arial 20 bold"))
        self.ID_le.place(x=0,y=70)


        self.Name_l = Label(master, text = "Enter Product Name", font = ("arial 20 bold"))
        self.Name_l.place(x=0,y=120)

        self.Stock_l = Label(master, text = "Enter Stock", font = ("arial 20 bold"))
        self.Stock_l.place(x=0,y=170)

        self.CostPrice_l = Label(master, text = "Enter Cost Price", font = ("arial 20 bold"))
        self.CostPrice_l.place(x=0,y=220)

        self.SellingPrice_l = Label(master, text = "Enter Selling Price", font = ("arial 20 bold"))
        self.SellingPrice_l.place(x=0,y=270)

        self.TotalCostPrice_l = Label(master, text = "Enter Total Cost Price", font = ("arial 20 bold"))
        self.TotalCostPrice_l.place(x=0,y=320)

        self.TotalSellingPrice_l = Label(master, text = "Enter Total Selling Price", font = ("arial 20 bold"))
        self.TotalSellingPrice_l.place(x=0,y=370)

                                                  
        #Labels for entries

        self.ID_leb = Entry(master, width = 15 ,font = ("arial 20 bold"))
        self.ID_leb.place(x=380,y=70)

        self.Name_e = Entry(master, width=25, font = ("arial 20 bold"))
        self.Name_e.place(x=380,y=120)

        self.Stock_e = Entry(master, width=25, font = ("arial 20 bold"))
        self.Stock_e.place(x=380,y=170)

        self.CostPrice_e = Entry(master, width=25, font = ("arial 20 bold"))
        self.CostPrice_e.place(x=380,y=220)

        self.SellingPrice_e = Entry(master, width=25, font = ("arial 20 bold"))
        self.SellingPrice_e.place(x=380,y=270)

        self.TotalCostPrice_e = Entry(master, width=25, font = ("arial 20 bold"))
        self.TotalCostPrice_e.place(x=380,y=320)

        self.TotalSellingPrice_e = Entry(master, width=25, font = ("arial 20 bold"))
        self.TotalSellingPrice_e.place(x=380,y=370)


        #Buttons

        self.btn_search = Button(master, text = "Search" , width=15 , height=2 , bg = "purple", fg = "white", command = self.search)
        self.btn_search.place(x=650, y=70)
        

        self.btn_add = Button(master, text = "Update Database", width=25, height = 2, bg = "steelblue", fg = "white", command = self.update)
        self.btn_add.place(x=420,y=430)

        #Textbox
        self.tBox = Text(master, width=60, height=15)
        self.tBox.place(x=810,y=70)
        self.tBox.insert(END, "ID had reached up to : " + str(ID))

    def search(self, *args, **kwargs):
        sql = "SELECT * FROM Inventory WHERE ID = ?"
        result = c.execute(sql, (self.ID_leb.get(), ))
        for i in result:
            self.n1 = i[1]  # returns name
            self.n2 = i[2]  # returns stock
            self.n3 = i[3]  # returns CostPrice
            self.n4 = i[4]  # SellingPrice
            self.n5 = i[5]  # TotalCostPrice
            self.n6 = i[6]  # TotalSellingPrice
            self.n7 = i[7]  # Profit

        conn.commit()

        self.Name_e.delete(0,END)
        self.Name_e.insert(0,str(self.n1))

        self.Stock_e.delete(0,END)
        self.Stock_e.insert(0,str(self.n2))

        self.CostPrice_e.delete(0,END)
        self.CostPrice_e.insert(0,str(self.n3))

        self.SellingPrice_e.delete(0,END)
        self.SellingPrice_e.insert(0,str(self.n4))

        self.TotalCostPrice_e.delete(0,END)
        self.TotalCostPrice_e.insert(0,str(self.n5))

        self.TotalSellingPrice_e.delete(0,END)
        self.TotalSellingPrice_e.insert(0,str(self.n6))

    def update(self, *args, **kwargs):
        """
        Gets the corresponding product details and
        updates the database.
        """
        self.u1 = self.Name_e.get()
        self.u2 = self.Stock_e.get()
        self.u3 = self.CostPrice_e.get()
        self.u4 = self.SellingPrice_e.get()
        self.u5 = self.TotalCostPrice_e.get()
        self.u6 = self.TotalSellingPrice_e.get()
        

        query = "UPDATE Inventory SET Name=?, Stock=?, CostPrice=?, SellingPrice=?, TotalCostPrice=?, TotalSellingPrice=? WHERE ID=?"
        c.execute(query,(self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.ID_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Updated the database successfully")
        

root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Update the database")
root.mainloop()



