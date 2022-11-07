

import rsa
import tkinter as tk

from tkinter import END, filedialog as fd
from tkinter import messagebox
root = tk.Tk()
root.geometry("300x350")
root.title("Engine Serializer")
root.resizable(False, False)



key_in = tk.Text(root, height = 0.5, width = 17, font = ('Arial',10))
key_in.place(x=100,y=15)
key_label = tk.Label(root, width = 10, height = 2, text="Insert Key:")
key_label.place(x=10,y=7)


key_out_text = tk.StringVar()
key_out = tk.Text(root)
key_out = tk.Entry(root, textvariable= key_out_text)
key_out.place(x=100,y=50)
eng_label = tk.Label(root, width = 10, height = 2, text="Engine Code:")
eng_label.place(x=10,y=42)



def select_file():
    try:
     global keydata
     filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
     )
     file = fd.askopenfile(mode = 'rb',
     filetypes= filetypes)
     keydata = file.read()
     key_out_text.set(keydata)
    except:
     messagebox.showinfo("Engine Code", "You did not select engine code file")


def ser_key():
    try:
     engine_key = key_in.get("1.0", "end-1c")
     x=[int (item) for item in engine_key.split(',')]
    
     priv_ky = rsa.PrivateKey(x[0], x[1], x[2], x[3], x[4])
    
     with open("private.pem", "wb") as f:
      f.write(priv_ky.save_pkcs1("PEM"))
     with open("private.pem", "rb") as f:
      priv_ky = rsa.PrivateKey.load_pkcs1(f.read())
    except:
     messagebox.showerror("Key Error", "Error on saving and loading key, make sure you have the right format.")
    try:
     engine_ser = rsa.decrypt(keydata, priv_ky)
     print(engine_ser)
     key_out_text.set(engine_ser.decode())
    except:
     messagebox.showerror("Serialization Error", "Engine key and engine code do not match")




select_text=tk.StringVar()
select_btn = tk.Button(root, textvariable=select_text,
command = select_file, font = "Arial", bg="gray", fg = "white", height = 1, width = 15)
select_text.set("Select File")
select_btn.place(x = 80, y=100)

gen_text=tk.StringVar()
gen_btn = tk.Button(root, textvariable=gen_text,
command = ser_key, font = "Arial", bg="gray", fg = "white", height = 1, width = 15)
gen_text.set("Serialize")
gen_btn.place(x = 80, y=140)


root.mainloop()
