import tkinter as tk
from tkinter import ttk
from playsound import playsound
import threading
import time

class CountdownTimer:
    def _init_(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("200x200")
        self.root.configure(bg="#f0f0f0")

        self.time_remaining = 300  # 5 minutes in seconds
        self.is_running = False

        # Timer display
        self.timer_label = ttk.Label(root, text=self.format_time(self.time_remaining), font=("Arial", 30), background="#fff", foreground="#333")
        self.timer_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=120, height=120)

        # Start the timer automatically
        self.start_timer()

    def start_timer(self):
        self.is_running = True
        self.update_timer()

    def update_timer(self):
        if self.is_running and self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=self.format_time(self.time_remaining))
            
            if self.time_remaining <= 3 and self.time_remaining > 0:
                threading.Thread(target=playsound, args=("https://www.soundjay.com/button/beep-07.wav",), daemon=True).start()

            self.root.after(1000, self.update_timer)
        else:
            self.is_running = False

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

# Set up the root window
root = tk.Tk()
app = CountdownTimer(root)

# Run the Tkinter event loop
root.mainloop()