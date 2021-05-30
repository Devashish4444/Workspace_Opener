import tkinter as tk 
from tkinter import filedialog, Text #file dialogue helps us pick up the app or file
import os

root = tk.Tk() # created an instance for tkinter

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)



def addApps():# This function is for openfile button to execute, open up file dir that we clicked and save for us.

    for element in frame.winfo_children(): # to clear the frame before we add the second app.
        element.destroy()

    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File", 
    filetypes = (("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text= app, bg= "grey" )
        label.pack()

def runApps(): # So that runApp button can run the files that we have on the window frame.
    for app in apps:
        os.startfile(app)


#To increase the size of the window we have created a canvas
canvas = tk.Canvas(root, height = 500, width = 500, bg = "#263D42") 
canvas.pack()

#In the canvas we will place a frame
frame = tk.Frame(root, bg= "white")
frame.place(relwidth = 0.8, relheight= 0.8, relx = 0.1, rely = 0.1)

#Now we have to add the button, we first add the button to open the apps
openFile = tk.Button(root, text = "Open File", padx =10, pady =5, fg= "white", bg = "#263D42", command= addApps )
openFile.pack()

#Now  we add the button to Run the apps
runApps = tk.Button(root, text = "Run Apps", padx =10, pady =5, fg= "white", bg = "#263D42", command = runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text= app)
    label.pack()

    
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')