from tkinter import *
import qrcode



app = Tk()
app.title("Code Generator")

app.geometry("1000x550")
app.config(bg="#1CBFFF")
app.resizable(False,False)

image_icon = PhotoImage(file="Uis.png")
app.iconphoto(False,image_icon)

def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("output/"+str(name)+".png")

    global Image
    Image = PhotoImage("output/"+str(name)+".png")
    I_view.config(image=Image)

I_view = Label(app,bg="#1CBFFF")
I_view.pack(padx=50,pady=10,side=RIGHT)

Label(app,text="Title",fg="white",bg="#1CBFFF",font=15).place(x=50,y=170)

title = Entry(app,width=13,font="arial 15")
title.place(x=50,y=200)

entry = Entry(app,width=28,font="arial 15")
entry.place(x=50,y=250)

Button(app,text="Generate",width=20,height=2,bg="black",fg="white",command=generate).place(x=50,y=300)


app.mainloop()
