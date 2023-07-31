import datetime as dt
from threading import *
from time import strftime
from tkinter import *
from playsound import playsound

window = Tk()
window.title("Alarm Clock")
window.geometry("500x400")
window.config(bg="#00008B")


def timer():
    string = strftime('%H:%M %p')
    label.config(text=string)
    label.after(100, timer)


def threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    while True:
        set_alm = f"{hour.get()}:{minute.get()}:{second.get()}"
        curr_tim = dt.datetime.now().strftime("%H:%M:%S")
        print(curr_tim, set_alm)

        if set_alm == curr_tim:
            print("Wake up")
            playsound('Running.mp3')


frame1 = Frame(window, bg="#00008B")
frame1.pack(padx=5, pady=5)

label = Label(frame1,
              font=("CopperplateGothicLight", 50),
              foreground="White",
              bg="#00008B")
label.grid(row=0, column=0)
label.pack(anchor="center")

date = dt.datetime.now()

label1 = Label(frame1,
               text=f"{date:%a, %b %d}",
               font="CopperplateGothicLight, 15",
               foreground="White",
               bg="#00008B")
label1.pack(anchor="center")

alm = Label(frame1,
            text="Alarm",
            font="CopperplateGothicLight, 15",
            foreground="White",
            bg="#00008B")
alm.pack(anchor="center", ipady=30)

frame2 = Frame(window, bg="#00008B")
frame2.pack(padx=5, pady=5)

timeset = Label(frame2,
                text="Set Time",
                font="CopperplateGothicLight, 15",
                foreground="White",
                bg="#00008B")
timeset.pack(anchor="center")

frame = Frame(window)
frame.pack()

hour = StringVar(window)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(window)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(window)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(window, text="Set Alarm", font=("Helvetica 15"), command=threading).pack(pady=20)

timer()
mainloop()
