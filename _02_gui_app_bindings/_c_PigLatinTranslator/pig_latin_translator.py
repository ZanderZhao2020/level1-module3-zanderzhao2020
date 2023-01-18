"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize an Entry (tk.Entry) for the input text
        self.entry = tk.Entry(self)
        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed
        self.button = tk.Button(self, text="Translate")
        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text
        self.label = tk.Label(self)
        # TODO: Look at the example image () and place all the
        #  components in the same order
        self.entry.place(relx=0, rely=0, relwidth=0.4, relheight=1)
        self.button.place(relx=0.4, rely=0, relwidth=0.2, relheight=1)
        self.label.place(relx=0.6, rely=0, relwidth=0.4, relheight=1)
        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released
        self.button.bind("<ButtonPress>", self.on_key_press)

    def on_key_press(self, event):
        print('button pressed!')

        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry
        self.label.configure(text=PigLatinConverter.translate(self.entry.get()))

if __name__ == '__main__':
    # TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
    #  Remember to call mainloop() at the end
    app = PigLatinTranslator()
    app.title("PigLatinTranslator")
    app.geometry("1000x500")
    app.mainloop()
