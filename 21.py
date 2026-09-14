import tkinter as tk
from tkinter import filedialog, messagebox
import datetime

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Новий документ - Блокнот")

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        with open(file, "r") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())
        root.title(f"{file} - Блокнот")

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))
        root.title(f"{file} - Блокнот")

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(text_area.get(tk.SEL_FIRST, tk.SEL_LAST))

def paste_text():
    text_area.insert(tk.INSERT, root.clipboard_get())

def delete_text():
    text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

def about_program():
    messagebox.showinfo("Про програму", "Блокнот розроблений: Мацюк")

def highlight_keywords():
    keywords = ['Python', 'Tkinter', 'blockchain']
    text_content = text_area.get(1.0, tk.END)
    for keyword in keywords:
        start_idx = 1.0
        while True:
            start_idx = text_content.find(keyword, start_idx)
            if start_idx == -1:
                break
            end_idx = start_idx + len(keyword)
            text_area.tag_add(keyword, f"1.0 + {start_idx} chars", f"1.0 + {end_idx} chars")
            text_area.tag_configure(keyword, foreground="red", font=("Arial", 10, "bold"))
            start_idx = end_idx

root = tk.Tk()
root.title("Блокнот - Новий документ")
root.geometry("600x400")

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новий", command=new_file)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вихід", command=root.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Редагувати", menu=edit_menu)
edit_menu.add_command(label="Копіювати", command=copy_text)
edit_menu.add_command(label="Вставити", command=paste_text)
edit_menu.add_command(label="Видалити", command=delete_text)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Допомога", menu=help_menu)
help_menu.add_command(label="Про програму", command=about_program)

highlight_button = tk.Button(root, text="Підсвітити ключові слова", command=highlight_keywords)
highlight_button.pack(pady=10)

root.mainloop()