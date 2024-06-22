import tkinter as tk
from tkinter import Canvas, PhotoImage, messagebox, simpledialog, ttk
from time import sleep
import pygame
import json
import os

TITLE = "MindBlowing"
WIDTH, HEIGHT = 240, 180
UserInfo_list = [0, 0]

class Window(tk.Tk):  
    def __init__(self, title, width, height):
        super(Window, self).__init__()

        self.title(title)  
        self.width, self.height = width, height
        self.screenwidth, self.screenheight = self.winfo_screenwidth(), self.winfo_screenheight()
        self.size = "%dx%d+%d+%d" % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.geometry(self.size)
        self.resizable(False, False)  

class Main(tk.Frame):  
    def __init__(self, master):
        super(Main, self).__init__(master)
        self.master = master
        self.login_desktop = None  
        self.register_desktop = None  
        self.pack(fill=tk.BOTH, expand=True)  
        
        self.login_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.desktop()

    def desktop(self):  
        if self.get_user_info():  
            self.Login()  
        else:  
            self.register_()  

    def get_user_info(self) -> bool:  
        global UserInfo_list
        try:
            with open("UserLogin.txt", "r") as f1, open("UserPassword.txt", "r") as f2:
                if f1.read().strip() == "" or f2.read().strip() == "":
                    return False
                else:
                    f1.seek(0)
                    f2.seek(0)
                    UserInfo_list[0] = f1.read().strip()
                    UserInfo_list[1] = f2.read().strip()
                    return True
        except FileNotFoundError:
            return False

    def Login(self):  
        self.login_desktop = tk.Frame(self)
        self.login_desktop.place(x=0, y=0, width=WIDTH, height=HEIGHT)
        tk.Label(self.login_desktop, text="MindBlowing", font=("Arial", 20)).pack()
        tk.Label(self.login_desktop, text="Name:").place(x=0, y=50, width=70, height=25)
        ttk.Entry(self.login_desktop, textvariable=self.login_var).place(x=70, y=50, width=100, height=25)
        tk.Label(self.login_desktop, text="Password:").place(x=0, y=80, width=70, height=25)
        ttk.Entry(self.login_desktop, textvariable=self.password_var, show="*").place(x=70, y=80, width=100, height=25)
        ttk.Button(self.login_desktop, text="Login", cursor="hand2", command=self.login_in).place(x=40, y=130, width=80, height=25)
        ttk.Button(self.login_desktop, text="Signup", cursor="hand2", command=lambda: self.register_in(True)).place(x=120, y=130, width=80, height=25)

    def login_in(self):  
        if self.login_var.get() == UserInfo_list[0] and self.password_var.get() == UserInfo_list[1]:  
            messagebox.showinfo("Hint", "Login Success")
            self.login_desktop.destroy()
            self.start_quiz()
        else:
            messagebox.showerror("Error", "Wrong Name or Password")

    def register_in(self, InLogin=False):  
        if self.login_var.get() != "" and self.password_var.get() != "":
            if InLogin:  
                answer = messagebox.askyesno("Hint", "Are you sure? This will rewrite previous Name and Password")
                if answer:  
                    with open("UserLogin.txt", "w") as f1, open("UserPassword.txt", "w") as f2:
                        f1.write(self.login_var.get())
                        f2.write(self.password_var.get())
                    messagebox.showinfo("Hint", "Signup success")
                else:
                    messagebox.showinfo("Hint", "User has canceled Signup")
            else:
                with open("UserLogin.txt", "w") as f1, open("UserPassword.txt", "w") as f2:
                    f1.write(self.login_var.get())
                    f2.write(self.password_var.get())
                messagebox.showinfo("Hint", "Signup success")
        else:
            messagebox.showerror("Error", "Name or Password can't be blank")

    def register_(self):
        self.register_desktop = tk.Frame(self)
        self.register_desktop.place(x=0, y=0, width=WIDTH, height=HEIGHT)
        tk.Label(self.register_desktop, text="MindBlowing", font=("Arial", 20)).pack()
        tk.Label(self.register_desktop, text="Name:").place(x=0, y=50, width=70, height=25)
        ttk.Entry(self.register_desktop, textvariable=self.login_var).place(x=70, y=50, width=100, height=25)
        tk.Label(self.register_desktop, text="Password:").place(x=0, y=80, width=70, height=25)
        ttk.Entry(self.register_desktop, textvariable=self.password_var, show="*").place(x=70, y=80, width=100, height=25)
        ttk.Button(self.register_desktop, text="Signup", cursor="hand2", command=lambda: self.register_in(False)).place(x=5, y=110, width=(WIDTH - 15) / 2, height=25)

    def start_quiz(self):
        self.pack_forget()
        root = tk.Toplevel(self.master)
        app = QuizApp(root)
        root.mainloop()

# Initialize pygame mixer for background music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Game music.mp3')
pygame.mixer.music.play(-1)

# Set up constants
BG_IMAGE_PATH = "SKY.png"
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
QUIZ_DATA_PATH = "quiz_data.json"

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind-Blowing Quiz!")
        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.bg_image = PhotoImage(file=BG_IMAGE_PATH)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        
        self.quiz_data = self.load_quiz_data()
        
        self.question_num = 0
        self.guesses = []

        self.init_quiz()

    def load_quiz_data(self):
        try:
            with open(QUIZ_DATA_PATH, 'r') as file:
                quiz_data = json.load(file)
            return quiz_data.get('quiz', [])
        except FileNotFoundError:
            messagebox.showerror("Error", f"Quiz data file not found: {QUIZ_DATA_PATH}")
            self.root.quit()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Failed to decode quiz data. Ensure the JSON file is correctly formatted.")
            self.root.quit()

    def init_quiz(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        self.canvas.create_text(CANVAS_WIDTH // 2, 50, text="Welcome to the Mind-Blowing Quiz!", font=("Arial", 24, "bold"))
        start_button = tk.Button(self.root, text="Start Quiz", command=self.display_question)
        self.canvas.create_window(CANVAS_WIDTH // 2, 200, window=start_button)

    def display_question(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

        if self.question_num < len(self.quiz_data):
            question_data = self.quiz_data[self.question_num]
            question_type = question_data.get('type', 'unknown')
            question_text = question_data.get('question', '')

            self.canvas.create_text(CANVAS_WIDTH // 2, 50, text=question_text, font=("Arial", 18), width=600, justify="center")

            if question_type == "multiple_choice":
                self.display_multiple_choice(question_data)
            elif question_type == "true_false":
                self.display_true_false(question_data)
            elif question_type == "fill_in_the_blank":
                self.display_fill_in_the_blank(question_data)
            else:
                messagebox.showerror("Error", f"Unknown question type: {question_type}")
        else:
            self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, text="Congratulations! You have completed the quiz!", font=("Arial", 24, "bold"))

    def display_multiple_choice(self, question_data):
        options = question_data.get('options', [])
        for idx, option in enumerate(options):
            btn = tk.Button(self.root, text=option, width=30, command=lambda opt=option: self.check_answer(opt))
            self.canvas.create_window(CANVAS_WIDTH // 2, 150 + idx * 50, window=btn)

    def display_true_false(self, question_data):
        btn_true = tk.Button(self.root, text="True", width=30, command=lambda: self.check_answer("true"))
        btn_false = tk.Button(self.root, text="False", width=30, command=lambda: self.check_answer("false"))
        self.canvas.create_window(CANVAS_WIDTH // 2 - 100, 150, window=btn_true)
        self.canvas.create_window(CANVAS_WIDTH // 2 + 100, 150, window=btn_false)

    def display_fill_in_the_blank(self, question_data):
        entry = tk.Entry(self.root, width=50)
        self.canvas.create_window(CANVAS_WIDTH // 2, 150, window=entry)
        submit_btn = tk.Button(self.root, text="Submit", width=30, command=lambda: self.check_answer(entry.get()))
        self.canvas.create_window(CANVAS_WIDTH // 2, 200, window=submit_btn)

    def check_answer(self, answer):
        self.guesses.append(answer)
        self.question_num += 1
        self.display_question()

if __name__ == "__main__":
    root = Window(TITLE, WIDTH, HEIGHT)
    app = Main(root)
    root.mainloop()
