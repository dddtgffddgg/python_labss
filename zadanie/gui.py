from tkinter import Tk, Label, Entry, Button
from calculations import calculate_area
from report_generator import generate_report

def create_gui():
    root = Tk()

    base_label = Label(root, text="Основание:")
    base_label.pack()

    height_label = Label(root, text="Высота:")
    height_label.pack()

    side_a_label = Label(root, text="Сторона А:")
    side_a_label.pack()

    side_b_label = Label(root, text="Сторона Б:")
    side_b_label.pack()

    base_entry = Entry(root)
    base_entry.pack()

    height_entry = Entry(root)
    height_entry.pack()

    side_a_entry = Entry(root)
    side_a_entry.pack()

    side_b_entry = Entry(root)
    side_b_entry.pack()

    result_label = Label(root)
    result_label.pack()

    calculate_button = Button(root, text="Рассчитать", command=lambda: calculate_area(base_entry.get(), height_entry.get(), side_a_entry.get(), side_b_entry.get(), result_label))
    calculate_button.pack()

    save_button = Button(root, text="Сохранить в отчёт", command=lambda: generate_report(base_entry.get(), height_entry.get(), side_a_entry.get(), side_b_entry.get()))
    save_button.pack()

    root.mainloop()

