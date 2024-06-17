from tkinter import Tk, Canvas, messagebox, PhotoImage
import tkinter as tk
import pygame
import pygame.mixer
import json
import os
from tkinter import simpledialog
pygame.init()
BG = pygame.image.load("SKY.png")

canvas_width=800
canvas_height=600

current_dir = os.path.dirname(os.path.abspath('C:\Mini It Project\Project\Test\quiz_data.json'))

relative_path = os.path.join("Test", "quiz_data.json")

json_file_path = os.path.join(current_dir, relative_path)

with open('C:\Mini It Project\Project\Test\quiz_data.json', 'r') as file:
   quiz_data=json.load(file)

def log_score(player_name, score):
    scores_file = os.path.join(current_dir, "quiz_scores(2).txt")
    with open(scores_file, 'a') as f:
        f.write(f"Player: {player_name} | Score: {score}\n")
        
music=pygame.mixer.music.load('Game music.mp3')
pygame.mixer.music.play(-1)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind-Blowing!")
        self.player_name=self.ask_player_name()
        self.init_quiz()

    def ask_player_name(self):
        name = simpledialog.askstring("Player Name", "Please enter your name:")
        if not name:
            name = "Anonymous"  # Default name if none is provided
        return name
    
    def init_quiz(self):
        self.score = 0
        self.question_num = 0
        self.guesses = []

        self.canvas = Canvas(self.root, width=800, height=400)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = PhotoImage(file="SKY.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        
        self.display_question()

    def display_question(self):
        question_data = quiz_data[self.question_num]
    
        self.question_label = tk.Label(self.root, text=question_data['question'], wraplength=400, justify="left", bg="white")
        self.canvas.create_window(400, 50, window=self.question_label)

        self.var = tk.StringVar()
        self.option_button=[]
        for idx, option in enumerate(question_data['options']):
            btn = tk.Radiobutton(self.root, text=option, variable=self.var, value=option[0], indicatoron=0, width=50, height=2)
            self.option_button.append(btn)
            self.canvas.create_window(400, 100 + idx * 80, window=btn)
            
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.canvas.create_window(400, 390, window=self.submit_button)

    def check_answer(self):
        guess = self.var.get() 
        self.guesses.append(guess)
        if guess == quiz_data[self.question_num]['answer']:
            self.score += 1            

        self.question_num += 1
        if self.question_num < len(quiz_data):
            self.update_question()
        else:
            self.show_results()

    def update_question(self):
        self.question_label.config(text=quiz_data[self.question_num]['question'])
        self.var.set(None)
        for i, option in enumerate(quiz_data[self.question_num]['options']):
            self.option_button[i].config(text=option, value=option[0])

    def show_results(self):
        self.root.quit()
        result_window = tk.Tk()
        result_window.title("Quiz Results")

        score_percentage = int(self.score / len(quiz_data) * 100)
        result_label = tk.Label(result_window, text=f"Your score is: {score_percentage}%", pady=20)
        result_label.pack()

        answers_label = tk.Label(result_window, text=f"Correct answers: {' '.join([data['answer'] for data in quiz_data])}", pady=5)
        answers_label.pack()

        guesses_label = tk.Label(result_window, text=f"Your guesses: {' '.join(self.guesses)}", pady=5)
        guesses_label.pack()

        close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
        close_button.pack(pady=20)
        
               
        playagain_button = tk.Button(result_window, text="Play Again", command=self.play_again)
        playagain_button.pack(pady=10)

        log_score(self.player_name, score_percentage)

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
