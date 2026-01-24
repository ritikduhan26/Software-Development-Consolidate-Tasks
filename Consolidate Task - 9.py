# Consolidate Task 9



 # import tkinter for GUI

import tkinter as tk  

 # import tkinter for GUI

# function to count words
def countword():

    text = textbox.get("1.0", tk.END).strip()

# If text box is empty

    if text == "":
        result_label.config(text="Please enter text.")

    else:

# split text into words
        words = text.split()

 # count words
        wordcount = len(words)

 # count characters
        charactercount = len(text)

 # Result on screen

        result_label.config(
            text="Words: " + str(wordcount) + " | Characters: " + str(charactercount)
        )


# Main window of word count GUI

window = tk.Tk()
window.title("Word Counter GUI")
window.geometry("500x500")

heading = tk.Label(window, text="Enter Words to Count", font=("Times New Roman", 19))
heading.pack(pady=10)

# Input tetx box

textbox = tk.Text(window, height=10, width=53, border=4)
textbox.pack(pady=10)

# Button

count_button = tk.Button(window, text="Count Words", command=countword)
count_button.pack(pady=5)

# Show result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
