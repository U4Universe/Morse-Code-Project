import tkinter as tk
from tkinter import Label, Text
import tkinter.font as tkfont

#creating the Morse code dictionary
Morse_Code_Dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
    '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '
}

def text_to_morse(text):
    text = text.upper()
    morse_code = ''
    for char in text:
        if char in Morse_Code_Dict.values():
            morse_code += list(Morse_Code_Dict.keys())[list(Morse_Code_Dict.values()).index(char)] + ' '
        else:
            morse_code += ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    morse_code += ' '  #ensuring there's a space at the end for final word processing
    decipher = ''
    morse_words = morse_code.split('  ')  #for split by double spaces for words
    for word in morse_words:
        if word:
            morse_letters = word.split()  #for split by single spaces for letters
            for letter in morse_letters:
                if letter:
                    decipher += Morse_Code_Dict.get(letter, 'Invalid Input')  #loookup in Morse_Code_Dict
            decipher += ' '  #for space between words
    return decipher.strip()

def update_morse_output(event):
    text = text_input.get("1.0", tk.END).strip()
    morse_code = text_to_morse(text)
    morse_output.config(state=tk.NORMAL)  #enable editing
    morse_output.delete("1.0", tk.END)
    morse_output.insert(tk.END, morse_code)
    morse_output.config(state=tk.DISABLED)  #disable editing
    
def update_text_output(event):
    morse_code = morse_input.get("1.0", tk.END).strip()
    text = morse_to_text(morse_code)
    text_output.config(state=tk.NORMAL)  #enable editing
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, text)
    text_output.config(state=tk.DISABLED)  #disable editing
    

#here the tkinter starts
root = tk.Tk()
root.title("Morse Code Translator Tool")
root.configure(bg="spring green4")

#for text_to_morse
font = tkfont.Font(family="Helvetica", size=18, weight="bold")
Label(root, text="Enter the Text", bg="spring green4",fg="white", font=font).grid(row=0, column=0, padx=10, pady=10)
input_font = tkfont.Font(family="Copper Black", size=14)
text_input = Text(root, height=3, width=40,bg="snow", font=input_font)
text_input.grid(row=0, column=1, padx=10, pady=10)
text_input.bind("<KeyRelease>", update_morse_output)
output_font = tkfont.Font(family="Copper Black", size=14, weight="bold")
morse_output = Text(root, height=3, width=40,bg="lightgreen", font = output_font)
morse_output.grid(row=1, column=1, padx=10, pady=10)

#for morse_to_text
font = tkfont.Font(family="Helvetica", size=18, weight="bold")
Label(root, text="Enter the Morse Code", bg="spring green4", fg="white", font=font).grid(row=2, column=0, padx=10, pady=10)
input_font = tkfont.Font(family="Copper Black", size=14)
morse_input = Text(root, height=3, width=40, bg="snow", font=input_font)
morse_input.grid(row=2, column=1, padx=10, pady=10)
morse_input.bind("<KeyRelease>", update_text_output)
output_font = tkfont.Font(family="Copper Black", size=14, weight="bold")
text_output = Text(root, height=3, width=40, bg="lightblue",font = output_font)
text_output.grid(row=3, column=1, padx=10, pady=10)

#run the loop
root.mainloop()
