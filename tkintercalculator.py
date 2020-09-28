from tkinter import *
root = Tk()
root.configure(bg='white')
root.geometry("720x1232+0+0")
lst = []
text = Label(root,text="Welcome !",height=5,bd=6,width=40,bg="silver")
text.place(y=70,x=10)
#functions--------------------------------------------------------------------------------------------
    
def ac():
    lst.clear()
    text = Label(root,text=str("".join(lst)),height=5,bd=6,width=40,bg="silver")
    text.place(y=70,x=10)
    
def delet():
    lst.pop()
    re = str("".join(lst))
    text = Label(root,text=re,height=5,bd=6,width=40,bg="silver")
    text.place(y=70,x=10)

def equals():
    try:
        re = str(eval("".join(lst)))
        text = Label(root,text=re,height=5,bd=6,width=40,bg="silver")
        text.place(y=70,x=10)
    except:
        text = Label(root,text="invalid syntex an error ocured",height=5,bd=6,width=40,bg="silver")
        text.place(y=70,x=10)
    lst.clear()
    lst.append(re)

def cal(x):
    lst.append(x)
    text = Label(root,text="".join(lst),height=5,bd=6,width=40,bg="silver")
    text.place(y=70,x=10)
    
#----------------------------------------------------------------------------------------------------------

#color codes-----------------------------------------------------------------------------------------
o = "orange"
sb = "skyblue"
lg = "lightgreen"
pk = "pink"
#----------------------------------------------------------------------------------------------------------

#button code----------------------------------------------------------------------------------------
Button(root,command = lambda: cal("**"),bg="red",text="POW",height=3,width=5).place(x=10,y=300)
Button(root,command = delet,bg=o,text="DEL",height=3,width=5).place(x=190,y=300)
Button(root,command = ac,bg=o,text="AC",height=3,width=5).place(x=370,y=300)
Button(root,command = lambda: cal("%"),bg=sb,text="%",height=3,width=5).place(x=550,y=300)


Button(root,command = lambda: cal("7"),bg=lg,text="7",height=3,width=5).place(x=10,y=490)
Button(root,command = lambda: cal("8") ,bg=lg,text="8",height=3,width=5).place(x=190,y=490)
Button(root,command = lambda: cal("9"),bg=lg,text="9",height=3,width=5).place(x=370,y=490)
Button(root,command = lambda: cal("+"),bg=sb,text="+",height=3,width=5).place(x=550,y=490)

Button(root,command = lambda: cal("4"),bg=lg,text="4",height=3,width=5).place(x=10,y=680)
Button(root,command = lambda: cal("5"),bg=lg,text="5",height=3,width=5).place(x=190,y=680)
Button(root,command = lambda: cal("6"),bg=lg,text="6",height=3,width=5).place(x=370,y=680)
Button(root,command = lambda: cal("*"),bg=sb,text="×",height=3,width=5).place(x=550,y=680)

Button(root,command = lambda: cal("1"),bg=lg,text="1",height=3,width=5).place(x=10,y=870)
Button(root,command = lambda: cal("2"),bg=lg,text="2",height=3,width=5).place(x=190,y=870)
Button(root,command = lambda: cal("3"),bg=lg,text="3",height=3,width=5).place(x=370,y=870)
Button(root,command = lambda: cal("-"),bg=sb,text="–",height=3,width=5).place(x=550,y=870)

Button(root,command = lambda: cal("."),bg=pk,text="•",height=3,width=5).place(x=10,y=1060)
Button(root,command = lambda: cal("0"),bg=lg,text="0",height=3,width=5).place(x=190,y=1060)
Button(root,command = equals,bg=pk,text="=",height=3,width=5).place(x=370,y=1060)
Button(root,command = lambda: cal("/"),bg=sb,text="÷",height=3,width=5).place(x=550,y=1060)
#----------------------------------------------------------------------------------------------------------
root.mainloop()