import tkinter as tk
from tkinter import simpledialog
import time
import threading
import platform

# For sound, use winsound on Windows and pygame on other platforms
if platform.system() == "Windows":
    import winsound
else:
    import pygame
    pygame.init()

def play_beep():
    if platform.system() == "Windows":
        winsound.Beep(1000, 500)  # Frequency 1000 Hz, Duration 500 ms
    else:
        pygame.mixer.Sound('beep.wav').play()

def countdown(timer_seconds):
    for remaining in range(timer_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer_display.set(f"{mins:02d}:{secs:02d}")
        root.update()
        if remaining <= 3:
            play_beep()
        time.sleep(1)
    timer_display.set("00:00")
    play_beep()

def start_timer():
    timer_seconds = simpledialog.askinteger("Input", "Enter the number of seconds:")
    if timer_seconds:
        threading.Thread(target=countdown, args=(timer_seconds,)).start()

root = tk.Tk()
root.title("Timer")
root.geometry("200x200")
root.attributes("-topmost", True)

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Draw a circle
canvas.create_oval(50, 50, 150, 150, outline="black", width=2)

# Timer display in the center of the circle
timer_display = tk.StringVar()
timer_display.set("00:00")
label = tk.Label(root, textvariable=timer_display, font=("Helvetica", 24))
canvas.create_window(100, 100, window=label)

# Start button
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=20)

root.mainloop()
