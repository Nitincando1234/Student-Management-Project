from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # for icons
class ReportClass:                      # RMS = Result Management System
    
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1500x600+0+180")
        self.root.config(bg = "white")
        self.root.focus_force()    
        # title
        self.title = Label(self.root, text = "View Results", font = ("Helvetica", 20, "bold"), bg = "#3b3b3b", fg = "white").place(x = 20, y = 10, width = 1460, height = 50)

        # Vars
        self.var_id = ""                # used for deletion
        self.search_var = StringVar()
        # Label Widgets
        lbl_search = Label(self.root, bg = "#414344", fg = "white", text = "Search By Roll No", font = ("Helvetica", 20),).place(x = 20, y = 80, width = 280)
        
        lbl_roll = Label(self.root, bg = "#414344", fg = "white", text = "Roll No", font = ("Helvetica", 20), bd = 2, relief = RIDGE).place(x = 20 + 70, y = 200, width = 220, height = 60)
        lbl_name = Label(self.root, bg = "#414344", fg = "white", text = "Name", font = ("Helvetica", 20), bd = 2, relief = RIDGE).place(x = 240 + 70, y = 200, width = 220, height = 60)
        lbl_course = Label(self.root, bg = "#414344", fg = "white", text = "Course", font = ("Helvetica", 20), bd = 2, relief = RIDGE).place(x = 460 + 70, y = 200, width = 220, height = 60)
        lbl_marks = Label(self.root, bg = "#414344", fg = "white", text = "Marks Obtained", font = ("Helvetica", 20), bd = 2, relief = RIDGE).place(x = 680 + 70, y = 200, width = 220, height = 60)
        lbl_fullmarks = Label(self.root, bg = "#414344", fg = "white", text = "Total Marks", font = ("Helvetica", 20), bd = 2, relief = RIDGE).place(x = 900 + 70, y = 200, width = 220, height = 60)
        lbl_per = Label(self.root, bg = "#414344", fg = "white", text = "Percentage", font = ("Helvetica", 20), bd = 2, relief = RIDGE).place(x = 1120 + 70, y = 200, width = 220, height = 60)

        self.roll = Label(self.root, bg = "white", fg = "black", font = ("Helvetica", 20), bd = 2, relief = RIDGE)
        self.roll.place(x = 20 + 70, y = 260, width = 220, height = 60)
        self.name = Label(self.root, bg = "white", fg = "black", font = ("Helvetica", 20), bd = 2, relief = RIDGE)
        self.name.place(x = 240 + 70, y = 260, width = 220, height = 60)
        self.course = Label(self.root, bg = "white", fg = "black", font = ("Helvetica", 20), bd = 2, relief = RIDGE)
        self.course.place(x = 460 + 70, y = 260, width = 220, height = 60)
        self.marks = Label(self.root, bg = "white", fg = "black", font = ("Helvetica", 20), bd = 2, relief = RIDGE)
        self.marks.place(x = 680 + 70, y = 260, width = 220, height = 60)
        self.fullmarks = Label(self.root, bg = "white", fg = "black", font = ("Helvetica", 20), bd = 2, relief = RIDGE)
        self.fullmarks.place(x = 900 + 70, y = 260, width = 220, height = 60)
        self.per = Label(self.root, bg = "white", fg = "black", font = ("Helvetica", 20), bd = 2, relief = RIDGE)
        self.per.place(x = 1120 + 70, y = 260, width = 220, height = 60)

        # Entry Widgets
        self.txt_search_course = Entry(self.root, bg = "white", fg = "black",  textvariable = self.search_var, font = ("Times New Roman", 14),).place(x = 340, y = 80, width = 350, height = 40)

        # Buttons
        btn_search = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Search", fg = "white", cursor = "hand2", command = self.search).place(x = 700, y = 80, height = 40, width = 140)
        btn_clear = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Clear", fg = "white", cursor = "hand2", command = self.clear).place(x = 860, y = 80, height = 40, width = 140)
        btn_delete = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Delete", fg = "white", cursor = "hand2", command = self.delete).place(x = 700, y = 360, height = 40, width = 140)
    #==========================================================

    def search(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try:
            if self.search_var.get() == "":
                messagebox.showerror("Error", "Roll No is A required field !")
            else:                
                cur.execute("SELECT * FROM result where roll = ?", (self.search_var.get(), ))
                row = cur.fetchone()
                if row:
                    self.var_id = str(row[0])
                    self.roll.config(text = row[1])
                    self.name.config(text = row[2])
                    self.course.config(text = row[3])
                    self.marks.config(text = row[4])
                    self.fullmarks.config(text = row[5])
                    self.per.config(text = row[6])
                else:
                    messagebox.showerror("Error","No Record Found For The Given Roll No !", parent = self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")
    
    def clear(self):
        self.roll.config(text = "")
        self.name.config(text = "")
        self.course.config(text = "")
        self.marks.config(text = "")
        self.fullmarks.config(text = "")
        self.per.config(text = "")
        self.search_var.set("")
        self.var_id = ""
    def delete(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try :

            if self.var_id== "":
                messagebox.showerror("Error","Please Search The Result First ! ", parent = self.root)
            else:
                cur.execute("SELECT * FROM result WHERE rid = ?", (self.var_id,))
                row = cur.fetchone()                
                if row == None:
                    messagebox.showerror("Error", "No Result Found Corresponding to any Student !")
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to perform deletion ?", parent = self.root)     # for yes/no dialogue box
                    if op == True:
                        cur.execute("DELETE FROM result WHERE rid = ? and roll = ?", (self.var_id, row[1]))
                        con.commit()
                        messagebox.showinfo("Success", "Student's Details Deleted successfully", parent = self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()        