'''
A CLI based Screenshot application on Python.
1) Need to install virtualenv; it's for creating a virtual environment where
    all external dependencies would be installed for a separate project.
 "pip install virtualenv"
 virtualenv not woking so proceeding with mamba

2) Create a virtual environment (projects_env)
    > Install pyautogui
'''
import time
import pyautogui
import tkinter as tk

def screenshot():
    #Adding a 5 second delay so that execution doesn't occour immediately.
    #Disabled for GUI mode.
    # time.sleep(5)

    #Screenshot file name generation.
    # --  --  --  --  --  --  --
    # Retrieve the current local time as a struct_time object, which represents the time broken down into its various components.
    date_time = time.localtime()

    # Format a struct_time object or a time tuple into a string representation based on a specified format.
    date_time = time.strftime("%m_%d_%Y_%H_%M_%S", date_time)
    
    ss_name = "SS"+date_time+".png"
    # --  --  --  --  --  --  --

    #minimize app before capture and delay 1sec
    root.iconify()
    time.sleep(1)

    #screenshot function allows you to capture screenshots of your computer screen programmatically.
    #Captures the entire screen by default.
    ss = pyautogui.screenshot(ss_name)

    ss.show()

    #restore minimized window app.
    root.deiconify()


root = tk.Tk()
root.title("SS App")
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Screenshot",
    command = screenshot
)
button.pack(side = tk.LEFT)

close = tk.Button(
    frame,
    text = "Quit",
    command = quit
)
close.pack(side = tk.LEFT)

root.mainloop()