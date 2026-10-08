from tkinter import Tk, Entry, Button, ttk, messagebox, Text

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
    



asd = Tk()
asd.title("Python Document Helper")
asd.resizable(False,False)
asd.geometry(f"800x390+{asd.winfo_screenwidth()//2-400}+{asd.winfo_screenheight()//2-195}")
asd.config(bg="gray")
value = Entry(asd)
value.pack()


Button(asd, text="Find", command=getInfo).pack()


data = ttk.Treeview(asd, columns=("Name",), show="headings", height=15)
data.pack( side = "left", fill="both",expand=True, pady=(10,5))
data.heading("Name", text = "Name", anchor = "w")

info = Text(asd, width=70)
info.pack(side="right", fill="both", pady=(10,5))
info.config(state="d")
asd.bind("<Return>", (lambda e: getInfo()))

data.bind("<ButtonRelease>", (lambda e: showInfo()))


value.focus()
asd.mainloop()
