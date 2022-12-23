import customtkinter
from PostMachine import PostMachine_class


class inter(customtkinter.CTk, PostMachine_class):
    """
    class App(customtkinter.CTk, PostMachine_class),
    наследует от customtkinter.CTk, PostMachine_class.

    Назначение - класс интерпретации, для работы
    с машиной Поста. В нем реализован весь необходимый интерфейс
    и логика работы
    """

    def __init__(self):
        """
        Выполняется всякий раз, когда из класса создаётся объект.
        Создаются все виджеты программы.
        """
        super().__init__()  # Функция super() позволяет наследовать базовые классы без необходимости явно ссылаться на базовый класс

        # инициализируем окно программы, задаем его размер, название, цветовую тему, и сетку размещения элементов
        self.title("Post Machine interpretator")
        self.geometry("1200x720")
        self.minsize(1200, 1000)
        self.maxsize(1200, 1000)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # окно разбито на три части
        # инициализируем первую часть(боковое меню). Создаем и размещаем все элементы в нем

        #############################################
        # фрейм один(меню)
        #############################################
        # создаём базовый фрейм и размещаем его в общем окне

        self.frame_menu = customtkinter.CTkFrame(self)
        self.frame_menu.grid(column=0, row=0, rowspan=4, padx=(15, 0), pady=15, sticky="NSEW")

        # Название приложения

        self.label_logo = customtkinter.CTkLabel(self.frame_menu, text="Post \nmachine \ninterpretator", font=("Segoe UI", 35),
                                                 compound="top", anchor="center")
        self.label_logo.grid(column=0, row=0, padx=20, pady=(20, 50), sticky="ew")

        # Кнопка очистки окон

        self.btn_reset_command = customtkinter.CTkButton(self.frame_menu, text="ОЧИСТИТЬ ОКНА", width=200, height=32,
                                                         font=("Segoe UI", 16), fg_color="#353535",
                                                         text_color="#888888", command=self._reset)
        self.btn_reset_command.grid(column=0, row=6, padx=20, pady=(0, 10), sticky="s")

        #############################################
        # фрейм два(реализованы виджеты ввода)
        #############################################

        # создаем второй фрейм на котором будут находиться все функции ввода.

        self.frame_inputConsole = customtkinter.CTkFrame(self, height=350)
        self.frame_inputConsole.grid(column=1, row=0, rowspan=1, padx=15, pady=(15, 0), sticky="NSEW")

        # заголовок Ввод программы

        self.headline_command_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=50, height=30,
                                                                     font=("Segoe UI", 20), activate_scrollbars=False,
                                                                     fg_color="#2B2B2B")
        self.headline_command_input_field.grid(row=0, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_command_input_field.insert("0.0", "Ввод программы")
        self.headline_command_input_field.configure(state="disabled")

        # поле ввода программы

        self.command_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=200, height=100,
                                                            font=("Segoe UI", 20), activate_scrollbars=True,
                                                            fg_color="#2f2f2f")
        self.command_input_field.grid(row=1, rowspan=3, column=0, padx=15, pady=(0, 20), sticky="NSEW")

        # заголовок Ввод начального состояния ленты

        self.headline_first_ribbon_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=50, height=20,
                                                                        font=("Segoe UI", 20),
                                                                        activate_scrollbars=False, fg_color="#2B2B2B")
        self.headline_first_ribbon_input_field.grid(row=0, column=1, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_first_ribbon_input_field.insert("0.0", "Ввод начального состояния ленты")
        self.headline_first_ribbon_input_field.configure(state="disabled")

        # поле ввода начального состояния ленты

        self.first_ribbon_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=400, height=100,
                                                               font=("Segoe UI", 20), activate_scrollbars=True,
                                                               fg_color="#2f2f2f")
        self.first_ribbon_input_field.grid(row=1, rowspan=2, column=1, padx=15, sticky="n")

        # кнопка начала выполнения программы

        self.btn_start = customtkinter.CTkButton(self.frame_inputConsole, text="Начать выполнение", width=300,
                                                 height=32, font=("Segoe UI", 16), fg_color="#2FA572",
                                                 text_color="#2B2B2B", command=self._start)
        self.btn_start.grid(column=0, row=5, padx=15, pady=(0, 20), sticky="nw")

        #############################################
        #############################################

        #############################################
        # фрейм три(реализованы виджеты вывода)
        #############################################

        # создаем и размещаем на нем все элементы вывода на 3 фрейме

        self.frame_outputConsole = customtkinter.CTkFrame(self)
        self.frame_outputConsole.grid(column=1, row=1, rowspan=2, padx=15, pady=100, sticky="NSEW")

        # заголовок Лента машины

        self.headline_ribbon = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,
                                                      font=("Segoe UI", 20), activate_scrollbars=False,
                                                      fg_color="#2B2B2B")
        self.headline_ribbon.grid(row=0, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_ribbon.insert("0.0", "Лента машины")
        self.headline_ribbon.configure(state="disabled")

        # окно вывода ленты

        self.output = customtkinter.CTkTextbox(self.frame_outputConsole, height=50, width=800, font=("Segoe UI", 20),
                                               activate_scrollbars=False)
        self.output.grid(row=1, column=0, padx=20, pady=(5, 5))
        self.output.configure(state="normal")
        self.output.insert("0.0",
                           '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        self.output.configure(state="disabled")

        # Каретка машины

        self.carriage_line = customtkinter.CTkSlider(self.frame_outputConsole, width=800, progress_color="#4A4D50")
        self.carriage_line.grid(row=2, column=0, padx=20)
        self.carriage_line.configure(state="disabled")

        # заголовок Команда (показывает на какой команде завершилось выполнение)

        self.headline_step = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,
                                                      font=("Segoe UI", 20), activate_scrollbars=False,
                                                      fg_color="#2B2B2B")
        self.headline_step.grid(row=3, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_step.insert("0.0", "Команда")
        self.headline_step.configure(state="disabled")

        # вывод последней команды (показывает на какой команде завершилось выполнение)

        self.step_out = customtkinter.CTkTextbox(self.frame_outputConsole, width=300, height=40,
                                                 font=("Segoe UI", 20),
                                                 activate_scrollbars=False)
        self.step_out.grid(row=4, padx=20, sticky="w")
        self.step_out.configure(state="disabled")

        # заголовок Результат выполнения

        self.headline_comp = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,
                                                      font=("Segoe UI", 20), activate_scrollbars=False,
                                                      fg_color="#2B2B2B")
        self.headline_comp.grid(row=5, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_comp.insert("0.0", "Результат выполнения")
        self.headline_comp.configure(state="disabled")

        # виджет результата выполнения

        self.rezult = customtkinter.CTkTextbox(self.frame_outputConsole, width=300, height=150, font=("Segoe UI", 20),
                                               activate_scrollbars=True)
        self.rezult.grid(row=6, column=0, pady=(0, 120), padx=20, sticky="NSEW")
        self.rezult.configure(state="disabled")

        #############################################
        #############################################




    def _corect_step(self, step1):
        """
        Метод проверяющий корректность номера выполняемой команды. В программе не может быть
        номеров с отрицательным значением или номеров больших,
        чем количество команд, или шагов в виде символов

        :param
        step1 номер выполняемой команды
        """
        if type(step1) != int:
            return False
        elif int(step1) <= 0:
            return False
        elif int(step1) > len(self.command_list):
            return False
        else:
            return True

    def _corect_input_ribbon(self, ribbon):
        """
        Метод проверяющий корректность начального состояния ленты машины, введенного
        пользователем. (В ленте не может быть что-то кроме 0 и 1 или пустоты)

        :param
        ribbon начальное состояние ленты
        """
        for i in ribbon:
            if i not in '01':
                return False
        return True

    def _reset(self):
        """
        Метод сбрасывающий весь контент виджетов, при нажатии на кнопку
        Нужен для подчистки памяти
        """
        self.output.configure(state="normal")
        self.output.delete('0.0', 'end')
        self.output.edit_reset()
        self.output.configure(state="disabled")

        self.step_out.configure(state="normal")
        self.step_out.delete('0.0', 'end')
        self.step_out.edit_reset()
        self.step_out.configure(state="disabled")

        self.rezult.configure(state="normal")
        self.rezult.delete('0.0', 'end')
        self.rezult.edit_reset()
        self.rezult.configure(state="disabled")

        self.command_input_field.configure(state="normal")
        self.command_input_field.configure()
        self.command_input_field.delete('0.0', "end")
        self.command_input_field.edit_reset()
        self.command_input_field.configure(state="disabled")

        self.first_ribbon_input_field.configure(state="normal")
        self.first_ribbon_input_field.delete('0.0', 'end')
        self.first_ribbon_input_field.edit_reset()
        self.first_ribbon_input_field.configure(state="disabled")

        if self.check_command_input_field.get() == 1:
            self.check_command_input_field.toggle()
        if self.check_first_ribbon_input_field.get() == 1:
            self.check_first_ribbon_input_field.toggle()

        self.output.configure(state="normal")
        self.output.insert("0.0",
                           '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        self.output.configure(state="disabled")

    def _start(self):
        """
        Метод описывающий работу машины и соединяющий возвращаемые значения, из класса
        PostMachine_class(), и интерфейс программы. Запускается при нажатии на кнопку
        "начать выполнение" в интерфейсе. Результатом работы данного метода является
        моделирование машины Поста выполняющую программу пользователя
        """

        # считываем список команд
        self.command_list = []  # список в котором хранятся все команды программы

        self.line_commands_str = self.command_input_field.get('0.0', 'end').split(
            '\n')  # переменная необходимая чтобы считать все команды из окна ввода програмыы и добавить их в self.comamnd_list

        self.command_list += self.line_commands_str

        # Убираем пробелы
        for i in range(len(self.command_list)):
            self.command_list[i] = self.command_list[i].replace(' ', '')
        self.command_list = self.command_list[:-1]

        # считываем изначальное состояние ленты
        self.first_ribbon_list = []  # список для начального состояние ленты, вводимое пользователем

        line_first_ribbon_str = self.first_ribbon_input_field.get('0.0', 'end').split(
            '\n')  # строковая переменная необходимая, чтобы считать начальное состояние ленты и занести его в self.first_tape_list
        line_first_ribbon_str = line_first_ribbon_str[:-1]
        for i in line_first_ribbon_str[0]:
            self.first_ribbon_list.append(i)
        self.first_ribbon_list += ['0'] * 30
        self.first_ribbon_list[:0] = ['0'] * 30

        # присваиваем индекс каретке машины
        self.carr = len(
            self.first_ribbon_list) // 2  # индекс каретке машины, вначале задаем ей положение в середине

        # инициализируем машину
        p_m = PostMachine_class(True, self.first_ribbon_list, self.carr)  # создаем объект из класса PostMachine_class()

        # делаем запуск
        work = True  # состояние машины
        step = 1  # номер выполняемой команды
        iter = 0  # шаг
        maxIter = 300  # максимальное кол-во шагов
        current_ribbon = []  # текущее состояние ленты

        # В первую очередь проверяем корректность ленты
        if self._corect_input_ribbon(self.first_ribbon_list):
            # пока состоянием машины True и программа не превысила максимальное количество шагов
            while work and iter <= maxIter:
                # проверяем корректность номера шага
                if self._corect_step(step):

                    current_command = self.command_list[step - 1][0]  # текущая команда

                    self.step_out.configure(state="normal")
                    self.step_out.delete("0.0", "end")
                    self.step_out.insert("0.0", self.command_list[step - 1])
                    self.step_out.insert("0.1", ': ')
                    self.step_out.insert("0.2", step)
                    self.step_out.configure(state="disabled")

                    ex = []  # список для хранения возвращаемых значений из функции command_function класса PostMachine_class
                    ex = p_m.command_function(current_command)

                    # В зависимости от возвращаемых значений проигрываем один из возможных сценариев
                    if ex != "Программа не может окончить свое выполнение в связи с ошибкой" and ex != "Программа окончила свое выполнение без ошибок" and ex != 11 and ex != 22:
                        current_ribbon, self.carr = ex[0], ex[1]

                        self.output.configure(state="normal")
                        self.output.delete("0.0", "end")
                        self.output.insert("0.0", current_ribbon[self.carr - 24:self.carr + 25])
                        self.output.configure(state="disabled")

                        step = int(self.command_list[step - 1][1:])  # номер шага

                    elif ex == 11 or ex == 22:
                        if ex == 11:
                            step = int(self.command_list[step - 1][
                                       self.command_list[step - 1].index('?') + 1:self.command_list[step - 1].index(
                                           ',')])

                        elif ex == 22:
                            step = int(self.command_list[step - 1][self.command_list[step - 1].index(',') + 1:])

                    elif ex == "Программа не может окончить свое выполнение в связи с ошибкой":
                        self.rezult.configure(state="normal")
                        self.rezult.insert("0.0",
                                           "-------------------------------------------------------------------------------------------------\n"
                                           "Программа не может окончить свое выполнение в связи с ошибкой\n"
                                           "-------------------------------------------------------------------------------------------------\n")
                        self.rezult.configure(state="disabled")

                        self.output.delete('1.0', "END")
                        self.output.edit_reset()

                        work = False


                    elif ex == "Программа окончила свое выполнение без ошибок":
                        self.rezult.configure(state="normal")
                        self.rezult.insert("0.0",
                                           "-------------------------------------------------------------------------------------------------\n"
                                           "Программа окончила свое выполнение без ошибок\n"
                                           "-------------------------------------------------------------------------------------------------\n")
                        self.rezult.configure(state="disabled")

                        self.output.delete('1.0', "END")
                        self.output.edit_reset()

                        work = False

                    iter += 1
                else:
                    self.rezult.configure(state="normal")
                    self.rezult.insert("0.0",
                                       "-------------------------------------------------------------------------------------------------\n"
                                       "Программа ссылается на несуществующую команду\n"
                                       "-------------------------------------------------------------------------------------------------\n")
                    self.rezult.configure(state="disabled")

                    self.output.delete('1.0', "END")
                    self.output.edit_reset()

                    work = False

                if iter > maxIter:
                    self.output.configure(state="normal")
                    self.output.delete("0.0", "end")
                    if self.carr >= len(current_ribbon) // 2:
                        self.output.insert("0.0",
                                           current_ribbon[0:49])
                    else:
                        self.output.insert("0.0", current_ribbon[0:49])

                    self.output.configure(state="disabled")

                    self.rezult.configure(state="normal")
                    self.rezult.insert("0.0",
                                       "-------------------------------------------------------------------------------------------------\n"
                                       "Программа зациклилась и превысила допустимое колличество шагов. Перепишите программу так, чтобы она выполнялась не боллее чем за 300 шагов\n"
                                       "Либо вы складывали/вычитали числа\n"
                                       "-------------------------------------------------------------------------------------------------\n")
                    self.rezult.configure(state="disabled")
                    work = False
        else:
            self.rezult.configure(state="normal")
            self.rezult.insert("0.0",
                               "-------------------------------------------------------------------------------------------------\n"
                               "Некоректный ввод начального состояния ленты\n"
                               "-------------------------------------------------------------------------------------------------\n")
            self.rezult.configure(state="disabled")
            work = False


if __name__ == "__main__":
    interpretation = inter()
    interpretation.mainloop()