def login():
    username=entry21.get()
    password=entry22.get()
    


    if (username=="" or password==''):
        messagebox.showinfo('error','Enter your username and password')



    

               
    else:
        messagebox.showerror('error','Enter your correct username and password')