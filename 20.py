import tkinter as tk
from tkinter import messagebox

def submit_test():
    if not name_entry.get() or not group_entry.get():
        warning_label.config(text="Будь ласка, введіть прізвище та групу!", fg="red")
        return
    
    score = 0
    if question1_var.get() == "A": score += 1
    if question2_var_python.get() and question2_var_java.get(): score += 1
    if question3_entry.get().lower() == "html": score += 1
    if question4_var.get() == "B": score += 1
    if question5_var.get() == "42": score += 1
    if question6_var_python.get(): score += 1
    if question7_entry.get().lower() == "google": score += 1
    if question8_var.get() == "A": score += 1
    if question9_entry.get().lower() == "earth": score += 1
    if question10_var.get() == "C": score += 1
    
    messagebox.showinfo("Результат", f"Користувач {name_entry.get()} ({group_entry.get()}) набрав {score} балів")

def clear_answers():
    name_entry.delete(0, tk.END)
    group_entry.delete(0, tk.END)
    question1_var.set(None)
    question2_var_python.set(False)
    question2_var_java.set(False)
    question3_entry.delete(0, tk.END)
    question4_var.set(None)
    question5_var.set("")
    question6_var_python.set(False)
    question7_entry.delete(0, tk.END)
    question8_var.set(None)
    question9_entry.delete(0, tk.END)
    question10_var.set(None)

root = tk.Tk()
root.title("Matsiuk_20_knit23")
root.geometry("500x600")

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.config(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

frame1 = tk.Frame(scrollable_frame)
frame1.pack(pady=10)

tk.Label(frame1, text="Прізвище:").grid(row=0, column=0, padx=10)
name_entry = tk.Entry(frame1)
name_entry.grid(row=0, column=1)

tk.Label(frame1, text="Група:").grid(row=1, column=0, padx=10)
group_entry = tk.Entry(frame1)
group_entry.grid(row=1, column=1)

warning_label = tk.Label(frame1, text="", fg="red")
warning_label.grid(row=2, column=0, columnspan=2)

frame2 = tk.Frame(scrollable_frame)
frame2.pack(pady=10)

question1_var = tk.StringVar(value=None)
tk.Label(frame2, text="1. Яка мова програмування є основною для тесту?").pack(anchor="w")
tk.Radiobutton(frame2, text="Python", variable=question1_var, value="A").pack(anchor="w")
tk.Radiobutton(frame2, text="C++", variable=question1_var, value="B").pack(anchor="w")

question2_var_python = tk.BooleanVar()
question2_var_java = tk.BooleanVar()
tk.Label(frame2, text="2. Які з наступних мов є популярними для програмування?").pack(anchor="w")
tk.Checkbutton(frame2, text="Python", variable=question2_var_python).pack(anchor="w")
tk.Checkbutton(frame2, text="Java", variable=question2_var_java).pack(anchor="w")

tk.Label(frame2, text="3. Яка мова використовується для створення сайтів?").pack(anchor="w")
question3_entry = tk.Entry(frame2)
question3_entry.pack(anchor="w")

question4_var = tk.StringVar(value=None)
tk.Label(frame2, text="4. Що таке GitHub?").pack(anchor="w")
tk.Radiobutton(frame2, text="Ігрова платформа", variable=question4_var, value="A").pack(anchor="w")
tk.Radiobutton(frame2, text="Платформа для розробників", variable=question4_var, value="B").pack(anchor="w")

question5_var = tk.StringVar()
tk.Label(frame2, text="5. Яка відповідь на питання життя, Всесвіту і всього такого?").pack(anchor="w")
question5_entry = tk.Entry(frame2, textvariable=question5_var)
question5_entry.pack(anchor="w")

question6_var_python = tk.BooleanVar()
tk.Label(frame2, text="6. Чи є Python мультипарадигмовою мовою?").pack(anchor="w")
tk.Checkbutton(frame2, text="Так", variable=question6_var_python).pack(anchor="w")

tk.Label(frame2, text="7. Яка пошукова система є найпопулярнішою?").pack(anchor="w")
question7_entry = tk.Entry(frame2)
question7_entry.pack(anchor="w")

question8_var = tk.StringVar(value=None)
tk.Label(frame2, text="8. Який логотип має компанія Apple?").pack(anchor="w")
tk.Radiobutton(frame2, text="Яблуко", variable=question8_var, value="A").pack(anchor="w")
tk.Radiobutton(frame2, text="Помаранч", variable=question8_var, value="B").pack(anchor="w")

tk.Label(frame2, text="9. На якій планеті ми живемо?").pack(anchor="w")
question9_entry = tk.Entry(frame2)
question9_entry.pack(anchor="w")

question10_var = tk.StringVar(value=None)
tk.Label(frame2, text="10. Що таке AI?").pack(anchor="w")
tk.Radiobutton(frame2, text="Людський інтелект", variable=question10_var, value="A").pack(anchor="w")
tk.Radiobutton(frame2, text="Автоматичний інтелект", variable=question10_var, value="B").pack(anchor="w")
tk.Radiobutton(frame2, text="Штучний інтелект", variable=question10_var, value="C").pack(anchor="w")

# Кнопки
frame3 = tk.Frame(scrollable_frame)
frame3.pack(pady=10)

submit_button = tk.Button(frame3, text="Надіслати результат", command=submit_test)
submit_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(frame3, text="Очистити відповіді", command=clear_answers)
clear_button.grid(row=0, column=1, padx=10)

root.mainloop()