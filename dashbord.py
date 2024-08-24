from tkinter import *
import sqlite3
from PIL import Image, ImageTk  # for icons
from time import strftime       # for system time
from tkinter import messagebox
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass


class RMS:                      # RMS = Result Management System
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1500x800+0+0")
        self.root.config(bg = "white")
        # icon
        self.logo_dash = Image.open("images/logo_dash.png")        # dbms project/logo_dash.png
        self.logo_dash = self.logo_dash.resize((50, 50), Image.Resampling.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(self.logo_dash)
        # widget
        self.title = Label(self.root, text = "Student Management System", font = ("Helvetica", 20, "bold"), bg = "#3b3b3b", fg = "white", image = self.logo_dash, compound = LEFT, padx = 20).place(x = 0, y = 0, relwidth = 1, height = 50)
        # menu
        Menu = LabelFrame(self.root, text = "Menu", font = ("Times New Roman", 15), bg = "white")
        Menu.place(x = 20, y = 70, width = 1460, height = 70)
        # button
        button_course = Button(Menu, bg = "#414344", font = ("Helvetica", 20), text = "Course", fg = "white", cursor = "hand2", command = self.addCourse).place(x = 10, y = 0, height = 40, width = 140)
        button_student = Button(Menu, bg = "#414344", font = ("Helvetica", 20), text = "Student", fg = "white", cursor = "hand2", command = self.addStudent).place(x = 180+50, y = 0, height = 40, width = 140)
        button_result = Button(Menu, bg = "#414344", font = ("Helvetica", 20), text = "Result", fg = "white", cursor = "hand2", command = self.addResult).place(x = 350+80, y = 0, height = 40, width = 140)
        button_vsr = Button(Menu, bg = "#414344", font = ("Helvetica", 20), text = "View Student Result", fg = "white", cursor = "hand2", command = self.addReport).place(x = 530+100, y = 0, height = 40, width = 300)
        button_exit = Button(Menu, bg = "#414344", font = ("Helvetica", 20), text = "Exit", fg = "white", cursor = "hand2", command = self.exit).place(x = 860+150, y = 0, height = 40, width = 140)
        # side image
        self.bg_img = Image.open("images/bg_img.png")
        self.bg_img = self.bg_img.resize((920, 420), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg = Label(self.root, image = self.bg_img).place(x = 1500-940, y = 150, height = 420, width = 920)
        # label widgets
        self.course = Label(self.root, bg = "#263850", fg = "white", text = "Total Courses\n[00]", font = ("Helvetica", 20), bd = 10, relief = RAISED)
        self.course.place(x = 560, y = 600, width = 220)
        self.students = Label(self.root, bg = "#263850", fg = "white", text = "Total Students\n[00]", font = ("Helvetica", 20), bd = 10, relief = RAISED)
        self.students.place(x = 760 + 150, y = 600, width = 220)
        self.result = Label(self.root, bg = "#263850", fg = "white", text = "Total Results\n[00]", font = ("Helvetica", 20), bd = 10, relief = RAISED)
        self.result.place(x = 960 + 300, y = 600, width = 220)
        
        # for clock
        self.lbl_time = Label(self.root, bg = "#263850", fg = "white", font = ("Helvetica", 80), bd = 10, relief = RAISED)
        self.lbl_time.place(x = 20, y = 150, height = 420, width = 520)
        self.clock()

        # footer
        self.footer = Label(self.root, text = "Contact us for any Technical Support: 9784xxxx29", font = ("Times New Roman", 15), bg = "#121212", fg = "white", anchor = "center").pack(fill = X, side = BOTTOM)

    # to access CourseClass when it's button is pressed
    def addCourse(self):
        self.new_win = Toplevel(self.root)  # TopLevel => for launching course object window on top of root ::of RMS type::
        self.new_obj = CourseClass(self.new_win)
    def addStudent(self):
        self.new_win = Toplevel(self.root)  # TopLevel => for launching course object window on top of root ::of RMS type::
        self.new_obj = StudentClass(self.new_win)
    def addResult(self):
        self.new_win = Toplevel(self.root)  # TopLevel => for launching course object window on top of root ::of RMS type::
        self.new_obj = ResultClass(self.new_win)
    def addReport(self):
        self.new_win = Toplevel(self.root)  # TopLevel => for launching course object window on top of root ::of RMS type::
        self.new_obj = ReportClass(self.new_win)

    def clock(self):
        try:
            time_string = strftime("%H:%M:%S")
            self.lbl_time.config(text = time_string)        

            # Update labels
            con = sqlite3.Connection("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            if rows:
                self.course.config(text = f"Total Courses\n[{str(len(rows))}]")
            con.close()

            con = sqlite3.Connection("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            if rows:
                self.students.config(text = f"Total Students\n[{str(len(rows))}]")
            con.close()

            con = sqlite3.Connection("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM result")
            rows = cur.fetchall()
            if rows:
                self.result.config(text = f"Total Results\n[{str(len(rows))}]")                            
            con.close()

            self.lbl_time.after(1000, self.clock)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
    def exit(self):
        op = messagebox.askyesno("Confirm", "Do You Really Want To Exit ?")
        if op:
            self.root.quit()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()