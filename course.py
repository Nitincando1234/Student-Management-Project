from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # for icons
class CourseClass:                      # RMS = Result Management System
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1500x600+0+180")
        self.root.config(bg = "white")
        self.root.focus_force()         # forces the root on top of RMS
        # variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # title
        self.title = Label(self.root, text = "Course Management", font = ("Helvetica", 20, "bold"), bg = "#3b3b3b", fg = "white").place(x = 20, y = 10, width = 1460, height = 50)

        # Label Widgets
        lbl_course = Label(self.root, bg = "#414344", fg = "white", text = "Course", font = ("Helvetica", 20),).place(x = 20, y = 80, width = 220)
        lbl_duration = Label(self.root, bg = "#414344", fg = "white", text = "Duration", font = ("Helvetica", 20),).place(x = 20, y = 120 + 20, width = 220)
        lbl_charges = Label(self.root, bg = "#414344", fg = "white", text = "Charges", font = ("Helvetica", 20),).place(x = 20, y = 160 + 40, width = 220)
        lbl_description = Label(self.root, bg = "#414344", fg = "white", text = "Description", font = ("Helvetica", 20),).place(x = 20, y = 200 + 60, width = 220)

        # Entry widget
        self.txt_course = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_course, font = ("Times New Roman", 14),)
        self.txt_course.place(x = 300, y = 80, width = 350, height = 40)
        txt_duration = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_duration, font = ("Times New Roman", 14),).place(x = 300, y = 120 + 20, width = 350, height = 40)
        txt_charges = Entry(self.root, bg = "white", fg = "black",  textvariable = self.var_charges, font = ("Times New Roman", 14),).place(x = 300, y = 160 + 40, width = 350, height = 40)
        self.txt_description = Text(self.root, bg = "white", fg = "black", font = ("Times New Roman", 14),)
        self.txt_description.place(x = 300, y = 200 + 60, width = 350, height = 220)

        # Buttons
        self.button_save = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Save", fg = "white", cursor = "hand2", command = self.add)
        self.button_save.place(x = 20, y = 520, height = 40, width = 140)
        self.button_update = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Update", fg = "white", cursor = "hand2", command = self.update)
        self.button_update.place(x = 180, y = 520, height = 40, width = 140)
        self.button_clear = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Clear", fg = "white", cursor = "hand2", command = self.clear)
        self.button_clear.place(x = 360, y = 520, height = 40, width = 140)
        self.button_delete = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Delete", fg = "white", cursor = "hand2", command = self.delete)
        self.button_delete.place(x = 540, y = 520, height = 40, width = 140)

        # Search Table
        self.search_var = StringVar()
        lbl_search_course = Label(self.root, bg = "#414344", fg = "white", text = "Course", font = ("Helvetica", 20),).place(x = 750, y = 80, width = 220)
        txt_search_course = Entry(self.root, bg = "white", fg = "black",  textvariable = self.search_var, font = ("Times New Roman", 14),).place(x = 1000, y = 80, width = 350, height = 40)
        btn_search_course = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Search", fg = "white", cursor = "hand2", command = self.search).place(x = 1380, y = 80, width = 100, height = 40)

        # Content of Search
        self.C_Frame = Frame(self.root, bd = 2)
        self.C_Frame.place(x = 750, y = 140, width = 730, height = 400)
        
        scrolly = Scrollbar(self.C_Frame, orient = VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient = HORIZONTAL)

        self.course_table = ttk.Treeview(self.C_Frame, columns =("cid", "name", "duration", "charges", "description"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command = self.course_table.xview)
        scrolly.config(command = self.course_table.yview)
        
        self.course_table.heading("cid", text = "Course ID")
        self.course_table.heading("name", text = "Name")
        self.course_table.heading("duration", text = "Duration")
        self.course_table.heading("charges", text = "Charges")
        self.course_table.heading("description", text = "Description")

        self.course_table["show"] = "headings"

        self.course_table.column("cid", width = 150)
        self.course_table.column("name", width = 150)
        self.course_table.column("duration", width = 150)
        self.course_table.column("charges", width = 150)
        self.course_table.column("description", width = 150)

        self.course_table.pack(fill = BOTH, expand = 1)             # BOTH => for both height and width
        self.course_table.bind("<ButtonRelease-1>", self.get_data) # bind the events with the course table and execute some function
        self.show()
    #===============================================================================
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.txt_description.delete("1.0", END)
        self.search_var.set("")
        self.txt_course.config(state = NORMAL)

    def get_data(self, e):
        self.txt_course.config(state = "readonly")
        r = self.course_table.focus()
        content = self.course_table.item(r)                         # numpy array of item and their respective names
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[4])
    def delete(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try :
            if self.var_course.get() == "" or self.var_duration.get() == "" or self.var_charges.get() == "" or self.txt_description.get("1.0", END) == "":              # value of variable as a string
                messagebox.showerror("Error","Course name is Required Field ! ", parent = self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_course.get(),))
                row = cur.fetchone()                
                if row == None:
                    messagebox.showerror("Error", "Select Course name from the list first !")
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to perform deletion ?", parent = self.root)     # for yes/no dialogue box
                    if op == True:
                        cur.execute("DELETE FROM course WHERE name = ?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Success", f"{self.var_course.get()} Course Deleted successfully", parent = self.root)
                        self.clear()
                        self.show()
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")
    def add(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try :
            if self.var_course.get() == "" or self.var_duration.get() == "" or self.var_charges.get() == "" or self.txt_description.get("1.0", END) == "":              # value of variable as a string
                messagebox.showerror("Error","Course name is Required Field ! ", parent = self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_course.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Course already present in record !")
                else:
                    cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (?, ?, ?, ?)",
                    (self.var_course.get(), 
                     self.var_duration.get(), 
                     self.var_charges.get(), 
                     self.txt_description.get("1.0", END), 
                     ))
                    con.commit()
                    messagebox.showinfo("Success", f"{self.var_course.get()} Course added successfully", parent = self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")
    def show(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            self.course_table.delete(*self.course_table.get_children())
            rows = cur.fetchall()
            for row in rows:
                self.course_table.insert("", END, values = row)
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")
            
    def search(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM course where name LIKE '%{self.search_var.get()}%'")
            self.course_table.delete(*self.course_table.get_children())
            rows = cur.fetchall()
            for row in rows:
                self.course_table.insert("", END, values = row)
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")

    def update(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try :
            if self.var_course.get() == "" or self.var_duration.get() == "" or self.var_charges.get() == "" or self.txt_description.get("1.0", END) == "":              # value of variable as a string
                messagebox.showerror("Error","Course name is Required Field ! ", parent = self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Course must be present in the list !")
                else:
                    cur.execute("UPDATE course SET duration = ?, charges = ?, description = ? where name = ?",
                    (self.var_duration.get(), 
                     self.var_charges.get(), 
                     self.txt_description.get("1.0", END), 
                     self.var_course.get()
                     ))
                    con.commit()
                    messagebox.showinfo("Success", f"{self.var_course.get()} Course updated successfully", parent = self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")        
if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()