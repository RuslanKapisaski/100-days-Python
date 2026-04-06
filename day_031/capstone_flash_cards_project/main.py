from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FRONT_TEXT_COLOR = "BLACK"
BACK_TEXT_COLOR = "WHITE"
FONT_NAME = "Arial"
LANGUAGE_FONT_SIZE = 40
LANGUAGE_STYLE = "italic"
WORD_FONT_SIZE = 60
WORD_STYLE = "bold"

#----------------------------------------+++LOAD DATA+++----------------------------------------
data = pandas.read_csv("./data/italian_words.csv")
italian_words = data["Italian"]
words_length = len(italian_words)
bulgarian_words = data["Bulgarian"]

current_word = ""

#----------------------------------------+++UI+++----------------------------------------
screen = Tk()
screen.configure(padx=50,pady=50)
screen.title("Flash Cards")
screen.configure(background=BACKGROUND_COLOR)

wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")
back_card_img = PhotoImage(file="./images/card_back.png")
front_card_img = PhotoImage(file="./images/card_front.png")

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas_side = canvas.create_image(400,250, image=front_card_img)
language = canvas.create_text(400,150,fill=FRONT_TEXT_COLOR,font=(FONT_NAME,LANGUAGE_FONT_SIZE,LANGUAGE_STYLE))
word = canvas.create_text(400,263,fill=FRONT_TEXT_COLOR,font=(FONT_NAME,WORD_FONT_SIZE,WORD_STYLE))
canvas.grid(row=0, column=0,columnspan=2)

no_btn = Button(image=wrong_img, highlightthickness=0, command=lambda: save_unlearnt_words())
no_btn.config(padx=50, pady=50)
no_btn.grid(row=1, column=0)

yes_btn = Button(image=right_img, highlightthickness=0, command=lambda: save_learnt_words())
yes_btn.config(padx=50, pady=50)
yes_btn.grid(row=1, column=1)

#----------------------------------------+++Display Words+++----------------------------------------

current_index = 0  # ДОБАВЕНО: пази текущия индекс

def display_front():
    global current_word, current_index

    italian_word = italian_words[current_index]
    bulgarian_word = bulgarian_words[current_index]
    current_word = italian_word
    canvas.itemconfig(canvas_side, image=front_card_img)
    canvas.itemconfig(language, text="Italian")
    canvas.itemconfig(word, text=italian_word)

    screen.after(3000, display_back, bulgarian_word)


def display_back(bulgarian_word):
    canvas.itemconfig(canvas_side, image=back_card_img)
    canvas.itemconfig(language, text="Bulgarian")
    canvas.itemconfig(word, text=bulgarian_word)

def next_card():
    global current_index
    current_index += 1
    if current_index < words_length:
        display_front()

#----------------------------------------+++Learnt/Unlearnt Words Mechanism+++----------------------------------------
def save_learnt_words():
    with open('./data/learnt_words.txt', 'a') as learnt_words:
        learnt_words.write(current_word + "\n")
    next_card()  # ДОБАВЕНО: минава към следващата карта

def save_unlearnt_words():
    with open('./data/unlearnt_words.txt', 'a') as unlearnt_words:
        unlearnt_words.write(current_word + "\n")
    next_card()


display_front()
screen.mainloop()