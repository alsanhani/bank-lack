from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
import cv2
from PIL import ImageTk, Image
from matplotlib import image
import mysql.connector as mc
import sys
from re import L
from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
from tkinter import filedialog
import os

root = Tk()
im_0=Image.open('C:\\Users\\pc\\Desktop\\L\\logo2.jpg')
bn_0=ImageTk.PhotoImage(im_0)
root.geometry('800x700')
root.title('lock')
root.iconbitmap('C:\\Users\\pc\\Desktop\\L\\ml.ico') 
lb_0=Label(root , image=bn_0)
lb_0.place(x=0 ,y=0)
root.resizable(False,False)

#-------------🙄large funcation🙄---------ok---------🙄large funcation🙄-----------------
def ok():
    uname=e1.get()
    passwo=e2.get()
    mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "pyqt5"
                )
    mycursor = mydb.cursor()
    query = "SELECT * FROM users WHERE name='"+ uname + "' and password='"+passwo+"'"
    mycursor.execute(query)
    result = mycursor.fetchone()
            
    if result :

#----------start program blaod bank 😁------------------------
        root = Tk()
        im1_0=Image.open('C:\\Users\\pc\\Desktop\\L\\logo2.jpg')
        bn1_0=ImageTk.PhotoImage(im1_0)

        root.title('Bload Bank')
        root.geometry('800x700+500+100')
        root.config(background='#FD5D5D')
        root.resizable(False,False)
        wel = pyttsx3.init() # نجهز المكتبة
        voices = wel.getProperty('voices')
        wel.setProperty('voice',voices[1].id) # هات خاصة الصوت 

        def Speak(audio):
            wel.say(audio) # اذا كان جاهز
            wel.runAndWait() # شغل وانتضر الاوامر مني 

        def TakeCommands():
            command= sr.Recognizer() # امر استدعاء
            with sr.Microphone() as mic:  # مع فتح المكرفون
                command.phrase_threshold= 0.1 # دقة التسجيل
                audio = command.listen(mic)
            try:
                query = command.recognize_google(audio, language='ar')
            except Exception as Error:
                print(Error)
            return query.lower()

        def b1():
            query = TakeCommands()
            name = query
            E1.insert(0,name)
        def b2():
            query = TakeCommands()
            name = query
            E2.insert(0,name)
        def b3():
            query = TakeCommands()
            name = query
            E3.insert(0,name)
        def b4():
            query = TakeCommands()
            name = query
            E4.insert(0,name)
        def b5():
            query = TakeCommands()
            name = query
            E5.insert(0,name)
  
        def Sv():
            namefile = E1.get()
            name = E1.get()
            co   = E2.get()
            j  = E3.get()
            j1 = E4.get()
            j2  = E5.get()
            sp='  ,  '
            go='   👍🏻'
            a1=' NAME : '
            a2=' , OLD : '
            a3=' , ADDERS : '
            a4=' , Quantity : '
            a5=' , PHAON : '
            info = qrcode.make(a1 +name + a2 + co + a3 + j + a4 + j1 + a5  + j2 + go)
            info.save('Donors//'+namefile+'.jpg')
            messagebox.showinfo('Save','Save [' +namefile+ '] Donors')

#------------start program Qr-code 😁----------------------------
        def p_scan():
    
            window = Tk()
            window.geometry('310x435+500+100')
            window.title('Qr-code scanner')
            window.config(background='#FD5D5D')
            def open():
                file = filedialog.askopenfile(mode='r',filetypes=[('Files','*.jpg')])
                if file:
                    filepath =os.path.abspath(file.name)
                    Ent1.insert(0,str(filepath))

            def scan():
                d = Ent1.get()
                res = cv2.QRCodeDetector()
                val , points , s_qr = res.detectAndDecode(cv2.imread(d))
                messagebox.showinfo('Qr-Scan',val)   
                     
            text = Label(window,text='QR_SCANNER',fg='white',bg='#D82148' ,font=('Stencil',10))
            text.pack(fill=X)
            lbl1 = Label(window, text='QR-code Scanner', bg='#FD5D5D', font=('Stencil',15)) 
            lbl1.place(x=40,y=40,width=230,height=190)
            Ent1 = Entry(window,font=('Tajawal',12),width=31)
            btn = Button(window, text='Select Image',fg='black',bg='#FFF7BC',width=27,font=('Stencil',12),command=open)
            btn.place(x=10,y=340)
            btn1 = Button(window, text='Read QR-code',fg='black',bg='#FFF7BC',width=27,font=('Stencil',12),command=scan)
            btn1.place(x=10,y=383)   
            window.mainloop()

#-------------- end program Qr-code 😉-----------------------
        t0 = Label(root, text='BLOAD BANK',fg='white',bg='#D82148',font=('Stencil',21))
        t0.pack(fill=X)
        l = Label(root, text='Donors name :', fg='black',bg='white',font=('Stencil',12))
        l.place(x=70,y=190)

        l1 = Label(root, text='the age :', fg='black',bg='white',font=('Stencil',12))
        l1.place(x=70,y=230)

        l2 = Label(root, text='the address :', fg='black',bg='white',font=('Stencil',12))
        l2.place(x=70,y=270)

        l3 = Label(root, text='Quantity :', fg='black',bg='white',font=('Stencil',12))
        l3.place(x=70,y=310)

        l4 = Label(root, text='the phone :', fg='black',bg='white',font=('Stencil',12))
        l4.place(x=70,y=350)

        E1 = Entry(root,font=('Tajawal',14))
        E1.place(x=200,y=190)

        E2 = Entry(root,font=('Tajawal',14))
        E2.place(x=200,y=230)

        E3 = Entry(root,font=('Tajawal',14))
        E3.place(x=200,y=270)
 
        E4 = Entry(root,font=('Tajawal',14))
        E4.place(x=200,y=310)

        E5 = Entry(root,font=('Tajawal',14))
        E5.place(x=200,y=350)

        b1=Button(root,text='🔊 ',bg='black',fg='white',font=('Tajawal',9),command=b1)
        b1.place(x=410,y=190)

        b2=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b2)
        b2.place(x=410,y=230)

        b3=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b3)
        b3.place(x=410,y=270)

        b4=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b4)
        b4.place(x=410,y=310)

        b5=Button(root,text='🔊',bg='black',fg='white',font=('Tajawal',9),command=b5)
        b5.place(x=410,y=350)

        b_save=Button(root,text='Save ✔',fg='black',bg='#FFF7BC',font=('Stencil',10),command=Sv)
        b_save.place(x=450,y=350)

        b_save2=Button(root,text='Select code-Image',fg='black',bg='#FFF7BC',font=('Stencil',10),command=p_scan)
        b_save2.place(x=650,y=50)
       
        root.mainloop()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^or in ok funcation^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    else :
                global er
                er=Label(f1,text='error password !!',fg='red',bg='white')
                er.place(x=200,y=160)
                s = cv2.VideoCapture(0)
                ret,image = s.read()
                cv2.imwrite('lock.png',image)
                del(s) 
  
#-------------🙄end large funcation🙄---------ok---------🙄end large funcation🙄-----------------
 


#---------Addyuser---------------
def addyuser():   
        window1 = Tk()
        window1.geometry('400x250')
        window1.title('singe in')
        def signup():
            username = e11.get()
            password = e22.get()
            if (username and password):
                    
                mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "pyqt5"
                )
                mycursor = mydb.cursor()
                query = "INSERT INTO users(id, name,password) VALUES(NULL,'"+ username + "','"+password+"')"
                mycursor.execute(query)
                mydb.commit()
                result = mycursor.fetchone()
                if result:
                    window1.quit()
                else :
                    print (result)
            else : 
                 print("Rerite pass")
                        #fram sing in
        t11 = Label(window1, text='ENTER USERNAME :',fg='black',bg='whitesmoke',font=('Stencil',12))
        t11.place(x=30,y=50)
 
        e11 = Entry(window1,justify=CENTER,font=('Impact',15),bd=2,relief=RIDGE,width=15,bg='white',fg='#D82148')
        e11.place(x=180,y=50)

        t22 = Label(window1, text='ENTER PASSWORD :',fg='black',bg='whitesmoke',font=('Stencil',12))
        t22.place(x=30,y=100)

        e22 = Entry(window1,justify=CENTER,font=('Impact',15),bd=2,relief=RIDGE,width=15,bg='white',fg='#D82148')
        e22.place(x=180,y=100)
 
        b33 = Button(window1,text='ok',fg='red',font=('Stencil',20),bg='whitesmoke',bd=0,relief=GROOVE,width=3,cursor='hand2',command=signup)
        b33.place(x=290,y=160)

        b00 = Button(window1,text='✔',fg='red',font=('Stencil',20),bg='whitesmoke',bd=0,relief=GROOVE,width=3,cursor='hand2',command=window1.destroy)
        b00.place(x=200,y=160)



#--------------------------start program lack😎 --------------------------------
                

t = Label(root, text='screen lock',fg='white',bg='#D82148',font=('Stencil',21))
t.pack(fill=X)

b_save2=Button(root,text='Add User',fg='white',bg='red',font=('Tajawal',12),command=addyuser)   
b_save2.place(x=685,y=45)

#------------Frame enter to --------------------------
f1 = Frame(root,bg='whitesmoke')
f1.place(x=90,y=70,width=400,height=250)

t1 = Label(f1, text='ENTER USERNAME :',fg='black',bg='whitesmoke',font=('Stencil',12))
t1.place(x=30,y=50)
 
e1 = Entry(f1,justify=CENTER,font=('Impact',15),bd=2,relief=RIDGE,width=15,bg='white',fg='#D82148')
e1.place(x=180,y=50)

t2 = Label(f1, text='ENTER PASSWORD :',fg='black',bg='whitesmoke',font=('Stencil',12))
t2.place(x=30,y=100)

e2 = Entry(f1,justify=CENTER,font=('Impact',15),bd=2,relief=RIDGE,width=15,bg='white',fg='#D82148')
e2.place(x=180,y=100)

b3 = Button(f1,text='✔',fg='red',font=('Stencil',20),bg='whitesmoke',bd=0,relief=GROOVE,width=3,cursor='hand2',command=ok)
b3.place(x=290,y=160)

root.mainloop()
#--------------------------end program lack😎 --------------------------------