from time import sleep
from win32com import client
from Tkinter import Tk,Entry,Label,Button
import keyboard

url = "tnresults.nic.in/hsform.htm"
url = str(url)

crdelay = 5
writedelay = 4
nextdelay = 2

def dly():
    top = Tk()
    top.geometry("300x200")

    def sit():
        top.destroy()
    def sbt():
        if ce.get() == '':
            global crdelay
            crdelay = 5.0
        else:
            global crdelay
            crdelay = float(ce.get())
        if we.get() == '':
            global writedelay
            writedelay = 4.0
        else:
            global writedelay
            writedelay = float(we.get())
        if ne.get() == '':
            global nextdelay
            nextdelay = 2.0
        else:
            global nextdelay
            nextdelay = float(ne.get())
        print crdelay
        print writedelay
        print nextdelay
        top.destroy()
    
    cl = Label(top,text = "Enter Chrome Launch Delay(sec): ")
    ce = Entry(top,width = 3)
    wl = Label(top,text = "Enter Data writing Delay(sec): ")
    we = Entry(top,width = 3)
    nl = Label(top,text = "Enter Next Result Delay(sec): ")
    ne = Entry(top,width = 3)
    sa = Button(top,text = "Apply",command = sbt)
    xt = Button(top,text = "Exit",command = sit)

    cl.place(x=20,y=40)
    ce.place(x=230,y=40)
    wl.place(x=20,y=80)
    we.place(x=230,y=80)
    nl.place(x=20,y=120)
    ne.place(x=230,y=120)
    sa.place(x=110,y=160)
    xt.place(x=170,y=160)
print "Modified: "
print crdelay
print writedelay
print nextdelay

def operation():
    d = de.get()
    l = le.get()
    u = ue.get()
    root.destroy()
    
    l = int(l)
    u = int(u)
    dob = str(d)
    run = u-l+1
    rno = l
            
    

    shell = client.Dispatch("WScript.Shell")
    shell.Run("Chrome")
    print "Launched Chrome"
    print crdelay
    sleep(crdelay)
    curr = 0

    def select():
        roll = str(rno)
        keyboard.press_and_release('Ctrl+t')
        sleep(1)
        shell.SendKeys(url)
        keyboard.press_and_release('Enter')
        sleep(writedelay)
        keyboard.write(roll)
        keyboard.press_and_release('Tab')
        keyboard.write(dob)
        keyboard.press_and_release('Tab')
        keyboard.press_and_release('Enter')
        print "Processed: "
        print roll
        print dob
        sleep(nextdelay)

    while curr < run:
        select()
        curr+=1
        rno+=1
    else:
        print "DONE!"
def xit():
    root.destroy()
    exit(0)

root = Tk()
root.geometry("320x240")
root.title("RESULTS GENERATOR V2  -- KAILASH RAMESH")

dl = Label(root,text = "Enter DOB: ")
de = Entry(root)
ll = Label(root,text = "Enter the Lower Limit: ")
le = Entry(root)
ul = Label(root,text = "Enter the Upper Limit: ")
ue = Entry(root)
sub = Button(root,text = "GENERATE!",command = operation)
xyt = Button(root,text = "EXIT",command = xit)
mod = Button(root,text = "Adjust Delays",command = dly)

dl.place(x=20,y=40)
de.place(x=160,y=40)
ll.place(x=20,y=80)
le.place(x=160,y=80)
ul.place(x=20,y=120)
ue.place(x=160,y=120)
sub.place(x=80,y=170)
xyt.place(x=165,y=170)
mod.place(x=210,y=170)
root.mainloop()

        
