from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps


    pomo_label.config(text="TIMER", fg=GREEN)
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_mins = WORK_MIN * 60
    short_break_mins = SHORT_BREAK_MIN * 60
    long_break_mins = LONG_BREAK_MIN * 60

    reps += 1
    if reps%8 == 0:
        pomo_label.config(text="BREAK", fg=RED)
        count_down(long_break_mins)
    elif reps % 2 == 0:
        pomo_label.config(text="BREAK", fg=PINK)
        count_down(short_break_mins)
    else:
        pomo_label.config(text="WORK", fg=GREEN)
        count_down(work_mins)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min )

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100,130,text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=2, row=2, padx=25, pady=25)


start_button = Button(window, text="START", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(window, text="RESET", command=reset)
reset_button.grid(column=3, row=3)

pomo_label = Label(window, text="Pomodoro Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
pomo_label.grid(column=2, row=1)

check_label = Label(window, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=4)







window.mainloop()

