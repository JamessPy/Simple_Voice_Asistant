from tkinter import *
from PIL import ImageTk ,Image
base = Tk()
base.title('Start Button')

img=ImageTk.PhotoImage(Image.open ("download.jpg"))
lab=Label(image=img)
lab.pack()

button=Button(base,text='start',command=base.quit)
button.pack()
base.mainloop()

import Recognition2
