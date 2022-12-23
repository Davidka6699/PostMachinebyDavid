import pytest
from PostMachine import PostMachine_class


def test_get_state():
    pm = PostMachine_class(False, [0]*60, 30)
    assert pm.get_state() == False

    pm = PostMachine_class(True, [0] * 60, 30)
    assert pm.get_state() == True

def test_get_ribbon_list():
    pm = PostMachine_class(False, [0]*20, 30)
    assert pm.get_ribbon_list() == [0]*20

    pm = PostMachine_class(True, "aa", 30)
    assert pm.get_ribbon_list() == "aa"

    pm = PostMachine_class(True, None, 30)
    assert pm.get_ribbon_list() == None

def test_get_carriage():
    pm = PostMachine_class(False, [0] * 20, 2)
    assert pm.get_carriage() == 2

    pm = PostMachine_class(True, "aa", 1)
    assert pm.get_carriage() == 1

    pm = PostMachine_class(True, None, 30)
    assert pm.get_carriage() == 30

def test_can_do_command():
    pm = PostMachine_class(True, ['1']*100, 30)
    command = 'V'
    assert pm._can_do_command(command) == False

    pm = PostMachine_class(True, ['0'] * 100, 30)
    command = 'V'
    assert pm._can_do_command(command) == True

    pm = PostMachine_class(True, ['1'] * 100, 30)
    command = 'X'
    assert pm._can_do_command(command) == True

    pm = PostMachine_class(True, ['0'] * 100, 30)
    command = 'X'
    assert pm._can_do_command(command) == False

    pm = PostMachine_class(True, ['0'] * 100, 30)
    command = 'k'
    assert pm._can_do_command(command) == False

    pm = PostMachine_class(True, ['0'] * 100, 30)
    command = '*'
    assert pm._can_do_command(command) == False


def test_ribbon_extension():
    pm = PostMachine_class(True, ['1'] * 100, len(['1'] * 100)-1)
    assert pm.ribbon_extension() ==  ['1'] * 100 + ['0']*33

    pm = PostMachine_class(True, ['0'] * 100, len(['0'] * 100) - 1)
    assert pm.ribbon_extension() == ['0'] * 33 + ['0'] * 100

def test_command_function():
    ribbon1 = ['1'] * 100
    wrh = len(ribbon1)//2
    pm = PostMachine_class(True, ribbon1, wrh)
    command = 'V'
    assert pm.command_function(command) == "Программа не может окончить свое выполнение в связи с ошибкой"


    ribbon1 = ['0'] * 60
    wrh = len(ribbon1)//2
    pm = PostMachine_class(True, ['0']*60, wrh)
    command = 'V'
    ex = ribbon1
    ex[wrh] = '1'
    assert pm.command_function(command) == (ex, wrh)


    ribbon1 = ['0'] * 100
    wrh = len(ribbon1) // 2
    pm = PostMachine_class(True, ribbon1, wrh)
    command = 'X'
    assert pm.command_function(command) == "Программа не может окончить свое выполнение в связи с ошибкой"


    ribbon1 = ['1'] * 100
    wrh = len(ribbon1) // 2
    pm = PostMachine_class(True, ['1'] * 100, wrh)
    command = 'X'
    ex = ribbon1
    ex[wrh] = '0'
    assert pm.command_function(command) == (ex, wrh)

    ribbon1 = ['0'] * 100
    wrh = len(ribbon1) // 2
    pm = PostMachine_class(True, ribbon1, wrh)
    command = 's'
    assert pm.command_function(command) == "Программа окончила свое выполнение без ошибок"

    ribbon1 = ['0'] * 100
    wrh = len(ribbon1) // 2
    pm = PostMachine_class(True, ribbon1, wrh)
    command = '?'
    assert pm.command_function(command) == 11

    ribbon1 = ['1'] * 100
    wrh = len(ribbon1) // 2
    pm = PostMachine_class(True, ribbon1, wrh)
    command = '?'
    assert pm.command_function(command) == 22

    ribbon1 = ['1'] * 100
    wrh = len(ribbon1)-1
    pm = PostMachine_class(True, ribbon1, wrh)
    command = '>'
    assert pm.command_function(command) == (['1'] * 100 + ['0']*33, wrh+1)

    ribbon1 = ['1'] * 100
    wrh = 0
    pm = PostMachine_class(True, ribbon1, wrh)
    command = '>'
    assert pm.command_function(command) == (['1'] * 100, wrh + 1)

    ribbon1 = ['1'] * 100
    wrh = 0
    pm = PostMachine_class(True, ribbon1, wrh)
    command = '<'
    assert pm.command_function(command) == (['0']*33 + ['1'] * 100, 30)

    ribbon1 = ['1'] * 100
    wrh = len(ribbon1)//2
    pm = PostMachine_class(True, ribbon1, wrh)
    command = '<'
    assert pm.command_function(command) == (['1'] * 100, wrh-1)

