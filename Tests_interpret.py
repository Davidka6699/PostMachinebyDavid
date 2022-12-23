import pytest
from interpret import inter

def test_correct_input_ribbon():
    app = inter()
    ribbon1 = ['0']*20
    assert app._correct_input_ribbon(ribbon1) == True

    app = inter()
    ribbon1 = ['1'] * 20
    assert app._correct_input_ribbon(ribbon1) == True

    app = inter()
    ribbon1 = ['01'] * 20
    assert app._correct_input_ribbon(ribbon1) == True

    app = inter()
    ribbon1 = ['7'] * 20
    assert app._correct_input_ribbon(ribbon1) == False

    app = inter()
    ribbon1 = ['*'] * 20
    assert app._correct_input_ribbon(ribbon1) == False

def test_correct_step():
    app = inter()
    app.command_list=['V2', 's2']
    step = 0
    assert app._correct_step(step) == False

    step = 1
    assert app._correct_step(step) == True

    step = 2
    assert app._correct_step(step) == True

    step = 3
    assert app._correct_step(step) == False

    step = '!'
    assert app._correct_step(step) == False

    step = 'd'
    assert app._correct_step(step) == False

