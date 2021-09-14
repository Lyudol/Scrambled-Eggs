import subprocess
import os
from tkinter import *

def wordgame():
    import random
    
    pointsM = [0]

    consonants = ["B", "C", "D", "F", "G", "H", "J", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    vowels = ["A", "E", "I", "O", "U", "Y"]

    parent = Tk()
    parent.title("Scrambled Eggs")
    parent.geometry("500x250")
    parent.resizable(False, False)

    consonants_shuffled = random.sample(consonants, len(consonants))
    vowels_shuffled = random.sample(vowels, len(vowels))

    L1 =(random.choice(consonants_shuffled))
    L2 =(random.choice(vowels_shuffled))
    L3 =(random.choice(consonants_shuffled))
    L4 =(random.choice(vowels_shuffled))
    L5 =(random.choice(consonants_shuffled))
    
    letterorder = [L1, L2, L3, L4, L5]

    def flattener():
        from english_words import english_words_alpha_set
        global flatlist
        try:
            def checker():
                if userstr.upper() in flatlist:
                    if userstr in english_words_alpha_set:
                        points = len(userstr)
                        pointsM.append(points)
                        pointsF = sum(pointsM)
                        instruction.config(text="Nice, you have "+ str(pointsF) + " points", fg="green")
                        instruction.pack()
                        wordsubmit.delete(0, END)
                    elif userstr == "":
                        instruction.config(text="Try to rearrange these letters into a word. The longer the word, the more points you win!", fg="black")
                    elif userstr not in english_words_alpha_set:
                        instruction.config(text="Are you sure that's a word?", fg="red")
                        instruction.pack()
                        wordsubmit.delete(0, END)
                else:
                    instruction.config(text="Make sure you're using the right letters!", fg="red")
                    instruction.pack()
                    wordsubmit.delete(0, END)
            userstr = wordsubmit.get()
            count = 0
            while count < 286:
                switcher = random.sample(gameletter2, len(gameletter2))
                joiner = "".join(switcher)
                merge2.append(joiner)
                count = count + 1
            flatlist = ("".join(merge2))
            checker()
        except:    
            merge = ["".join(gameletter)]
            def checker():
                if userstr.upper() in flatlist:
                    if userstr in english_words_alpha_set:
                        points = len(userstr)
                        pointsM.append(points)
                        pointsF = sum(pointsM)
                        instruction.config(text="Nice, you have "+ str(pointsF) + " points", fg="green")
                        instruction.pack()
                        wordsubmit.delete(0, END)
                    elif userstr == "":
                        instruction.config(text="Try to rearrange these letters into a word. The longer the word, the more points you win!", fg="black")
                    elif userstr not in english_words_alpha_set:
                        instruction.config(text="Are you sure that's a word?", fg="red")
                        instruction.pack()
                        wordsubmit.delete(0, END)
                else:
                    instruction.config(text="Make sure you're using the right letters!", fg="red")
                    instruction.pack()
                    wordsubmit.delete(0, END)
            userstr = wordsubmit.get()
            count = 0
            while count < 286:
                switcher = random.sample(gameletter, len(gameletter))
                joiner = "".join(switcher)
                merge.append(joiner)
                count = count + 1
            flatlist = ("".join(merge))
            checker()

    gameletter = random.sample(letterorder, len(letterorder))
    gamewidget = Label(parent, text=gameletter, font=("Arial", 70))
    gamewidget.pack()
    instruction = Label(parent, text="Try to rearrange these letters into a word. The longer the word, the more points you win!")
    instruction.pack()
    wordsubmit = Entry(parent, width=20, justify="center")
    wordsubmit.pack(pady=5)
    guess = Button(parent, text="Submit", bg="#e0dc8d", command=flattener)
    guess.pack(pady=5)
    
    def clearpoints():
        pointsM.clear()
        newword()

    def newword():
        global merge2
        global gameletter2
        L1 =(random.choice(consonants_shuffled))
        L2 =(random.choice(vowels_shuffled))
        L3 =(random.choice(consonants_shuffled))
        L4 =(random.choice(vowels_shuffled))
        L5 =(random.choice(consonants_shuffled))
    
        letterorder = [L1, L2, L3, L4, L5]

        gameletter2 = random.sample(letterorder, len(letterorder))
        merge2 = ["".join(gameletter2)]
        gamewidget.config(text=gameletter2)
        gamewidget.pack
        flattener()

    newgame = Button(parent, text="New Game", bg="#5a6309", command=clearpoints)
    newgame.pack(pady=3)
    parent.mainloop()
            
pip_output = subprocess.check_output("pip install english-words", encoding='UTF-8')
clear = lambda: os.system('cls')
clear()

if "Requirement already satisfied" in pip_output:
    wordgame()
else:
    pass