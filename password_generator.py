import tkinter as tk
from tkinter import *
import numpy as np
import argparse
import random
import string


def generate_password(length_password=15, upper=False, symbols=True, numbers=True):
    # first check the type of the length parameter
    password = []
    
    if type(length_password) is not int or length_password <= 0: 
        listToStr = "chech the length parameter"
    else:
        if upper and symbols and numbers:
            password_list = string.ascii_letters + string.punctuation + string.digits
        
        elif upper and symbols and not numbers:
            password_list = string.ascii_letters + string.punctuation
        
        elif upper and not symbols and numbers:
            password_list = string.ascii_letters + string.digits
        
        elif not upper and symbols and numbers:
            password_list = string.ascii_lowercase + string.digits
        
        elif upper and not symbols and not numbers:
            password_list = string.ascii_letters
        
        elif not upper and symbols and not numbers:
            password_list = string.ascii_lowercase + string.punctuation
        
        elif not upper and not symbols and numbers:
            password_list = string.ascii_lowercase + string.digits
        
        elif not upper and not symbols and not numbers:
            password_list = string.ascii_lowercase
        
        for _ in range(length_password):
            password.append(random.choice(password_list))
            listToStr = ''.join([str(elem) for elem in password]) 
    # print('length', length_password)
    # print('upper', upper)
    # print('symbols', symbols)
    # print('numbers', numbers)
    print(listToStr)
    return listToStr


root = tk.Tk()
# length_password

e_length = Entry(root, width=50)
e_length.pack()

# upper
var_upper = tk.IntVar()
c_upper = tk.Checkbutton(root, text="Upper case letters?", variable=var_upper)
c_upper.pack()
c_upper_value = var_upper.get()
# symbols
var_symbols = tk.IntVar()
c_symbols = tk.Checkbutton(root, text="Symbols?", variable=var_symbols)
c_symbols.pack()
c_symbols_value = var_symbols.get()
# numbers
var_numbers = tk.IntVar()
c_numbers = tk.Checkbutton(root, text="Numbers?", variable=var_numbers)
c_numbers.pack()
c_numbers_value = var_numbers.get()
# length_password, upper, symbols, numbers
genButton = Button(root, text="Generate password.", padx=40, pady=20, command=lambda: generate_password(int(e_length.get()), var_upper.get(), var_symbols.get(), var_numbers.get()))
genButton.pack()

root.mainloop()