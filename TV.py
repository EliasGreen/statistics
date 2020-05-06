from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

from DefaultGenerator import DefaultGenerator

# --------------------------------
# Главный класс - приложение
# --------------------------------
class App(object):
    def __init__(self, master, **kwargs):
        self.master = master

        # Добавление главной картинки
        self.canvas = Canvas(root, width=256, height=188)
        self.canvas.place(relx=.5, rely=.3, anchor="c")
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\Roman\\Desktop\\-8xHIWHRl5Y.jpg"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)

        # Начальные графические параметры главного экрана приложения
        master.title("Генератор типовых расчетов по предмету 'Теория вероятности'")
        master.configure(background='gray')
        master.geometry('600x450')

        # Label кол-ва вариантов
        vars_count_label = Label(text="Введите количество вариантов для генерации:")
        vars_count_label.place(relx=.5, rely=.6, anchor="c")

        # Input кол-ва вариантов
        self.vars_count = StringVar()
        vars_count_entry = Entry(textvariable=self.vars_count)
        vars_count_entry.place(relx=.5, rely=.66, anchor="c")

        # Кнопка обработки генерации вариантов
        vars_gen_button = Button(text="Сгенерировать варианты", command=self.generate_variants)
        vars_gen_button.place(relx=.5, rely=.8, anchor="c")

        # Кнопка обработки показа вариантов
        vars_del_button = Button(text="Открыть папку с вариантами", command=self.show_docx_variants)
        vars_del_button.place(relx=.5, rely=.9, anchor="c")

    # Вспомогательная функция вывода информации об успешности генерации вариантов
    def show_gen_results(self):
        if self.vars_count.get() == '' :
            messagebox.showerror("Безуспешная генерация\n ",
                                "Вы не ввели количество вариантов для генерации")
            return False

        try:
            count = int(self.vars_count.get())
        except Exception as exp:
            messagebox.showinfo("Безуспешная генерация\n",
                                "Ввод не является числом!")
            return False

        if self.vars_count.get() != '' and count > 0:
            messagebox.showinfo("Успешная генерация\n ",
                                   "Сгенерированные варианты находятся в "
                                   "одной папке с программой.\n"
                                   "Количество сгенерированных вариантов: " + self.vars_count.get())
            return True
        elif self.vars_count.get() != '' and count <= 0:
            messagebox.showerror("Безуспешная генерация\n ",
                                "Количество вариантов для генерации "
                                "должно быть больше нуля")
            return False

    # Метод запуска генерации объектов
    def generate_variants(self):
        if self.show_gen_results():
            count = int(self.vars_count.get()) # Исключения проверены выше

            for i in range(1, count + 1):
                DefaultGenerator([i for i in range(1, 19)], i, f"Типовой_вариант_{i}")

    # Метод открытия папки с вариантами
    def show_docx_variants(self):
        os.system('explorer ' + os.path.dirname(os.path.abspath(__file__)))


root = Tk()
app = App(root)
root.mainloop()
