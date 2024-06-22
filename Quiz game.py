import tkinter as tk
from tkinter import Canvas, PhotoImage, messagebox, simpledialog
import json
import os
import pygame
import pygame.mixer

# Initialize pygame mixer for background music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Game music.mp3')
pygame.mixer.music.play(-1)

# Set up constants
BG_IMAGE_PATH = "SKY.png"
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
QUIZ_DATA_PATH = "quiz_data.json"  # Assuming quiz_data.json is in the same directory as this script

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
        """Load quiz data from a JSON file."""
        try:
            with open(os.path.join(os.path.dirname(__file__), QUIZ_DATA_PATH), 'r') as file:
                quiz_data = json.load(file)
            return quiz_data.get('quiz', [])  # Ensure it returns an empty list if 'quiz' key is missing
        except FileNotFoundError:
            messagebox.showerror("Error", f"Quiz data file not found: {QUIZ_DATA_PATH}")
            self.root.quit()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Failed to decode quiz data. Ensure the JSON file is correctly formatted.")
            self.root.quit()

    def init_quiz(self):
        """Initialize the quiz interface."""
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        self.canvas.create_text(CANVAS_WIDTH // 2, 50, text="Welcome to the Mind-Blowing Quiz!", font=("Arial", 24, "bold"))

        start_button = tk.Button(self.root, text="Start Quiz", command=self.display_question)
        self.canvas.create_window(CANVAS_WIDTH // 2, 200, window=start_button)

    def display_question(self):
        """Display the current question based on its type."""
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
            # Display end of quiz message
            self.canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, text="Congratulations! You have completed the quiz!", font=("Arial", 24, "bold"))

    def display_multiple_choice(self, question_data):
        """Display multiple choice options."""
        options = question_data.get('options', [])
        for idx, option in enumerate(options):
            btn = tk.Button(self.root, text=option, width=30, command=lambda opt=option: self.check_answer(opt))
            self.canvas.create_window(CANVAS_WIDTH // 2, 150 + idx * 50, window=btn)

    def display_true_false(self, question_data):
        """Display true/false options."""
        btn_true = tk.Button(self.root, text="True", width=30, command=lambda: self.check_answer("true"))
        btn_false = tk.Button(self.root, text="False", width=30, command=lambda: self.check_answer("false"))
        self.canvas.create_window(CANVAS_WIDTH // 2 - 100, 150, window=btn_true)
        self.canvas.create_window(CANVAS_WIDTH // 2 + 100, 150, window=btn_false)

    def display_fill_in_the_blank(self, question_data):
        """Display a fill-in-the-blank entry."""
        
        entry = tk.Entry(self.root, width=50)
        self.canvas.create_window(CANVAS_WIDTH // 2, 150, window=entry)
        submit_btn = tk.Button(self.root, text="Submit", width=30, command=lambda: self.check_answer(entry.get()))
        self.canvas.create_window(CANVAS_WIDTH // 2, 200, window=submit_btn)

    def check_answer(self, answer):
        """Check the answer provided by the user."""
        self.guesses.append(answer)
        self.question_num += 1
        self.display_question()

    def play_again(self):
        """Reset the quiz for another round."""
        self.question_num = 0
        self.guesses = []
        self.init_quiz()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
