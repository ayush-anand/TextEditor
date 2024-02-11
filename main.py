import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
def saveFn(window, text_edit):
    filename = asksaveasfilename(filetypes=[("Text file", "*.txt")])
    if not filename:
        return
    with open (filename,"w") as f:
        content= text_edit.get(1.0, tk.END)
        f.write(content)
    pass


def openFn(window, text_edit):
    filename = askopenfilename(filetypes=[("Text file", "*.txt")])
    if not filename:
        return
    #clearing current editor , 1.0 -> line=1 char=0 till END
    text_edit.delete(1.0, tk.END)
    with open (filename, "r") as f:
        content=f.read()
        text_edit.insert(tk.END, content)
    window.title(filename)
    pass


def main():
    window = tk.Tk();
    window.title("Text Editor")
    window.rowconfigure(0,minsize=400)
    window.columnconfigure(1,minsize=400)
    #creating a text editor window , parent='window'
    text_edit = tk.Text(window, font="Helvetica 16")
    #tkinter uses grid system starting from (0,0) = top left
    #column = 1 as want button on left
    text_edit.grid(row=0,column=1)
    #to set the size of the component we need to set the size of the cell line 6
    
    ##now creating buttoms we first need a frame
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    #sticky sticks comp to certian side ns = north to south = strect vertically
    frame.grid(row=0,column=0,sticky="ns")

    #since command take only functionname as the paramter we creates a lambda n gave pram there
    saveButton = tk.Button(frame,text="Save", command=lambda : saveFn(window=window, text_edit=text_edit))
    saveButton.grid(row=0,column=0,sticky="ew")

    openButton = tk.Button(frame,text="Open",command=lambda : openFn(window=window, text_edit=text_edit))
    openButton.grid(row=1,column=0,sticky="ew")

    #TO MAKE ctrl+s TO SAVE, x as this function passes a argumnet to handle that
    window.bind("<Control-s>",lambda x : saveFn(window=window, text_edit=text_edit))
    window.bind("<Control-o>",lambda x : openFn(window=window, text_edit=text_edit))
    window.mainloop()
main()

