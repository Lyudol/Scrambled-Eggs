import subprocess
import os
from tkinter import *

def wordgame():
    import random

    def authenticator():
        idek = wordsubmit.get()
        
        wordsubmit_s = str(idek)
        
        print(wordsubmit_s)

        if len(wordsubmit_s) > 5:
            instruction.config(text="Careful! Make sure you don't use more than 5 letters.", fg="red")    
        else:
            if  wordsubmit_s not in flatlist:
                instruction.config(text="Careful! Make sure you only use the letters shown above.", fg="red")
            else:
                wordchecker(wordsubmit_s)

    consonants = ["B", "C", "D", "F", "G", "H", "J", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    vowels = ["A", "E", "I", "O", "U", "Y"]

    parent = Tk()
    parent.title("Scrambled Eggs")
    parent.geometry("500x400")

    consonants_shuffled = random.sample(consonants, len(consonants))
    vowels_shuffled = random.sample(vowels, len(vowels))

    L1 =(random.choice(consonants_shuffled))
    L2 =(random.choice(vowels_shuffled))
    L3 =(random.choice(consonants_shuffled))
    L4 =(random.choice(vowels_shuffled))
    L5 =(random.choice(consonants_shuffled))
    
    letterorder = [L1, L2, L3, L4, L5]

    gameletter = random.sample(letterorder, len(letterorder))
    gamewidget = Label(parent, text=gameletter, font=("Arial", 70))
    gamewidget.pack()
    instruction = Label(parent, text="Try to rearrange these letters into a word. The longer the word, the more points you win!")
    instruction.pack()
    wordsubmit = Entry(parent, width=20, justify="center")
    wordsubmit.pack(pady=5)
    guess = Button(parent, text="Submit", bg="#e0dc8d", command=authenticator)
    guess.pack(pady=5)
    newgame = Button(parent, text="New Game", bg="#5a6309")
    newgame.pack(pady=3)
    parent.mainloop()

    merge = ["".join(gameletter)]

    count = 0
    while count < 286:
        switcher = random.sample(gameletter, len(gameletter))
        joiner = "".join(switcher)
        merge.append(joiner)
        count = count + 1
    flatlist = ("".join(merge))
                
    def wordchecker(wordsubmit_s):
        from english_words import english_words_alpha_set
        if wordsubmit_s not in english_words_alpha_set:
            instruction.config(text="Hey! That's not a real word!", fg="red")
        elif wordsubmit_s in english_words_alpha_set:
            points = str(len(wordsubmit_s))
            instruction.config("Nice! You got " + points + " points!", fg="green")
            guess.destroy()
            wordgame()

        


        
pip_output = subprocess.check_output("pip install english-words", encoding='UTF-8')
clear = lambda: os.system('cls')
clear()

if "Requirement already satisfied" in pip_output:
    wordgame()
else:
    pass