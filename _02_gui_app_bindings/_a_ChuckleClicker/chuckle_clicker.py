"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random
from tkinter import messagebox


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        self.button_1 = tk.Button(self, text="Joke")
        self.button_2 = tk.Button(self, text="Punchline")
        # TODO: Place the 2 buttons next to each other (see example image)
        self.button_1.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        self.button_2.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        #  example: self.joke_button.bind('<ButtonPress>', self.on_joke)
        self.button_1.bind("<ButtonPress>", self.on_joke)
        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed
        self.button_2.bind("<ButtonPress>", self.on_punchline)
    def on_joke(self, event):
        print('Joke button pressed')

        # TODO: Write your joke below!
        messagebox.showinfo("Message", "What is 1+!?")
    def on_punchline(self, event):
        print('Punchline button pressed')

        # TODO: Write a punchline to your joke!
        messagebox.showinfo("Message", "3!!!!11!!11! AAHAHAHAHAHAjf sUTHVCE(SHTSER")

if __name__ == '__main__':
    pass
    # TODO: Create a new ChuckleClicker object and set the title and geometry.
    #  Remember to call mainloop() at the end
    app = ChuckleClicker()
    app.title("Chuckle Clicker")
    app.geometry("1000x500")
    app.mainloop()
