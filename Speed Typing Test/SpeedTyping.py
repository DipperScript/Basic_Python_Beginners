import tkinter as tk
import time
import threading
import random
from ttkthemes import ThemedStyle

class TypeSpeedGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Checker")

        style = ThemedStyle(self.root)
        style.set_theme("arc")  # Use the "arc" theme

        self.texts = open("test.txt", "r").read().split("\n")
        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Helvetica", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, pady=10, padx=5)
        self.input_entry.bind("<Key>", self.start)
        self.input_entry.bind("<FocusIn>", self.reset_color)

        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS\n0.00 CPM", font=("Helvetica", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False
        self.correct_text = self.sample_label.cget('text')
        self.is_correct = False

        self.root.mainloop()

    def start(self, event):
        if not event.keycode in [16, 17, 18]:
            self.running = True
            t = threading.Thread(target=self.time_thread)
            t.start()

        typed_text = self.input_entry.get()
        if not self.correct_text.startswith(typed_text):
            self.input_entry.config(fg="red")
            self.is_correct = False
        else:
            self.input_entry.config(fg="black")
            self.is_correct = True

        if typed_text == self.correct_text:
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM")

    def reset(self):
        self.correct_text = random.choice(self.texts)
        self.sample_label.config(text=self.correct_text)
        self.input_entry.delete(0, tk.END)
        self.input_entry.config(fg="black")
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM")
        self.counter = 0
        self.running = False
        self.is_correct = False

    def reset_color(self, _):
        self.input_entry.config(fg="black")

TypeSpeedGUI()
