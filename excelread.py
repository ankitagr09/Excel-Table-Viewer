import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if filepath:
        df = pd.read_excel(filepath)
        create_table(df)

def create_table(dataframe):
    top = tk.Toplevel(root)
    table = tk.Frame(top)
    table.pack()

    # Create table headers
    headers = dataframe.columns
    for col_index, header in enumerate(headers):
        label = tk.Label(table, text=header, relief=tk.RIDGE, width=20)
        label.grid(row=0, column=col_index, sticky=tk.W)

    # Populate table with data
    for row_index, row in dataframe.iterrows():
        for col_index, value in enumerate(row):
            label = tk.Label(table, text=str(value), relief=tk.RIDGE, width=20)
            label.grid(row=row_index+1, column=col_index, sticky=tk.W)

# Create the main window
root = tk.Tk()
root.title("Excel Table Viewer")

# Create Open File button
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

root.mainloop()
