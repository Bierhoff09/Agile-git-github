import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2

def merge_pdfs_in_folder(folder_path, output_path):
    merger = PyPDF2.PdfMerger()
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            merger.append(pdf_path)
            
    try:
        with open(output_path + '/bierhoff.pdf', 'wb') as output_file:
            merger.write(output_file)
        messagebox.showinfo("Success", "PDF files merged successfully.")
    except PermissionError:
        messagebox.showerror("Error", f"Permission denied: Unable to write to {output_path}")
    finally:
        merger.close()

def select_input_directory():
    input_dir = filedialog.askdirectory()
    input_directory_var.set(input_dir)

def select_output_directory():
    output_dir = filedialog.askdirectory()
    output_directory_var.set(output_dir)

def merge_pdfs():
    input_dir = input_directory_var.get()
    output_file = output_directory_var.get()
    merge_pdfs_in_folder(input_dir, output_file)

# Create main window
root = tk.Tk()
root.title("PDF Merger")

# Input directory
input_directory_var = tk.StringVar()
tk.Label(root, text="Input Directory:").grid(row=0, column=0, padx=5, pady=5)
input_directory_entry = tk.Entry(root, textvariable=input_directory_var, width=50)
input_directory_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_input_directory).grid(row=0, column=2, padx=5, pady=5)

# Output directory
output_directory_var = tk.StringVar()
tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=5, pady=5)
output_directory_entry = tk.Entry(root, textvariable=output_directory_var, width=50)
output_directory_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_output_directory).grid(row=1, column=2, padx=5, pady=5)

# Merge button
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()