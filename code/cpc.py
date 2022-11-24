# E M Petersen
# 15/09/2022

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * # import the tkinter library

def button_press(num):   # defining each button press
    global equation_text
    
    equation_text = equation_text + str(num)
    
    equation_label.set(equation_text)

def equals():    # this block checks for the button_press(equals)
    
    global equation_text
    
    try:  #  try is used in try...except blocks. It defines a block of code test if it contains any errors.
          #  You can define different blocks for different error types, and blocks to execute if nothing went wrong.
        total = str(eval(equation_text))  # parses the expression arguement and evaluates it as a python expression.
        
        equation_label.set(total)   #   
        
        equation_text = total
        
    except SyntaxError:  # Check for syntax error
        
        equation_label.set("syntax error")
        
        equation_text = ""
        
    except ZeroDivisionError:  #  Check for division by zero
        
        equation_label.set("arithmetic error")
        
        equation_text = ""

def clear():  #  Clears the equation_label for the next calculation
    global equation_text
    
    equation_label.set("")
    
    equation_text = ""




# Designing the user interface

window = Tk()  #  you can use window, root, ... or a descriptive variable of your own
window.title("Python Calculator")  #  Title in the window bar




window.geometry("500x500")   #  size of the window dependent on your design
window.configure(bg="#5176f0")  #  window colour dependent on your design

equation_text = ""  #  starting off with no text in the label 

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 18), bg="#5176f0", width=25, height=2)
label.pack()  #  widgets have to be "pack"ed into the window

frame = Frame(window)
frame.pack()  #  the frame is a widget that is "pack"ed into the window

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

# create operation buttons

plus = Button(frame, text='PLUS', height=14, width=9, font=35, bg="#c4918d", command=lambda: button_press('+'))
plus.grid(row=0, column=3, rowspan=3)



# create equals button

equal = Button(frame, text='Equals', height=4, width=30, font=35, bg="#e69a95", command=equals)
equal.grid(row=3, column=1, columnspan=3)



# create clear button

clear = Button(window, text='New Sum', bg="#e3e032", height=4, width=12, font=35, command=clear)
clear.pack()


window.mainloop()

