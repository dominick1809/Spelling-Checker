import tkinter
from tkinter import *
from textblob import TextBlob 

# Create the main Tkinter window
root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

# Function to check spelling using TextBlob
def check_spelling():
    # Get the input text from the Entry widget
    word = enter_text.get()
    
    # Create a TextBlob object for spell checking
    text_blob = TextBlob(word)
    
    # Get the corrected text
    corrected_text = str(text_blob.correct())

    # Create a label to display the corrected text
    correct_label = Label(root, text="Correct text is :", font=("poppins", 20), bg="#dae6f0", fg="#364971")
    correct_label.place(x=100, y=250)
    
    # Update the Label with the corrected text
    spell.config(text=corrected_text)

# GUI elements
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50,0))

# Entry widget for user input
enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

# Button to trigger the spelling check
button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

# Label to display the corrected text
spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250)

# Start the Tkinter event loop
root.mainloop()
