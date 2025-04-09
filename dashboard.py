from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title('Student Result Management System')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='white')

        self.logo_dash = ImageTk.PhotoImage(file='logo_p.png')
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash,
                      font=('goudy old style', 20, 'bold'), bg='#033054', fg='white').place(x=0, y=0, relwidth=1,
                                                                                             height=50)

        # ========== MENU BUTTONS ==========
        M_Frame = LabelFrame(self.root, text='Menus', font=('times new roman', 15), bg='white')
        M_Frame.place(x=10, y=70, width=1340, height=80)

        Button(M_Frame, text='Course', font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white', cursor='hand2',
               command=self.add_course).place(x=20, y=5, width=200, height=40)
        Button(M_Frame, text='Student', font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white', cursor='hand2',
               command=self.add_student).place(x=240, y=5, width=200, height=40)
        Button(M_Frame, text='Result', font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white', cursor='hand2',
               command=self.add_result).place(x=460, y=5, width=200, height=40)
        Button(M_Frame, text='View Student Results', font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white',
               cursor='hand2', command=self.add_report).place(x=680, y=5, width=200, height=40)
        Button(M_Frame, text='Exit', font=('goudy old style', 15, 'bold'), bg='#0b5377', fg='white', cursor='hand2',
               command=self.exit_).place(x=1120, y=5, width=200, height=40)

        footer = Label(self.root, text="VHD-Student Result Management System\nContact us for any Technical Issue: 8469304210",
                       font=('goudy old style', 12,), bg='#262626', fg='white').pack(side=BOTTOM, fill=X)

        # =================== IMAGE SLIDER =======================
        self.images = [
            'success  images/s1.jpg',
            'success  images/s2.jpeg',
            'success  images/s3.jpg',
            'success  images/s4.jpg',
            'success  images/s5.jpg',
            'success  images/s6.jpg',
            'success  images/s7.jpg',
        ]
        self.image_index = 0

        bg_Fram = Frame(self.root, bg='white')
        bg_Fram.place(x=400, y=180, width=920, height=340)

        self.display_image = Label(bg_Fram)
        self.display_image.place(x=0, y=0, width=920, height=340)
        self.show_image(self.image_index)

        Button(bg_Fram, text='<', font=("Verdana", 25), command=self.prev_image, bg='white',bd=0, fg='black').place(x=0, y=140)
        Button(bg_Fram, text='>', font=("Verdana", 25), command=self.next_image, bg='white', bd=0,fg='black').place(x=880, y=140)

        # side image
        self.bg_img1 = Image.open('images/side.png')
        self.bg_img1 = self.bg_img1.resize((340, 430))
        self.bg_img1 = ImageTk.PhotoImage(self.bg_img1)
        Label(self.root, image=self.bg_img1).place(x=40, y=180, width=350, height=450)

        # info labels
        self.lbl_course = Label(self.root, text='Total Courses\n [0]', font=('goudy old style', 20), bd=10, relief=RIDGE,
                                bg='#e43b06', fg='white')
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text='Total Students\n [0]', font=('goudy old style', 20), bd=10, relief=RIDGE,
                                 bg='#0676ad', fg='white')
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text='Total Results\n [0]', font=('goudy old style', 20), bd=10, relief=RIDGE,
                                bg='#038074', fg='white')
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        self.update_details()

    def show_image(self, index):
        img = Image.open(self.images[index])
        img = img.resize((920, 340))
        img = ImageTk.PhotoImage(img)
        self.display_image.configure(image=img)
        self.display_image.image = img

    def next_image(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        self.show_image(self.image_index)

    def prev_image(self):
        self.image_index = (self.image_index - 1) % len(self.images)
        self.show_image(self.image_index)

    def update_details(self):
        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f'Total Courses\n[{str(len(cr))}]')

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f'Total Students\n[{str(len(cr))}]')

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f'Total Results\n[{str(len(cr))}]')

            self.lbl_course.after(200, self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to {str(ex)}')

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def exit_(self):
        op = messagebox.askyesno("Confirm", 'Do you really want to Exit?', parent=self.root)
        if op == True:
            self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    Obj = RMS(root)
    root.mainloop()
