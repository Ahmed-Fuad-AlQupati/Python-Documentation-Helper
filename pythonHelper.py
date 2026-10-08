from tkinter import Tk, Entry, Button, ttk, messagebox, Text, Frame

library = None


def getInfo():
    try:        
        exec(f"""import {value.get()} as lib
global library
library = lib""")        
        
        for i in data.get_children():
            data.delete(i)
        
        exec("""for i in dir(library):            
            data.insert("", "end", values = (i,))
            """)        
    
    except Exception as e:
        messagebox.showerror("Error", f"Make Sure To Write The Name Correct.!!!\n\n{e}")
    

def showInfo():    
    info.config(state="n")
    try:
        from io import StringIO
        import sys
    
        
        
        oldOutput = sys.stdout
        
        sys.stdout = helpText = StringIO()
        
        help(library.__getattribute__(data.item(data.selection())['values'][0]))
        
        showText = helpText.getvalue()
        
        sys.stdout = oldOutput
        
        #s = library.__getattribute__(data.item(data.selection())['values'][0]).__doc__
        
        
        info.delete("0.1","end")
        info.insert("end", showText)
    except Exception as e:
        messagebox.showerror("Error", f"There is Some Error in This Choice.!!!\n\n{e}")
        
    info.config(state="d")
    
def fontSizing(scaling:bool):        
    fontSize = int(info.cget("font").split()[1])    
    if(scaling and fontSize < 30):                
        fontSize += 1
        
    elif(not scaling and fontSize > 5):
        fontSize -= 1
    info.config(font = ("",fontSize,""))


asd = Tk()
asd.title("Python Document Helper")
asd.resizable(False,False)
asd.geometry(f"800x390+{asd.winfo_screenwidth()//2-400}+{asd.winfo_screenheight()//2-195}")
asd.config(bg="gray")

top = Frame(asd, bg = "gray")
top.pack(fill='both')

value = Entry(top)
value.pack()

Button(top, text="Find", command=getInfo).pack()

body = Frame(asd)
body.pack(expand=True, fill='both')

data = ttk.Treeview(body, columns=("Name",), show="headings", height=15)
data.pack( side = "left", fill="both")
data.heading("Name", text = "Name", anchor = "w")

info = Text(body, width=70, font=['',20,""])
info.pack(side="left", fill="both", expand=True)
info.config(state="d")


asd.bind("<Return>", (lambda e: getInfo()))


data.bind("<ButtonRelease>", (lambda e: showInfo()))


top.bind("<Control-MouseWheel>", (lambda e: fontSizing(True)if e.delta > 0 else fontSizing(False)))
asd.bind("<Control-]>", (lambda e: fontSizing(True)))
asd.bind("<Control-[>", (lambda e: fontSizing(False)))


value.focus()
asd.mainloop()
