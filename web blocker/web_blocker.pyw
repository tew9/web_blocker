from tkinter import *
from datetime import datetime as dt
import time



#user_end = endent.get()
#stat1 = variable.get()
#stat2 = variable2.get()

host_loc = r"C:\Windows\System32\drivers\etc\hosts"
#Ip address to which the blocked websites will be redirected
host_loc = 'hosts'
redirect_Ip = "127.0.0.1"
websites = ["www.facebook.com","facebook.com","www.google.com/mail","gmail.com",]


def toggle():
    if (block['text']=="Run The Blocker"):
        block['text'] = 'Running...'
        block['relief'] = 'sunken'
        block['bg'] = 'red'
        return block['text']
    else:
        block['text'] = "Run The Blocker"
        block['relief'] = 'solid'
        block['bg'] = 'green'
        return block['text']

def calculate():
    user_start = startent.get()
    st_hour = int(user_start[0:2])
    st_min = int(user_start[3:])
    cur_time = dt.now()
    work_start = dt(cur_time.now().year,cur_time.now().month,cur_time.now().day,st_hour,st_min)

    user_end = endent.get()
    end_hour = int(user_end[0:2])
    end_min = int(user_end[3:])
    work_end = dt(cur_time.now().year,cur_time.now().month,cur_time.now().day,
    end_hour,end_min)
    if work_start < cur_time < work_end:
         return True
    else:
        return False

def workhour():
    txt = toggle()
    work = calculate()
    print(txt,work)

    while txt=='Running...':
        if work == True:
            window.wm_state('iconic')
            with open(host_loc,'r+') as f:
                file_data = f.read()
                for web in websites:
                    if web in file_data:
                        pass #don't execute this line,try the other one

                    else:
                            f.write(redirect_Ip+' '+web+'\n')
        else:
            window.lift()
            block['text'] = 'Run the blocker'
            block['relief'] = 'solid'
            block['bg'] = 'green'
            with open(host_loc,'r+') as f:
                file_lines = f.readlines()
                f.seek(0)
                for lines in file_lines:
                    if any(web in lines for web in websites):
                        pass
                    else:
                        #print('fun time...')
                        f.write(lines)
                    f.truncate()
            break
        time.sleep(5)


window = Tk()
window.wm_title("simple web_blocker")

lab1 = Label(window,text="start time: ")
lab1.grid(row=0,column=0)

lab2 = Label(window,text="End time: ")
lab2.grid(row=1,column=0)

startent = StringVar()
ent1 = Entry(window, textvariable = startent)
ent1.grid(row=0,column=1)

endent = StringVar()
ent2 = Entry(window,textvariable = endent)
ent2.grid(row=1,column=1)

btext = StringVar()
block = Button(window,text="Run The Blocker",padx=0.0,pady=0.0,relief=GROOVE,activebackground = 'blue',bg='green',highlightthickness = 2,command=workhour) #SUNKEN MAKES BUTTON LOOK HOLD DOWN
                                                                            # RAISED MAKES BUTON LOOK UP
block.grid(row=4,column=1)

variable = StringVar(window)
variable.set("AM")
menu1 = OptionMenu(window, variable, "AM", "PM")
menu1.grid(row=0,column=2)
menu_1 = menu1.winfo_children()[0]
menu_1.configure(bg='red')

variable2 = StringVar(window)
variable2.set("PM")
w = OptionMenu(window, variable2, "PM", "AM")
w.grid(row=1,column=2)
menu = w.winfo_children()[0]
menu.configure(bg='blue')

ent1.insert(END,"00:00")
ent2.insert(END,"00:00")


window.mainloop()
