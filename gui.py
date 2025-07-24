import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import subprocess
import json

def run_program():
    date = cal.get_date().strftime("20%y-%m-%d")
    location = combo_location.get()
    data_type = combo_data_type.get()
    anomalie = spin_window.get()

    with open('config.json') as f:
        config = json.load(f)
    
    

    cmd = ['python3', 'main.py', date, location, data_type, anomalie]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Program output:")
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
    except Exception as e:
        print(f"Błąd podczas uruchamiania programu: {e}")

    date = cal.get_date().strftime("20%y-%m-%d")
    location = combo_location.get()
    data_type = combo_data_type.get()

    cmd = ['python3', 'main.py', date, location, data_type]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Program output:")
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
    except Exception as e:
        print(f"Błąd podczas uruchamiania programu: {e}")

root = tk.Tk()
root.title("GUI for ambient data")


tk.Label(root, text="Data:").grid(row=0, column=0, sticky="e")
cal = DateEntry(root, date_pattern='yy-mm-dd')
cal.grid(row=0, column=1)

with open('config.json') as f:
        config = json.load(f)
locList = list(config["fit"].keys())


tk.Label(root, text="Lokalizacja:").grid(row=1, column=0, sticky="e")
combo_location = ttk.Combobox(root, values=locList)
combo_location.grid(row=1, column=1)
combo_location.current(0) 


tk.Label(root, text="Typ danych:").grid(row=2, column=0, sticky="e")
combo_data_type = ttk.Combobox(root, values=config["options"])
combo_data_type.grid(row=2, column=1)
combo_data_type.current(0)

tk.Label(root, text="TempAnomaly").grid(row=3, column=0, sticky="e")
spin_window = tk.Spinbox(root, from_=1, to=100, width=5, value= 29)
spin_window.grid(row=3, column=1)

btn_run = tk.Button(root, text="PlotGraph", command=run_program)
btn_run.grid(row=4, column=0, columnspan=2, pady=10)

import tkinter.messagebox as mb

def show_info():
    mb.showinfo("?", "auth: FK")

btn_info = tk.Button(root, text="?", command=show_info)
btn_info.grid(row=4, column=2, padx=10)

root.mainloop()
