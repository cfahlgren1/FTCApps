from tkinter import *
import sys,math,random,datetime,os,time,codecs,webbrowser,os.path
import tkinter.messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showerror
from time import gmtime, strftime
#from docx import Document
#from docx.shared import Inches
import xlsxwriter

export = "Excel"
job = "No Job"
current_time = strftime("%m-%d-%Y", gmtime())
root = Tk()

TextArea = Text(width=60,height=17,pady=0)
task = Entry(width=90)
task.insert(10, "Task:")
e1 = Entry()
e1.insert(10, "First Name")
e2 = Entry()
e2.insert(10, "Last Name")
TextArea.insert(END, "Reflection:")
title = ["Titan Tech ", "Caleb Fahlgren made this!", "Python is life!", "FIRST Robotics!","This program is over 200 lines of code!"]
title = (random.choice(title))
root.title(title)
root.geometry("680x600")

#Submit Button
#This definition writes to the excel file
def Submit():
    submit = tkinter.messagebox.askquestion("Submit Entry", "Are you sure you want to submit?")
    if submit == "yes":
        current_time = strftime("%m-%d-%Y %H:%M", gmtime())
        fullname = "%s %s" % (e1.get(), e2.get())
        lastname = "%s" % (e2.get())
        task1 = "%s" % (task.get())
        alltext = TextArea.get("1.0",END)

        if (os.path.exists('Titan Tech ' + (strftime("%m-%d-%Y", gmtime())) + '.xlsx')):
            overwrite = tkinter.messagebox.askquestion("Overwrite","Are you sure you want to overwrite an existing file!")
            if overwrite == "yes":
                workbook = xlsxwriter.Workbook('Titan Tech ' + (strftime("%m-%d-%Y", gmtime())) + '.xlsx')
            elif overwrite == "no":
                excelpath = tkinter.filedialog.asksaveasfilename()
                if excelpath != None:
                    try:
                        workbook = xlsxwriter.Workbook(excelpath + 'Titan Tech ' + (strftime("%m-%d-%Y", gmtime())) + '.xlsx')
                    except TypeError:
                        return
                else:
                    return
        else:
            workbook = xlsxwriter.Workbook('Titan Tech ' + (strftime("%m-%d-%Y", gmtime())) + '.xlsx')


        worksheet = workbook.add_worksheet()
        format_text = workbook.add_format()
        format_text.set_text_wrap()
        cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'text_wrap': 1})
        middle = workbook.add_format({'align':'center'})
        worksheet.merge_range('A5:G20', "", cell_format)
        cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'text_wrap': 1})
        worksheet.merge_range('A3:G4', "", cell_format)
        bold = workbook.add_format({'bold': 1})
        worksheet.write('A1', 'Name:',bold)
        worksheet.write_rich_string('A3', task1,cell_format)
        worksheet.write_string('B1',fullname, bold)
        worksheet.merge_range('A2:B2', "", cell_format)
        worksheet.merge_range('D2:E2', "", cell_format)
        worksheet.write_string('A2',"Student Initials")
        worksheet.write_string('C2',"_______",middle)
        worksheet.write_string('D2',"Mentor Initials")
        worksheet.write_string('F2',"_______",middle)
        worksheet.write('E1', 'Date:',bold)
        worksheet.write('F1',(strftime("%m-%d-%Y", gmtime())),bold)
        worksheet.write_rich_string('A5',alltext,cell_format)
        userconfirm = tkinter.messagebox.showinfo("Save","Your entry has been saved to an " + export + " document!")
        workbook.close()

def Reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()

def Quit():
    quitask = tkinter.messagebox.askquestion("Quit", "Are you sure you want to quit?")
    if quitask == "yes":
        root.destroy()


firstname = Label(root, text="First Name",font=("Helvetica", 12),fg="green")
lastname = Label(root, text="Last Name",font=("Helvetica", 12),fg="green")
time = Label(root, text=current_time, font=("Helvetica", 12),fg="black")

ScrollBar = Scrollbar(root)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=RIGHT, fill=Y)


def cf():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Caleb")
    e2.insert(10, "Fahlgren")
def al():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 2")
def cm():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 3")
def np():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 4")
def cp():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 5")
def ns():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 6")
def ct():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 7")
def kt():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 8")
def mt():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 9")
def ek():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Sample")
    e2.insert(10, "Name 10")
def n():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e1.insert(10, "Team")
    e2.insert(10, "Name")
def other():

    e1.delete(0, 'end')
    e2.delete(0, 'end')

def TextFile():
    current_time = strftime("%m-%d-%Y", gmtime())
    fullname = "%s %s" % (e1.get(), e2.get())
    lastname = "%s" % (e2.get())
    task1 = "%s" % (task.get())
    alltext = TextArea.get("1.0",END)
    textfile1 = tkinter.messagebox.askquestion("Text File", "Are you sure you want to export as a text file?")
    if textfile1 == "yes":
        textfile = open('Titan Tech' + (strftime("%m-%d-%Y", gmtime())) + '.txt',"w")
        textfile.write("Titan Tech  | Team # 10385   ")
        textfile.write("Name: " + fullname)
        textfile.write("        " + "Date: " + current_time)
        textfile.write('\n' + '\n' + task1)
        textfile.write('\n' + '\n' + alltext)
        textfile.close()
        tkinter.messagebox.showinfo("Save", "You have exported to text file successfully. It is in the location of this program.")

def helpmenusave():
    helpsaveconfirm = tkinter.messagebox.showinfo("Save", "This program exports the Excel, Text, HTML to the location of this program!")

def userinterfacemenu():
    helpuserinterface = tkinter.messagebox.showinfo("User Interface", "The Users tab is where you can click on your name to autofill the name text boxes. The Export tab is where you choose to export to a specific format.")

def Open():
    textopen = tkinter.filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt'),('Java', '*.java'),('Python','*.py'),('All Files', '*')])
    try:
        if textopen != None:
            txtopen = textopen.read()
            TextArea.delete(1.0,END)
            TextArea.insert(END,txtopen)
            tkinter.messagebox.showinfo("Open",  "Success!")
            try:
                txtopen.close()
            except AttributeError:
                pass
    except UnicodeDecodeError:
        tkinter.messagebox.showinfo("Failed","This is not a text file!")
        return


def html():
    alltext = TextArea.get("1.0",END)
    htmlcode = open("TitanTechHTML" + ".html", "w")
    htmlcode.write(alltext)
    htmlcode.close()
    webbrowser.open_new_tab("TitanTechHTML.html")
    tkinter.messagebox.showinfo("HTML Code", "Your code is running and will pop up in your default browser.")

def cmd():
    alltext = TextArea.get("1.0",END)
    command = open('command.bat','w')
    command.write(alltext)
    os.system("command.bat")
    if (os.path.exists("command.bat")):
        os.remove("command.bat")


menubar = Menu(root)
filemenu = Menu(menubar,tearoff = 0)
filemenu.add_command(label="New",command=Reset)
filemenu.add_command(label="Open",command=Open)
filemenu.add_command(label="Exit",command=Quit)
menubar.add_cascade(label="File",menu=filemenu)

#help menu
helpmenu = Menu(menubar,tearoff = 0)
helpmenu.add_command(label="None", command=n)
helpmenu.add_command(label="Caleb Fahlgren", command=cf)
helpmenu.add_command(label="Sample Name 2", command=al)
helpmenu.add_command(label="Sample Name 3", command=cm)
helpmenu.add_command(label="Sample Name 4", command=np)
helpmenu.add_command(label="Sample Name 5",command=cp)
helpmenu.add_command(label="Sample Name 6",command=ns)
helpmenu.add_command(label="Sample Name 7",command=ct)
helpmenu.add_command(label="Sample Name 8",command=kt)
helpmenu.add_command(label="Sample Name 9",command=mt)
helpmenu.add_command(label="Sample Name 10", command=ek)
helpmenu.add_command(label="Other", command=other)
menubar.add_cascade(label="Users",menu=helpmenu)

def Word():
    current_time = strftime("%m-%d-%Y", gmtime())
    lastname = "%s" % (e2.get())
    fullname = "%s %s" % (e1.get(), e2.get())
    task1 = "%s" % (task.get())
    alltext = TextArea.get("1.0",END)
    wordsaveask = tkinter.messagebox.askquestion("Save", "Are you sure you want to export to a Microsoft Word file?")
    if wordsaveask == ("yes") :
        try:
            document = Document()
            document.add_heading('FTC Titan Tech Summary', 0)
            document.add_paragraph('Titan Tech  | Team # 10385')
            document.add_paragraph('Mentor Initials ____           Student Initials _____')
            document.add_paragraph('Name: ' + fullname)
            document.add_paragraph('Date: ' + current_time)
            document.add_paragraph(task1)
            document.add_paragraph(alltext)
            document.save('Titan Tech ' + (strftime("%m-%d-%Y", gmtime())) + '.docx')
            tkinter.messagebox.showinfo('Save', 'The program has exported the information to a Microsoft Word document!')
        except PermissionError:
            tkinter.messagebox.showinfo('Error' + ' You need Write privledges to this directory.')

def developerinfo():
    tkinter.messagebox.showinfo("Developers","Caleb Fahlgren developed this in Python starting in 2015-2016. This app is copyrighted under the GNU General Public License")

#export
exportmenu = Menu(menubar, tearoff = 0)
exportmenu.add_command(label="Microsoft Excel",command=Submit)
#exportmenu.add_command(label="Microsoft Word",command=Word)
exportmenu.add_command(label="Text File",command=TextFile)
exportmenu.add_command(label="HTML Web File", command=html)
menubar.add_cascade(label="Export",menu=exportmenu)

codemenu = Menu(menubar, tearoff = 0)
codemenu.add_command(label="HTML Code",command = html)
codemenu.add_command(label="Command Line",command = cmd)
menubar.add_cascade(label="Code",menu=codemenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="Save Help", command=helpmenusave)
helpmenu.add_command(label="User Interface", command=userinterfacemenu)
menubar.add_cascade(label="Help",menu=helpmenu)


developermenu = Menu(menubar, tearoff = 0)
developermenu.add_command(label="Who is the developer?",command=developerinfo)
menubar.add_cascade(label="Developer", menu=developermenu)
root.config(menu=menubar)

Submit = Button(root, fg="white", bg="green", text="Submit", width=50, command=Submit, activebackground="yellow")
Quit = Button(root, fg="white", bg="green", text="Quit", width=50, command=Quit,activebackground="yellow")

root.bind_all('<Key>', keypress)
firstname.pack()
e1.pack()
lastname.pack()
e2.pack()
time.pack()
task.pack()
TextArea.pack(expand=YES, fill=BOTH)
Submit.pack()
Quit.pack()
mainloop()
