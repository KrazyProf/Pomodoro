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
check_symbol = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_symbol , reps
    reps = 0
    check_symbol = ''

    window.after_cancel(timer)
    label.config(text="Timer" , fg=GREEN)
    canvas.itemconfig(timer_text , text = "00:00")
    check_mark.config(text=check_symbol)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_mins = WORK_MIN * 60 
    short_break_mins = SHORT_BREAK_MIN * 60
    long_break_mins = LONG_BREAK_MIN * 60

    # long break
    if reps % 8  == 0:
        count_down(long_break_mins)
        label.config(text='Break' , fg=RED)
    # short break
    elif reps % 2 == 0:
        count_down(short_break_mins)
        label.config(text='Break' , fg=PINK)
    # work     
    else :
        count_down(work_mins)
        label.config(text='Work' , fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count) :
    global reps, check_symbol, timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        canvas.itemconfig(timer_text , text = f"{count_min}:00")
    elif count_sec < 10:
        canvas.itemconfig(timer_text , text = f"{count_min}:0{count_sec}")
    else:
        canvas.itemconfig(timer_text , text = f"{count_min}:{count_sec}")
    if count > 0 :
        timer = window.after(1000 ,count_down ,count - 1)
    else:
        start_timer()
        # for every one session
        if reps % 2 == 0 :
            check_symbol += '✅'
            check_mark.config(text=check_symbol)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100 , pady=50 , bg=YELLOW)
window.title('Pomodoro')


canvas = Canvas(width=200 , height=224 , bg=YELLOW)
img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112 , image= img)
timer_text = canvas.create_text(100 , 130 , text='00:00' , fill='white' , font=(FONT_NAME , 32 , 'bold'))
canvas.grid(column=1, row=1)

label = Label(text='Timer' , fg=GREEN , bg=YELLOW,  font=(FONT_NAME , 50))
label.grid(column=1, row=0)


start_btn = Button(text='start' , highlightthickness= 0 , command=start_timer)
start_btn.grid(column=0 , row=2)

reset_btn = Button(text='reset' , highlightthickness=0 , command=reset_timer)
reset_btn.grid(column=2 , row=2)


check_mark = Label(bg=YELLOW , fg=GREEN)
check_mark.grid(column=1, row=3)



window.mainloop()
