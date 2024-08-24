from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # for icons
class ResultClass:                      # RMS = Result Management System
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1500x600+0+180")
        self.root.config(bg = "white")
        self.root.focus_force()         # forces the root on top of RMS
        #=================Image=============================================
        self.bg_img = Image.open("images/results.jpeg")
        self.bg_img = self.bg_img.resize((560, 500), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg = Label(self.root, image = self.bg_img).place(x = 920, y = 80,)

        #=================Title=============================================
        self.title = Label(self.root, text = "Result Management", font = ("Helvetica", 20, "bold"), bg = "#3b3b3b", fg = "white").place(x = 20, y = 10, width = 1460, height = 50)
        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_fullmarks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        # Label Widgets
        lbl_select = Label(self.root, bg = "#414344", fg = "white", text = "Select Students", font = ("Helvetica", 20),).place(x = 20, y = 80, width = 220)
        lbl_name = Label(self.root, bg = "#414344", fg = "white", text = "Name", font = ("Helvetica", 20),).place(x = 20, y = 120 + 20, width = 220)
        lbl_course = Label(self.root, bg = "#414344", fg = "white", text = "Course", font = ("Helvetica", 20),).place(x = 20, y = 160 + 40, width = 220)
        lbl_marks = Label(self.root, bg = "#414344", fg = "white", text = "Marks Obtained", font = ("Helvetica", 20),).place(x = 20, y = 200 + 60, width = 220)
        lbl_fullmarks = Label(self.root, bg = "#414344", fg = "white", text = "Full Marks", font = ("Helvetica", 20),).place(x = 20, y = 240 + 80, width = 220)
        
        # Button 
        btn_search = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Search", fg = "white", cursor = "hand2", command = self.search).place(x = 680, y = 80, width = 180, height = 40)
        button_add = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Add", fg = "white", cursor = "hand2", command = self.add).place(x = 460, y = 400, height = 40, width = 100)
        button_clear = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Clear", fg = "white", cursor = "hand2", command = self.clear).place(x = 580, y = 400, height = 40, width = 100)
        # Entry and Combobox Widgets
        self.txt_student_roll = ttk.Combobox(self.root, textvariable = self.var_roll, justify = CENTER, state = "readonly", values = self.roll_list, font = ("Helvetica", 14))
        self.txt_student_roll.place(x = 300, y = 80, width = 350, height = 40)
        self.txt_student_roll.set("Select")
        txt_name = Entry(self.root, bg = "white", fg = "black", state = "readonly", textvariable = self.var_name, font = ("Times New Roman", 14),).place(x = 300, y = 120 + 20, width = 560, height = 40)
        txt_course = Entry(self.root, bg = "white", fg = "black", state = "readonly", textvariable = self.var_course, font = ("Times New Roman", 14),).place(x = 300, y = 160 + 40, width = 560, height = 40)
        txt_marks = Entry(self.root, bg = "white", fg = "black",  textvariable = self.var_marks, font = ("Times New Roman", 14),).place(x = 300, y = 200 + 60, width = 560, height = 40)
        txt_fullmarks = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_fullmarks, font = ("Times New Roman", 14),).place(x = 300, y = 240 + 80, width = 560, height = 40)

    #==========================================
    def fetch_roll(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")
    def search(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, course FROM student where roll = ?", (self.var_roll.get(), ))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No Record Found For The Given Roll No !", parent = self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("") 
        self.var_course.set("") 
        self.var_marks.set("") 
        self.var_fullmarks.set("") 

    def add(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try :
            if self.var_roll.get() == "":              # value of variable as a string
                messagebox.showerror("Error","Marks are Required Field ! ", parent = self.root)
            else:
                cur.execute("SELECT * FROM result WHERE name = ? and course = ?", (self.var_name.get(), self.var_course.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Result already present in record !")
                else:
                    per = (int(self.var_marks.get()) * 100) / int(self.var_fullmarks.get())
                    cur.execute("INSERT INTO result (roll, name, course, marks_ob, fullmarks, per) VALUES (?, ?, ?, ?, ?, ?)",
                    ((self.var_roll.get()), 
                     self.var_name.get(), 
                     self.var_course.get(), 
                     self.var_marks.get(), 
                     self.var_fullmarks.get(), 
                     str(per)
                     ))
                    con.commit()
                    messagebox.showinfo("Success", " Result added successfully", parent = self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")            
if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()
