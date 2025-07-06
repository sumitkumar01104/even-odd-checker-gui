"""
Even/Odd Checker GUI using Tkinter
Created by: Sumit Nagar
Description: This simple Python app takes a number input from the user
and checks whether it's even or odd using a GUI interface.
"""
# import tkinter library:-
import tkinter as tk  

# Function to check a number is even or odd:-
def check_even_odd():
    
    try:
        number = int(entry.get())
        if number %2==0:
            label_result.config(text=f"{number} is an even number",fg="green")
            
            
            
        else:
            label_result.config(text=f"{number} is an odd number", fg="red")
        entry.delete(0,tk.END)
    except ValueError:
         label_result.config(text="Please enter a valid number", fg="red")

# Function to reset the entry and result label:-       
def reset():
    entry.delete(0,tk.END)
    label_result.config(text="")

# create a display window:-  
window = tk.Tk()
window.title("Even/Odd Checker")
window.geometry("300x400")

# label and entry for number input
label =tk.Label(window,text="Enter a number:-",font=("Sitka Heading",16,"bold"))
label.pack()
entry = tk.Entry(window)
entry.pack(pady=5)
entry.focus() # set focus on entry field
frame = tk.Frame(window)
frame.pack()

# create button to check even or odd number:-
button_check = tk.Button(frame,text="Check",command=check_even_odd,font=("Imprint MT Shadow",14),fg="blue",bg="white")
button_check.pack(pady =5 ,padx=5,side ="left" )

# reset button to clear the entry and result label:-
button_reset = tk.Button(frame,text="Reset",command=reset,font=("Imprint MT Shadow",14),fg="black",bg="white")
button_reset.pack(pady =5, side="left" )

#label to display result:-
label_result =tk.Label(window,text="",font=("Imprint MT Shadow",16))
label_result.pack()
# Start the GUI event loop
window.mainloop()
