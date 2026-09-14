import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("mini-paint")
        self.root.geometry("800x600")
        
        self.current_color = "black"
        self.fill_color = "white"
        self.shape = "rectangle"
        self.start_x = None
        self.start_y = None
        self.current_shape_id = None
        self.is_brush = False
        
        self.create_menu()
        
        self.canvas = tk.Canvas(self.root, bg="white", width=780, height=500)
        self.canvas.pack(pady=10)
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.finish_draw)
        
        self.create_toolbar()
        
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Відкрити...", command=self.open_file)
        file_menu.add_command(label="Зберегти як...", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Вийти", command=self.root.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        
        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="Про програму", command=self.show_about)
        menu_bar.add_cascade(label="Допомога", menu=about_menu)
    
    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bg="lightgrey")
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        shapes = [("Прямокутник", "rectangle"), ("Овал", "oval"), ("Лінія", "line")]
        for text, shape in shapes:
            btn = tk.Button(toolbar, text=text, command=lambda s=shape: self.set_shape(s))
            btn.pack(side=tk.LEFT, padx=5)
        
        tk.Button(toolbar, text="Пензлик", command=self.set_brush).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar, text="Колір контуру", command=self.choose_outline_color).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar, text="Колір заливки", command=self.choose_fill_color).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar, text="Очистити все", command=self.clear_canvas).pack(side=tk.LEFT, padx=5)
    
    def set_shape(self, shape):
        self.shape = shape
        self.is_brush = False
    
    def set_brush(self):
        self.is_brush = True
    
    def choose_outline_color(self):
        color = colorchooser.askcolor(title="Виберіть колір контуру")[1]
        if color:
            self.current_color = color
    
    def choose_fill_color(self):
        color = colorchooser.askcolor(title="Виберіть колір заливки")[1]
        if color:
            self.fill_color = color
    
    def clear_canvas(self):
        self.canvas.delete("all")
    
    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.is_brush:
            self.canvas.create_line(event.x, event.y, event.x + 1, event.y + 1, fill=self.current_color, width=3)
    
    def draw(self, event):
        if self.is_brush:
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.current_color, width=3)
            self.start_x = event.x
            self.start_y = event.y
        else:
            if self.current_shape_id:
                self.canvas.delete(self.current_shape_id)
            if self.shape == "rectangle":
                self.current_shape_id = self.canvas.create_rectangle(
                    self.start_x, self.start_y, event.x, event.y,
                    outline=self.current_color, fill=self.fill_color)
            elif self.shape == "oval":
                self.current_shape_id = self.canvas.create_oval(
                    self.start_x, self.start_y, event.x, event.y,
                    outline=self.current_color, fill=self.fill_color)
            elif self.shape == "line":
                self.current_shape_id = self.canvas.create_line(
                    self.start_x, self.start_y, event.x, event.y,
                    fill=self.current_color, width=2)
    
    def finish_draw(self, event):
        if not self.is_brush:
            self.current_shape_id = None
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Файли зображень", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.show_custom_message("Неможливо відкрити", "red")
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG файли", "*.png")])
        if file_path:
            self.show_custom_message("Збереження не можливе.", "orange")
    
    def show_about(self):
        self.show_custom_message("Малювалка\nРозробник: Мацюк\nДата: 2024", "green")
    
    def show_custom_message(self, message, color):
        msg_window = tk.Toplevel(self.root)
        msg_window.title("Повідомлення")
        msg_window.geometry("300x100")
        msg_window.configure(bg=color)
        
        tk.Label(msg_window, text=message, bg=color, fg="white", font=("Arial", 12)).pack(expand=True, padx=10, pady=10)
        tk.Button(msg_window, text="OK", command=msg_window.destroy).pack(pady=5)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()