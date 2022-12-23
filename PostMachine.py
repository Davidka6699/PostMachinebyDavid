class PostMachine_class():
    """
    class PostMachine_class()
    Моделирует работу машины
    посредством обработки текущих команд, возвращает обновленную
    ленту и ошибки в случае невозможности выполнения программы
    """

    def __init__(self, state, ribbon_list, carriage):
        """
        __init__(self, state, ribbon_list, carriage)
        Выполняется всякий раз, когда из класса создаётся объект.
        Используется для инициализации переменных класса.
        -------------------------------------------------------------
        params:
        state - состояние машины (True - работает. False - не работает)
        ribbon_list - лента машины
        carriage - индекс каретки на ленте
        """

        self.state = state
        self.ribbon_list = ribbon_list
        self.carriage = carriage

    def get_state(self):
        """
        Функция возвращающая состояние машины
        """

        return self.state

    def get_ribbon_list(self):
        """
        Функция возвращающая ленту машины
        """

        return self.ribbon_list

    def get_carriage(self):
        """
        Функция возвращающая индекс пишущей головки машины
        """

        return self.carriage

    def _can_do_command(self, current_command):
        """
        Функция определяющая возможность выполнения той или иной команды
        поступившей машине

        params:
        current_command текущая команда
        """

        # проверяем возможность выполнения команды согласно правилам работы машины
        # (невозможно поставить метку в непустое поле, как и убрать метку из пустого)
        # проверяемрй командой не может быть символ кроме v и -
        if self.ribbon_list[self.carriage] == '1' and current_command == 'V':
            return False
        elif self.ribbon_list[self.carriage] == '0' and current_command == 'X':
            return False
        elif current_command != 'V' and current_command != 'X':
            return False
        else:
            return True

    def ribbon_extension(self):
        """
        Функция удлиняющая ленту в случае необходимости
        (головка машины дошла до одного из краев)
        """

        # расширяем ленту, если доходим до одного из ее концов
        if self.carriage == len(self.ribbon_list) - 1:
            self.ribbon_list += ['0'] * 33
        elif self.carriage == 0:
            self.ribbon_list[:0] = ['0'] * 33

        return self.ribbon_list



    def command_function(self, current_command):
        """
        Основная функция класса, моделирующая выполнение команд
        :params
        current_command текущая команда
        -------------------------------------------------------------
        Return
        В случае если команду можно выполнить и она не является командой
        остановки, метод вернет
        self.ribbon_list, self.carriage

        В случае если команду можно выполнить и она является командой
        остановки, метод вернет
        "Программа окончила свое выполнение без ошибок"

        В случае если команду нельзя выполнить, метод вернет
        "Программа не может окончить свое выполнение в связи с ошибкой"
        """

        #инициализируем поступившую программу и возможность ее выполнения,
        #после чего приступаем к ее реализации
        if current_command == 'V' and self._can_do_command(current_command):
            self.ribbon_list[self.carriage] = '1'

            return self.ribbon_list, self.carriage

        elif current_command == 'X' and self._can_do_command(current_command):
            self.ribbon_list[self.carriage] = '0'

            return self.ribbon_list, self.carriage

        elif current_command == '>':
            if self.carriage == len(self.ribbon_list)-1:
                self.ribbon_list = self.ribbon_extension()
            self.carriage += 1

            return self.ribbon_list, self.carriage

        elif current_command == '<':
            if self.carriage == 0:
                self.ribbon_list = self.ribbon_extension()
                self.carriage = 30
            else:
                self.carriage -= 1

            return self.ribbon_list, self.carriage

        elif current_command == 's':

            return "Программа окончила свое выполнение без ошибок"

        elif current_command == '?':
            if self.ribbon_list[self.carriage] == '1':
                return 22
            if self.ribbon_list[self.carriage] == '0':
                return 11
        #в случае ошибки, возвращаем не новую ленту и индекс головки, а ошибку
        elif not self._can_do_command(current_command):

            return "Программа не может окончить свое выполнение в связи с ошибкой"