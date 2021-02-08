#Importing tkinter &messagebox 
import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("Flames")
n1=tk.StringVar()
n2=tk.StringVar()
res=tk.StringVar()
def match():
    name1=str(n1.get())
    name2=str(n2.get())
    name1=name1.lower()
    name2=name2.lower()
    flames='flames'
    if len(name1)<len(name2):
      for x in name1:
        for y in name2:
          if x==y:
            name1=name1.replace(x,'',1)
            name2=name2.replace(y,'',1)
            break
    else:
      for x in name2:
        for y in name1:
          if x==y:
            name1=name1.replace(x,'',1)
            name2=name2.replace(y,'',1)
            break
    combined_length=len(name1)+len(name2)
    flames_len=len(flames)
    count=0
    while flames_len>1:
        for i in flames:
            count+=1
            if count==combined_length:
                count=0
                flames=flames.replace(i,'')
                flames_len-=1
                break
    #Driving Meaning for the FLAMES character
    if flames=='f':
        result="Friends"
        messagebox.showinfo("Friend","Good Friends")
    elif flames=='l':
        result="Love each other"
        messagebox.showinfo("Love","Love each other")
    elif flames=='a':
        result="Affectionated"
        messagebox.showinfo("Affection","You both are more Affectionated")
    elif flames=='m':
        result="Marriage"
        messagebox.showinfo("Marriage","You both will get Married")
    elif flames=='e':
        result="Enemies"
        messagebox.showinfo("Enemies","You both are Enemies")
    else:
        result="Brother and Sister"
        messagebox.showinfo("Brothers & Sisters","You both will be brothers and sisters")
    res.set(result)
def neumerology():
    pass
label1=tk.Label(master=window,text="Enter your Name:").grid(row=0,column=0)
entry1=tk.Entry(master=window,textvariable=n1).grid(row=0,column=1)

label2=tk.Label(master=window,text="Enter your Partner's Name:").grid(row=1,column=0)
entry2=tk.Entry(master=window,textvariable=n2).grid(row=1,column=1)

button1=tk.Button(master=window,text="Match",command=match).grid(row=2,column=1)
label3=tk.Label(master=window,text="Numerology Result:").grid(row=3,column=0)
result_label=tk.Label(master=window,text="",textvariable=res).grid(row=3,column=1)


window.mainloop()
