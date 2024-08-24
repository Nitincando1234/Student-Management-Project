from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # for icons
class StudentClass:                      # RMS = Result Management System
    
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1500x600+0+180")
        self.root.config(bg = "white")
        self.root.focus_force()         # forces the root on top of RMS
        # variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_duration = StringVar()
        self.var_email = StringVar()
        self.var_a_date = StringVar()
        self.var_contact = StringVar()
        self.var_gender = StringVar()
        self.var_course = StringVar()
        self.var_dob = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # title
        self.title = Label(self.root, text = "Student Management", font = ("Helvetica", 20, "bold"), bg = "#3b3b3b", fg = "white").place(x = 20, y = 10, width = 1460, height = 50)

        # Label Widgets
        # left side
        lbl_course = Label(self.root, bg = "#414344", fg = "white", text = "Roll No", font = ("Helvetica", 20),).place(x = 20, y = 80, width = 180)
        lbl_name = Label(self.root, bg = "#414344", fg = "white", text = "Name", font = ("Helvetica", 20),).place(x = 20, y = 120 + 20, width = 180)
        lbl_email = Label(self.root, bg = "#414344", fg = "white", text = "Email", font = ("Helvetica", 20),).place(x = 20, y = 160 + 40, width = 180)
        lbl_gender = Label(self.root, bg = "#414344", fg = "white", text = "Gender", font = ("Helvetica", 20),).place(x = 20, y = 200 + 60, width = 180)

        lbl_state = Label(self.root, bg = "#414344", fg = "white", text = "State", font = ("Helvetica", 20),).place(x = 20, y = 240 + 80, width = 100)
        txt_state = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_state, font = ("Times New Roman", 14),).place(x = 160, y = 240 + 80, width = 100, height = 40)

        lbl_city = Label(self.root, bg = "#414344", fg = "white", text = "City", font = ("Helvetica", 20),).place(x = 300, y = 240 + 80, width = 100)
        txt_city = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_city, font = ("Times New Roman", 14),).place(x = 440, y = 240 + 80, width = 100, height = 40)

        lbl_pin = Label(self.root, bg = "#414344", fg = "white", text = "Pin", font = ("Helvetica", 20),).place(x = 580, y = 240 + 80, width = 100)
        txt_pin = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_pin, font = ("Times New Roman", 14),).place(x = 720, y = 240 + 80, width = 120, height = 40)

        lbl_address = Label(self.root, bg = "#414344", fg = "white", text = "Address", font = ("Helvetica", 20),).place(x = 20, y = 280 + 100, width = 180)
        # right side
        lbl_dob = Label(self.root, bg = "#414344", fg = "white", text = "D.O.B", font = ("Helvetica", 20),).place(x = 460, y = 80, width = 180)
        lbl_contact = Label(self.root, bg = "#414344", fg = "white", text = "Contact", font = ("Helvetica", 20),).place(x = 460, y = 120 + 20, width = 180)
        lbl_admission = Label(self.root, bg = "#414344", fg = "white", text = "Admission", font = ("Helvetica", 20),).place(x = 460, y = 160 + 40, width = 180)
        lbl_course = Label(self.root, bg = "#414344", fg = "white", text = "Course", font = ("Helvetica", 20),).place(x = 460, y = 200 + 60, width = 180)        
        # Entry widget
        # left side
        self.txt_roll = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_roll, font = ("Times New Roman", 14),)
        self.txt_roll.place(x = 240, y = 80, width = 180, height = 40)
        txt_name = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_name, font = ("Times New Roman", 14),).place(x = 240, y = 120 + 20, width = 180, height = 40)
        txt_email = Entry(self.root, bg = "white", fg = "black",  textvariable = self.var_email, font = ("Times New Roman", 14),).place(x = 240, y = 160 + 40, width = 180, height = 40)
        self.txt_gender = ttk.Combobox(self.root, textvariable = self.var_gender, justify = CENTER, state = "readonly", values = ("Select", "Male", "Female", "Others"), font = ("Helvetica", 14))
        self.txt_gender.place(x = 240, y = 220 + 40, width = 180, height = 40)
        self.txt_gender.current(0)

        # right side
        self.course_list = []
        self.fetch_course()
        txt_dob = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_dob, font = ("Times New Roman", 14),).place(x = 660, y = 80, width = 180, height = 40)
        txt_contact = Entry(self.root, bg = "white", fg = "black", textvariable = self.var_contact, font = ("Times New Roman", 14),).place(x = 660, y = 120 + 20, width = 180, height = 40)
        txt_admission = Entry(self.root, bg = "white", fg = "black",  textvariable = self.var_a_date, font = ("Times New Roman", 14),).place(x = 660, y = 160 + 40, width = 180, height = 40)
        self.txt_course = ttk.Combobox(self.root, textvariable = self.var_course, justify = CENTER, state = "readonly", values = self.course_list, font = ("Helvetica", 14),)
        self.txt_course.place(x = 660, y = 220 + 40, width = 180, height = 40)
        self.txt_course.set("Select")

        self.txt_address = Text(self.root, bg = "white", fg = "black", font = ("Times New Roman", 14),)
        self.txt_address.place(x = 240, y = 280 + 100, width = 600, height = 100)

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
        lbl_search_roll = Label(self.root, bg = "#414344", fg = "white", text = "Roll No", font = ("Helvetica", 20),).place(x = 880, y = 80, width = 140)
        txt_search_roll = Entry(self.root, bg = "white", fg = "black",  textvariable = self.search_var, font = ("Times New Roman", 14),).place(x = 1060, y = 80, width = 2810, height = 40)
        btn_search_roll = Button(self.root, bg = "#414344", font = ("Helvetica", 20), text = "Search", fg = "white", cursor = "hand2", command = self.search).place(x = 1380, y = 80, width = 100, height = 40)

        # Content of Search
        self.C_Frame = Frame(self.root, bd = 2)
        self.C_Frame.place(x = 880, y = 140, width = 600, height = 400)
        
        scrolly = Scrollbar(self.C_Frame, orient = VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient = HORIZONTAL)

        self.course_table = ttk.Treeview(self.C_Frame, columns =("roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command = self.course_table.xview)
        scrolly.config(command = self.course_table.yview)
        
        self.course_table.heading("roll", text = "Roll No")
        self.course_table.heading("name", text = "Name")
        self.course_table.heading("email", text = "Email Id")
        self.course_table.heading("gender", text = "Gender")
        self.course_table.heading("dob", text = "Date of Birth")
        self.course_table.heading("contact", text = "Contact")
        self.course_table.heading("admission", text = "Admission Date")
        self.course_table.heading("course", text = "Course Enrolled")
        self.course_table.heading("state", text = "State")
        self.course_table.heading("city", text = "City")
        self.course_table.heading("pin", text = "Pin")
        self.course_table.heading("address", text = "Address")

        self.course_table["show"] = "headings"

        self.course_table.column("roll", width = 150)
        self.course_table.column("name", width = 150)
        self.course_table.column("email", width = 150)
        self.course_table.column("gender", width = 150)
        self.course_table.column("dob", width = 150)
        self.course_table.column("contact", width = 150)
        self.course_table.column("admission", width = 150)
        self.course_table.column("course", width = 150)
        self.course_table.column("state", width = 150)
        self.course_table.column("city", width = 150)
        self.course_table.column("pin", width = 150)
        self.course_table.column("address", width = 150)

        self.course_table.pack(fill = BOTH, expand = 1)             # BOTH => for both height and width
        self.course_table.bind("<ButtonRelease-1>", self.get_data) # bind the events with the course table and execute some function
        self.show()
    #===============================================================================
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("") 
        self.var_email.set("") 
        self.var_gender.set("") 
        self.var_dob.set("") 
        self.var_contact.set("") 
        self.var_a_date.set("") 
        self.var_course.set("") 
        self.var_state.set("") 
        self.var_city.set("") 
        self.var_pin.set("")
        self.search_var.set("") 
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state = NORMAL)

    def get_data(self, e):
        self.txt_roll.config(state = "readonly")
        r = self.course_table.focus()
        content = self.course_table.item(r)                         # numpy array of item and their respective names
        row = content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]), 
        self.var_email.set(row[2]), 
        self.var_gender.set(row[3]), 
        self.var_dob.set(row[4]), 
        self.var_contact.set(row[5]), 
        self.var_a_date.set(row[6]), 
        self.var_course.set(row[7]), 
        self.var_state.set(row[8]), 
        self.var_city.set(row[9]), 
        self.var_pin.set(row[10]), 
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[11])
    def delete(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try :

            if self.var_roll.get() == "":              # value of variable as a string
                messagebox.showerror("Error","Required Fields Must be Filled ! ", parent = self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll = ?", (self.var_roll.get(),))
                row = cur.fetchone()                
                if row == None:
                    messagebox.showerror("Error", "Select Student from the list first !")
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to perform deletion ?", parent = self.root)     # for yes/no dialogue box
                    if op == True:
                        cur.execute("DELETE FROM student WHERE roll = ?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Success", f"{self.var_roll.get()} Student's Details Deleted successfully", parent = self.root)
                        self.clear()
                        self.show()
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")
    def add(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try :
            if self.var_roll.get() == "" or self.var_name.get() == "" or self.var_dob.get() == "" or self.txt_address.get("1.0", END) == "":              # value of variable as a string
                messagebox.showerror("Error","Required Fields Must Be Filled (Roll No, Name, Date Of Birth, Address of Student) ! ", parent = self.root)
            else:
                print(self.var_gender.get())
                cur.execute("SELECT * FROM student WHERE roll = ?", (self.var_roll.get(), ))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Student's Roll No already present in record !")
                else:
                    cur.execute("INSERT INTO student (roll, name, email, gender, dob, contact, admission, course, state, city, pin, address) VALUES (?, ?, ?, ?,?, ?, ?, ?,?,?,?,?)",
                    (int(self.var_roll.get()),
                     self.var_name.get(), 
                     self.var_email.get(), 
                     self.var_gender.get(), 
                     self.var_dob.get(), 
                     self.var_contact.get(), 
                     self.var_a_date.get(), 
                     self.var_course.get(), 
                     self.var_state.get(), 
                     self.var_city.get(), 
                     self.var_pin.get(), 
                     self.txt_address.get("1.0", END)
                     ))
                    con.commit()
                    messagebox.showinfo("Success", f"{self.var_name.get()} Student's Details added successfully", parent = self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")
    def show(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            self.course_table.delete(*self.course_table.get_children())
            rows = cur.fetchall()
            for row in rows:
                self.course_table.insert("", END, values = row)
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")

    def fetch_course(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM course")
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")

    def search(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student where roll = ?", (self.search_var.get(), ))
            self.course_table.delete(*self.course_table.get_children())
            row = cur.fetchone()
            if row:
                self.course_table.insert("", END, values = row)
            else:
                messagebox.showerror("Error","No Record Found For The Given Roll No !", parent = self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")

    def update(self):
        con = sqlite3.connect(database = "rms.db")
        cur = con.cursor()
        try :
            if self.var_roll.get() == "" or self.var_name.get() == "" or self.var_dob.get() == "" or self.txt_address.get("1.0", END) == "":              # value of variable as a string
                messagebox.showerror("Error","Required Fields Must be Filled ! ", parent = self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll = ?", (self.var_roll.get(), ))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Roll no must be present in the list !")
                else:
                    cur.execute("UPDATE student SET name = ?, email = ?, gender = ?, dob = ?, contact = ?, admission = ?, course = ?, state = ?, city = ?, pin = ?, address = ? WHERE roll = ?",
                    (
                     self.var_name.get(), 
                     self.var_email.get(), 
                     self.var_gender.get(), 
                     self.var_dob.get(), 
                     self.var_contact.get(), 
                     self.var_a_date.get(), 
                     self.var_course.get(), 
                     self.var_state.get(), 
                     self.var_city.get(), 
                     self.var_pin.get(), 
                     self.txt_address.get("1.0", END),
                     int(self.var_roll.get())
                     ))
                    con.commit()
                    messagebox.showinfo("Success", f"{self.var_roll.get()} Student Details updated successfully", parent = self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error",f"Error Due to {str(e)}")     
   
if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()