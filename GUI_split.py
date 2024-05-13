import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import PyPDF2

def split_pdf(input_path, output_path, start_page, end_page):
    with open(input_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        num_pages = len(pdf_reader.pages)
        if start_page < 1 or end_page > num_pages or start_page > end_page:
            messagebox.showerror("Error", f"Invalid page range for {os.path.basename(input_path)}.")
            return

        for page_num in range(start_page - 1, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
        
        messagebox.showinfo("Success", f"PDF file {os.path.basename(input_path)} has been split successfully.")

def select_input_directory():
    input_dir = filedialog.askdirectory()
    input_directory_var.set(input_dir)

def select_output_directory():
    output_dir = filedialog.askdirectory()
    output_directory_var.set(output_dir)

def split_pdf_files():
    input_dir = input_directory_var.get()
    output_dir = output_directory_var.get()
    start_page = int(start_page_var.get())
    end_page = int(end_page_var.get())
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            input_file_path = os.path.join(input_dir, filename)
            output_file_name = f"{os.path.splitext(filename)[0]}_split.pdf"
            output_file_path = os.path.join(output_dir, output_file_name)
            split_pdf(input_file_path, output_file_path, start_page, end_page)

# Create main window
root = tk.Tk()
root.title("PDF Splitter")

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

# Start page
start_page_var = tk.StringVar()
tk.Label(root, text="Start Page:").grid(row=2, column=0, padx=5, pady=5)
start_page_entry = tk.Entry(root, textvariable=start_page_var, width=10)
start_page_entry.grid(row=2, column=1, padx=5, pady=5)

# End page
end_page_var = tk.StringVar()
tk.Label(root, text="End Page:").grid(row=3, column=0, padx=5, pady=5)
end_page_entry = tk.Entry(root, textvariable=end_page_var, width=10)
end_page_entry.grid(row=3, column=1, padx=5, pady=5)

# Split button
split_button = tk.Button(root, text="Split PDF Files", command=split_pdf_files)
split_button.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
