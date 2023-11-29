import tkinter as tk
import random

def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21 - bar11, 0)
    canvas.move(pos_1, bar12 - bar22, 0)

# Bubble Sort
def _bubble_sort():
    global barList
    global lengthList
    
    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if(lengthList[j] > lengthList[j + 1]):
                lengthList[j] , lengthList[j + 1] = lengthList[j + 1] , lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1] , barList[j]
                swap(barList[j + 1] , barList[j])
                yield

# Insertion Sort
def _insertion_sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i

        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos], barList[pos - 1])
            yield
            pos -= 1

        lengthList[pos] = cursor
        barList[pos] = cursorBar
        swap(barList[pos], cursorBar)

# Selection Sort
def _selection_sort():
    global barList    
    global lengthList

    for i in range(len(lengthList)):
        min = i
        for j in range(i + 1, len(lengthList)):
            if(lengthList[j] < lengthList[min]):
                min = j
        lengthList[min], lengthList[i] = lengthList[i], lengthList[min]
        barList[min], barList[i] = barList[i], barList[min]
        swap(barList[min], barList[i])
        yield

def insertion_sort():
    global worker
    worker = _insertion_sort()
    animate()

def selection_sort():
    global worker
    worker = _selection_sort()
    animate()

def bubble_sort():
    global worker
    worker = _bubble_sort()
    animate()

def animate():
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(10, animate)
        except StopIteration:
            worker = None

def generate():
    global barList, lengthList
    canvas.delete('all')
    barstart, barend = 5, 15
    barList, lengthList = [], []

    for _ in range(1, 60):
        randomY = random.randint(1, 360)
        bar = canvas.create_rectangle(barstart, randomY, barend, 365, fill='yellow')
        barList.append(bar)
        barstart += 10
        barend += 10

    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        lengthList.append(length)

    for i in range(len(lengthList) - 1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='red')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='black')

window = tk.Tk()
window.title('Sorting Visualizer')
window.geometry('600x450')

canvas = tk.Canvas(window, width='600', height='400')
canvas.grid(column=0, row=0, columnspan=50)

insert = tk.Button(window, text='Insertion Sort', command=insertion_sort)
select = tk.Button(window, text='Selection Sort', command=selection_sort)
bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
shuf = tk.Button(window, text='Shuffle', command=generate)
insert.grid(column=1, row=1)
select.grid(column=2, row=1)
bubble.grid(column=3, row=1)
shuf.grid(column=0, row=1)

generate()
window.mainloop()
