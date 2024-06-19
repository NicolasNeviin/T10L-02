import tkinter as tk

class CongratulationsWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Congratulations!")
        self.root.geometry("1000x600")
        self.root.configure(bg="#88c1f2")

        self.score_container = tk.Label(self.root, text="You scored 4/5!", bg="#2124dd", fg="white", font=("Arial", 18),
                                        border=2, relief="solid", bd=1, width=20, height=2)
        self.score_container.place(relx=0.5, rely=0.4, anchor="center")

        self.congrats_container = tk.Label(self.root, text="Congratulations!", font=("Arial", 48, "bold"), fg="#333",
                                           bg=self.root.cget("bg"))
        self.congrats_container.place(relx=0.5, rely=0.2, anchor="center")

        self.congrats_message = self.congrats_container.nametowidget("congrats_container")
        self.congrats_message.configure(text="Congratulations!", font=("Arial", 48, "bold"), fg="#333",
                                         bg=self.root.cget("bg"))

        self.button_container = tk.Frame(self.root, bg=self.root.cget("bg"))
        self.button_container.place(relx=0.5, rely=0.6, anchor="center")

        self.restart_button = tk.Button(self.button_container, text="Restart", font=("Arial", 24), fg="white",
                                         bg="#333", relief="solid", bd=2, command=self.restart_quiz)
        self.restart_button.pack(side="left", padx=20, pady=10)

        self.complete_button = tk.Button(self.button_container, text="Complete", font=("Arial", 24), fg="white",
                                         bg="#333", relief="solid", bd=2, command=self.complete_quiz)
        self.complete_button.pack(side="left", padx=20, pady=10)

        self.root.mainloop()

    def restart_quiz(self):
        self.root.destroy()
        CongratulationsWindow()

    def complete_quiz(self):
        # Add your quiz completion logic here
        print("Quiz completed!")

if __name__ == "__main__":
    CongratulationsWindow()