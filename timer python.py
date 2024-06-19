import tkinter as tk
import time
import winsound  # for Windows, use `os.system` for Mac/Linux

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.root.geometry("200x200")
        self.root.configure(background="#f0f0f0")

        self.timer_container = tk.Label(self.root, text="05:00", font=("Arial", 24, "bold"), bg="#fff", fg="#333")
        self.timer_container.pack(pady=20)

        self.controls = tk.Frame(self.root, bg="#f0f0f0")
        self.controls.pack()

        self.beep_sound = "beep.wav"  # replace with your beep sound file

        self.start_timer()

        self.root.mainloop()

    def start_timer(self):
        self.time = 300
        self.update_timer_display(self.time)
        self.timer = self.root.after(1000, self.decrement_time)

    def decrement_time(self):
        self.time -= 1
        self.update_timer_display(self.time)
        if self.time <= 3 and self.time > 0:
            winsound.PlaySound(self.beep_sound, winsound.SND_FILENAME)  # play beep sound
        if self.time <= 0:
            self.root.after_cancel(self.timer)
        else:
            self.timer = self.root.after(1000, self.decrement_time)

    def update_timer_display(self, time):
        minutes = time // 60
        seconds = time % 60
        formatted_time = f"{minutes:02d}:{seconds:02d}"
        self.timer_container.config(text=formatted_time)

if __name__ == "__main__":
    CountdownTimer()