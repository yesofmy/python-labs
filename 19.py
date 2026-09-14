from tkinter import *

root = Tk()
root.title("Анкета")
root.geometry("400x500")
root.iconbitmap("C:/other files and games/Programs/codes/icon.png")

root.configure(bg='lightblue')

a = Label(root, text="Анкета", font=("Arial", 16, "bold"))
a.pack(pady=10)

first_name = Label(root, text="Введіть ваше ім’я")
first_name.pack()
first_name_entry = Entry(root)
first_name_entry.pack(pady=5)

second_name = Label(root, text="Введіть ваше прізвище")
second_name.pack()
second_name_entry = Entry(root)
second_name_entry.pack(pady=5)

sex_male = BooleanVar()
sex_female = BooleanVar()

male = Checkbutton(root, text="чол", variable=sex_male)
male.pack(side=LEFT, padx=10, pady=5)
female = Checkbutton(root, text="жін", variable=sex_female)
female.pack(side=LEFT, padx=10, pady=5)

def ff(event):
    a.config(bg="red")

light = Button(root, text="Підсвітити заголовок")
light.pack(pady=5)
light.bind("<Button-1>", ff)

def ff_del(event):
    first_name_entry.delete(0, END)
    second_name_entry.delete(0, END)
    first_name_entry.insert(0, "Петро")
    second_name_entry.insert(0, "Петренко")
    sex_male.set(True)

by_default = Button(root, text="За замовчуванням")
by_default.pack(pady=5)
by_default.bind("<Button-1>", ff_del)

note_text = Text(root, height=6, width=40)
note_text.pack(pady=10)

def ff_data(event):
    note_text.delete(1.0, END)
    note_text.insert(1.0, first_name_entry.get())
    note_text.insert(2.0, "\n" + second_name_entry.get())

    if sex_male.get():
        note_text.insert(3.0, "\nХлопець")
    elif sex_female.get():
        note_text.insert(3.0, "\nДівчина")

    note_text.insert(4.0, "\nНавчається у %s класі" % grade.get())

data_button = Button(root, text="Дані")
data_button.pack(pady=5)
data_button.bind("<Button-1>", ff_data)

grade = IntVar()
grade.set(1)

for i in range(1, 12):
    Radiobutton(root, text=f"{i}", variable=grade, value=i).pack()

root.mainloop()