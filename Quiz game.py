from tkinter import Tk, Canvas, messagebox, PhotoImage
import tkinter as tk
import pygame
import pygame.mixer


pygame.init()
BG = pygame.image.load("SKY.png")

canvas_width=800
canvas_height=400
questions = [
    "What is the past tense of the verb go?: ",
    "Which of the following is a synonym for happy?: ",
    "What is a synonym for the word exhilarating?: ",
    "She ____ to the gym every morning.: ",
    "Choose the correct word to complete the sentence: Her speech was full of _______ quotes.: ",
    ]

options = [
    ["A. Goes", "B. Gone", "C. Went", "D. Going"],
    ["A. Sad ", "B. Angry", "C. Joyful", "D. Tired"],
    ["A. Boring", "B. Exciting", "C. Calm", "D. Depressing"],
    ["A. go", "B. going", "C. goes", "D. gone"],
    ["A. inspiring","B. inspiration", "C. inspire", "D. inspired"]
      ]

answers=["C","C","B","C","A"]

music=pygame.mixer.music.load('Game music.mp3')
pygame.mixer.music.play(-1)
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind-Blowing!")
        self.init_quiz()

    def init_quiz(self):
        self.score = 0
        self.question_num = 0
        self.guesses = []

        self.canvas = Canvas(self.root, width=800, height=400)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = PhotoImage(file="SKY.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

        self.question_label = tk.Label(self.root, text=questions[self.question_num], wraplength=400, justify="left", bg="white")
        self.canvas.create_window(400, 100, window=self.question_label)

        self.var = tk.StringVar()
        self.option_buttons = []
        for option in options[self.question_num]:
            btn = tk.Radiobutton(self.root, text=option, variable=self.var, value=option[0], indicatoron=0, width=20, pady=5)
            self.option_buttons.append(btn)
            self.canvas.create_window(400, 160 + len(self.option_buttons) * 40, window=btn)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.canvas.create_window(400, 380, window=self.submit_button)

    def check_answer(self):
        guess = self.var.get()
        self.guesses.append(guess)
        if guess == answers[self.question_num]:
            self.score += 1

        self.question_num += 1
        if self.question_num < len(questions):
            self.update_question()
        else:
            self.show_results()

    def update_question(self):
        self.question_label.config(text=questions[self.question_num])
        self.var.set(None)
        for i, option in enumerate(options[self.question_num]):
            self.option_buttons[i].config(text=option, value=option[0])

    def show_results(self):
        self.root.quit()
        result_window = tk.Tk()
        result_window.title("Quiz Results")

        score_percentage = int(self.score / len(questions) * 100)
        result_label = tk.Label(result_window, text=f"Your score is: {score_percentage}%", pady=20)
        result_label.pack()

        answers_label = tk.Label(result_window, text=f"Correct answers: {' '.join(answers)}", pady=5)
        answers_label.pack()

        guesses_label = tk.Label(result_window, text=f"Your guesses: {' '.join(self.guesses)}", pady=5)
        guesses_label.pack()

        close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
        close_button.pack(pady=20)
        
        playagain_button = tk.Button(result_window, text="Play Again", command=self.play_again)
        playagain_button.pack(pady=10)

        result_window.protocol("WM_DELETE_WINDOW", lambda: (self.root.deiconify(), result_window.destroy()))

        result_window.mainloop()
        
    def play_again(self):
        self.root.deiconify()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.init_quiz()
            
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
