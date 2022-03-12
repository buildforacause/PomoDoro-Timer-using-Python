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
mark = ""
timer_on = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    # after cancel will stop the after function (if any) which in this case is our updating timer every second function
    window.after_cancel(timer_on)
    # changing the values to default again as it is being reset
    main_label.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(timer, text="00:00")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    # every 8th rep you should get a long break of 20 minutes and every other even number rep you should get a short
    # break. odd reps means you gotta work 25 minutes
    global reps
    reps += 1
    # converting minutes to seconds
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    # implementing the logic written above
    if reps % 8 == 0:
        countdown(long_break_sec)
        main_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        main_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        main_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps, mark, timer_on
    minutes = math.floor(count / 60)
    seconds = count % 60
    # dynamic typing in this if block
    if seconds < 10:
        seconds = f"0{seconds}"
    elif minutes < 10:
        minutes = f"0{minutes}"
    time_remaining = f"{minutes}:{seconds}"
    # updating the timer text
    canvas.itemconfig(timer, text=time_remaining)
    if count > 0:
        timer_on = window.after(1000, countdown, count - 1)
    else:
        # if a rep has finished , go to next rep and add a check mark at every even rep to denote a complete
        # work session
        start_timer()
        if reps % 2 == 0:
            mark += "✔"
            check_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("PomoDoro Timer")
# adding some padding to our window
window.config(padx=100, pady=50, bg=YELLOW)
# setting up labels and placing on screen with the grid layout manager
main_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45), bg=YELLOW)
main_label.grid(row=0, column=1)
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)
# photoimage class enables us to use an image to be created on our canvas widget as it accepts that particular type
# of argument only.
image = PhotoImage(file="tomato.png")
# creating a canvas (which allows us to lay things one top of the other)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# creating an image in our canvas
canvas.create_image(100, 112, image=image)
# creating a canvas text which will show on top of our image
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# packing it so that it is visible on our window
canvas.grid(row=1, column=1)
# creating start and reset buttons
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)
# countdown(5)
window.mainloop()
