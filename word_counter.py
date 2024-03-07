from tkinter import *
import re 

win=Tk()

win.geometry("800x800")

win.title("WORD COUNTER")

no_of_words=0
value=0


def clear_default(e):
    text1.delete(1.0,END)
    text1.unbind("<FocusIn>")
    

def chars(b):
    
    def clear_default1(b):
    
        text1.delete(1.0,END)
        text1.unbind("<FocusIn>")
    
    global no_of_words
    
    global value
    
    label5.config(text=' ')
    valid= re.findall(r"[a-zA-Z0-9_@*]+",text1.get(1.0,END))
    
    no_of_words=len(valid)
    
  
    text1.config(state='normal')
        
    length=len(text1.get(1.0,END))
    value=str(length-1)
    label4.config(text=value)
            
                
           
    label3.config(text=str(no_of_words)+'/'+'10') 
    
    if int(value)==0:
        
        text1.insert(1.0,'Start entering your text here.......')
        win.focus_set()
        print(win.focus_set())

        text1.bind("<FocusIn>", lambda e:clear_default1(e))


def submit():
    global value
    global no_of_words
    label5.config(text="There are "+ str(value) + ' characters ' + ' and ' + str(no_of_words) + ' words ')   
    
def clear():
    
    def clear_default1(b):
        
        text1.delete(1.0,END)
        text1.unbind("<FocusIn>")
    
    
    global no_of_words
    global value
    
    
    
        
    text1.delete(1.0,END)
    no_of_words=0
    value=0
    label3.config(text=str(no_of_words)+'/'+'10')
    label4.config(text=str(value))
    label5.config(text=' ')
    
    text1.insert(1.0,'Start entering your text here.......')
    win.focus_set()
    text1.bind("<FocusIn>", lambda e:clear_default1(e))
        
    
def undo():
    
    def clear_default1(b):
        
        text1.delete(1.0,END)
        text1.unbind("<FocusIn>")
        return
    global no_of_words
    global value
       
    
    label5.config(text=' ')
    
    if int(value)>0:
    
        data = text1.get(1.0,'end-2c')
        text1.delete(1.0,END)
        text1.insert(1.0,data)
        count=int(value)-1
    
    
        
    if count>0:
        value=str(count)
        valid= re.findall(r"[a-zA-Z0-9_@*]+",text1.get(1.0,END))
                
        no_of_words=len(valid)
         
        label3.config(text=str(no_of_words)+'/'+'10')
        label4.config(text=str(value))
            
    elif count==0:
        value=0
        no_of_words=0
        label3.config(text=str(no_of_words)+'/'+'10')
        label4.config(text=str(value))
        
        
        text1.insert(1.0,'Start entering your text here.......')
        win.focus_set()
        text1.bind("<FocusIn>", lambda e:clear_default1(e))
    else:
        value=0
        no_of_words=0
        label3.config(text=str(no_of_words)+'/'+'10')
        label4.config(text=str(value))
        
        
    
label1=Label(win,text='Total Words:', font=("Arial",15))
label1.place(x=5,y=10)

label2=Label(win, text='Total Chars:',font=("Arial",15))
label2.place(x=1000,y=10)
label3=Label(win, text='0/10', font=("Arial",15))
label3.place(x=150,y=10)

label4=Label(win, text='0',font=("Arial",15))
label4.place(x=1150,y=10)

text1=Text(win,width=110,relief=RAISED,height=20,takefocus=0,font=("Arial",15),fg='grey',wrap=WORD,spacing1=1)
text1.place(x=5,y=50)
    
text1.insert(1.0,'Start entering your text here.......')
text1.bind("<FocusIn>", lambda e:clear_default(e))

label5=Label(win,text=' ',font=("Arial",25),fg='blue')
label5.place(x=400,y=600)

btn2=Button(win,text='CLEAR',font=("Arial",17), command=clear,fg='grey')
btn2.place(x=700,y=550)

btn3=Button(win,text='UNDO',font=("Arial",17),command=undo,fg='grey')
btn3.place(x=900,y=550)

btn1=Button(win,text='SUBMIT',font=("Arial",17),command=submit,fg='grey')
btn1.place(x=500,y=550)

text1.bind('<KeyRelease>', lambda a :chars(a))

win.mainloop()
