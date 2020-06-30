# Student Data Management System

from tkinter import *   # importing tkinter for GUI
import sqlite3


root = Tk()  # creating tkinter class object
root.title("Student Data Management")
# initializing variable
student_name = StringVar()
roll_no = StringVar()
branch = StringVar()
sem_no = StringVar()


def connection():  # Establishing database connection
    try:
        conn = sqlite3.connect("student.db")
    except:
        print("Cannot connect to the database")
    return conn


def verify():  # Checking whether required fields are filled
    a = b = c = d = 0
    if not student_name.get():
        t1.insert(END, "Student Name required!!!\n")
        a = 1
    if not roll_no.get():
        t1.insert(END, "Roll No required!!!\n")
        b = 1
    if not branch.get():
        t1.insert(END, "Branch required!!!\n")
        c = 1
    if not sem_no.get():
        t1.insert(END, "Semester required!!!\n")
        d = 1
    if a or b or c or d == 1:
        return 1
    else:
        return 0

def verifyroll():  # Roll number mandatory for updating and deleting data
    a = 0
    if not roll_no.get():
        t1.insert(END, "Roll No required!!!\n")
        a = 1
    if a == 0:
        return 0
    else:
        return 1


def available():  # checking availability of data for deletion, update based on entered roll number
    a = 0
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM STUDENTINFO WHERE ROLL=?", (int(roll_no.get()),))
    data = cur.fetchall()
    if not data:
        t1.insert(END, "NO DATA TO PROCESS\n")
        a = 1
    if a == 0:
        return 0
    else:
        return 1



def add_student():  # Function to add student details
    ver = verify()
    try:
        if ver == 0:
            conn = connection()
            cur = conn.cursor()

            cur.execute("CREATE TABLE IF NOT EXISTS STUDENTINFO(NAME TEXT,ROLL INTEGER PRIMARY KEY,BRANCH TEXT,SEMESTER TEXT)")
            cur.execute("INSERT INTO STUDENTINFO VALUES(?,?,?,?)", (student_name.get(), roll_no.get(), branch.get(), sem_no.get()))
            conn.commit()
            conn.close()
            t1.insert(END, "ADDED SUCCESSFULLY\n")
    except sqlite3.IntegrityError:
        t1.insert(END, "DUPLICATION OF ROLL NUMBER NOT ALLOWED\n")



def view_student():  # Displays Student details
    label_list = ['Name: ', 'Roll No: ', 'Branch: ', 'Sem: ']
    conn = connection()
    cur = conn.cursor()
    cur.execute('SELECT * from STUDENTINFO')
    data = cur.fetchall()
    if not data:
        t1.insert(END, "NO DATA TO DISPLAY\n")

    conn.close()

    for i in data:  # unpacking each element of the tuple
        disp = list(map(lambda z, y: z+str(y), label_list, i))  # For simultaneous display from 2 lists
        for x in disp:
            t1.insert(END, " " + str(x)+" ")
        t1.insert(END, "\n")




def delete_student():  # Deletes student data

    ver = verifyroll()
    if ver == 0:
        avl = available()
        if avl == 0:
            conn = connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM STUDENTINFO WHERE ROLL=?", (int(roll_no.get()),))
            conn.commit()
            conn.close()
            t1.insert(END, "SUCCESSFULLY DELETED THE USER\n")

def update_student():  # Updates Student details

    ver = verifyroll()
    if ver == 0:
        avl = available()
        if avl == 0:

            conn = connection()
            cur = conn.cursor()
            cur.execute('UPDATE STUDENTINFO SET NAME = ?, BRANCH = ?, SEMESTER = ? where ROLL=?', (student_name.get(), branch.get(), sem_no.get(), roll_no.get()))
            conn.commit()
            conn.close()
            t1.insert(END, "SUCCESSFULLY UPDATED THE USER\n")

def clse():
    sys.exit()


# creating labels

label1 = Label(root, text="Student name:")
label1.place(x=0, y=0)

label2 = Label(root, text="Roll no:")
label2.place(x=0, y=30)

label3 = Label(root, text="Branch:")
label3.place(x=0, y=60)

label4 = Label(root, text="Semester No:")
label4.place(x=0, y=90)

# entering data
entry1 = Entry(root, textvariable=student_name)
entry1.place(x=100, y=0)

entry2 = Entry(root, textvariable=roll_no)
entry2.place(x=100, y=30)

entry3 = Entry(root, textvariable=branch)
entry3.place(x=100, y=60)

entry4 = Entry(root, textvariable=sem_no)
entry4.place(x=100, y=90)

# Text box for display
t1 = Text(root, width=80, height=21.5)
t1.place(x=300, y=0)

# Buttons for addition,deletion, update and other functions
b1 = Button(root, text="ADD STUDENT DETAILS", command=add_student, width=40)
b1.place(x=0, y=200)
b2 = Button(root, text="DISPLAY STUDENT DETAILS", command=view_student, width=40)
b2.place(x=0, y=240)
b3 = Button(root, text="DELETE STUDENT DETAILS", command=delete_student, width=40)
b3.place(x=0, y=280)
b4=Button(root, text="UPDATE INFORMATION", command=update_student, width=40)
b4.place(x=0, y=320)
b5=Button(root,text="CLOSE", command=clse, width=40)
b5.place(x=0, y=360)

root.mainloop()
