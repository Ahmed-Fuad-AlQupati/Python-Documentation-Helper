from tkinter import Tk, Entry, Button, ttk, messagebox

def getInfo():
    try:        
        exec(f"import {value.get()} as library")
        exec("""for i in dir(library):            
            data.insert("", "end", values = (i, library.__getattribute__(i).__doc__))
            """)        
    
    except Exception as e:
        messagebox.showerror("Error", f"Make Sure To Write The Name Correct.!!!\n\n{e}")
    

asd = Tk()
asd.title("Python Document Helper")
asd.resizable(False,False)
asd.geometry(f"800x390+{asd.winfo_screenwidth()//2-400}+{asd.winfo_screenheight()//2-195}")
asd.config(bg="gray")
value = Entry(asd)
value.pack()


Button(asd, text="Find", command=getInfo).pack()

data = ttk.Treeview(asd, columns=("Name", "Help",), show="headings", height=15)
data.column("Name", width = 1)
data.pack( fill="both", pady=(10,5))
data.heading("Name", text = "Name", anchor = "w")
data.heading("Help", text = "Help Doc", anchor = "w")

asd.bind("<Return>", (lambda e: getInfo()))

value.focus()
asd.mainloop()




#import random

#a = random.__getattribute__("_log").__doc__

#print(a)
#print(a)
