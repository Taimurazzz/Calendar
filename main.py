from tkinter import *
import calendar
import datetime
root = Tk()
root.title('Calendar')

now = datetime.datetime.now()
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 
            'Октябрь', 'Ноябрь', 'Декабрь',]
weekDays = ['пн', 'вт', 'ср', 'чт', 'пн', 'сб', 'вс']
day = now.day
year = now.year
month = now.month
days = []
startDay = calendar.monthrange(year, month)[0]
currentDays = calendar.monthrange(year, month)[1]
selectItem = 1

lbl = Label(root, text=months[month - 1], font=('Verdana', 20, 'normal'), fg='darkblue')
lbl.grid(row=0, column=0)

def addSelect(num):
    global selectItem
    selectItem += num
    fill(selectItem)

btnUp = Button(root, text ="Вверх", command = lambda: addSelect(-7))
btnUp.grid(row=0, column=1)
btnUp = Button(root, text ="Вниз", command = lambda: addSelect(7))
btnUp.grid(row=0, column=2)
btnUp = Button(root, text ="Вправо", command = lambda: addSelect(1))
btnUp.grid(row=0, column=3)
btnUp = Button(root, text ="Влево", command = lambda: addSelect(-1))
btnUp.grid(row=0, column=4)


for weekD in range(7):
    lbl = Label(root, text=weekDays[weekD], width=10, height=10,
    font=('Verdana', 14, 'normal'), fg='darkblue')
    lbl.grid(row=2, column=weekD, sticky='nsew')

def fill(selectItem):
    counterDay = 1
    isSelect = False
    for row in range(6):
        for col in range(7):
            if counterDay > currentDays:
                counterDay = 1

            if row == 0:
                if col < startDay:
                    continue

            if counterDay == day:
                lbl = Label(root, text=counterDay, width=4, height=2, font=('Verdana', 16, 'bold'))
            elif selectItem == counterDay and not(isSelect): 
                lbl = Label(root, text=counterDay, width=4, height=2, font='Times 16', fg='red')
                isSelect = True
            else:
                lbl = Label(root, text=counterDay, width=4, height=2, font=('Verdana', 16, 'normal'))

            lbl.grid(row=row+3, column=col, sticky='nsew')
            counterDay += 1 

fill(selectItem)

root.mainloop()
