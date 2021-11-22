from decimal import Decimal
from tkinter import *

from src.functions.basic import dividir, multiplicar, somar, subtrair
from src.functions.especial import exponencial, quadratica


def clear_all():
    global result, operation, result_lbl, parcial_lbl
    result = 0
    operation = ''
    result_lbl.config(text='')
    parcial_lbl.config(text='0')

def remove_last_digit():
    number = str(result_lbl.cget("text"))
    new_number = number[:-1]
    result_lbl.config(text=new_number)

def set_result_lbl(value):
    result_lbl.config(text = result_lbl.cget("text") + str(value))

def set_values(symbol, value):
    global operation, result
    if operation == '':
        operation = symbol
        result = value
        result_lbl.config(text='')
        parcial_lbl.config(text=result)
    else:
        resolve_basic_opr(operation, result, result_lbl.cget("text"))
        set_values(symbol, result_lbl.cget("text"))
        
def set_negative_value():
    try:
        positive = result_lbl.cget("text")
        negative = -abs(Decimal(positive))
        result_lbl.config(text=negative)
    except:
        pass

def resolve_especial_opr(comand, value_):
    if comand == 'x²':
        value = exponencial(Decimal(value_))
        result_lbl.config(text=round(value, 2))
        parcial_lbl.config(text=result_lbl.cget("text"))
    elif comand == 'Raizq':
        value = quadratica(Decimal(value_))
        result_lbl.config(text=round(value, 2))
        parcial_lbl.config(text=result_lbl.cget("text"))

def resolve_basic_opr(comand, value1, value2):
    value = 0
    try:
        if comand == "+":
            value = somar(Decimal(value1), Decimal(value2))
            result_lbl.config(text=round(value, 2))
            parcial_lbl.config(text=result_lbl.cget("text"))
        elif comand == "-":
            value = subtrair(Decimal(value1), Decimal(value2))
            result_lbl.config(text=round(value, 2))
            parcial_lbl.config(text=result_lbl.cget("text"))
        elif comand == "*":
            value = multiplicar(Decimal(value1), Decimal(value2))
            result_lbl.config(text=round(value, 2))
            parcial_lbl.config(text=result_lbl.cget("text"))
        elif comand == "/":
            value = dividir(Decimal(value1), Decimal(value2))
            result_lbl.config(text=round(value, 2))
            parcial_lbl.config(text=result_lbl.cget("text"))

    except:
        parcial_lbl.config(text='err')
    
    global operation
    operation = ''


LABEL_WIDTH = 15
LABEL_HEIGHT = 2
LABEL_FONT = "Arial, 24"
LABEL_COLOR_BG = '#2c3e50'
LABEL_COLOR_FG = 'white'
BUTTON_WIDTH = 10
BUTTON_FONT = "Arial, 14"
BUTTON_COLOR_BG = '#6a89cc'

result = 0
operation = ''


root = Tk()
root.title("Calculadora Python")

main_frm = Frame(root, bg='#2c3e50')
main_frm.grid()

result_lbl = Label(main_frm, text="", font=LABEL_FONT, width=LABEL_WIDTH, height=LABEL_HEIGHT, bg=LABEL_COLOR_BG, fg=LABEL_COLOR_FG)
result_lbl.grid(columnspan=4, column=0, row=0)
parcial_text_lbl = Label(main_frm, text="Ultima Parcial", font=BUTTON_FONT, width=BUTTON_WIDTH, height=2, bg=LABEL_COLOR_BG, fg=LABEL_COLOR_FG)
parcial_text_lbl.grid(column=1, row=1)
parcial_lbl = Label(main_frm, text="0", font=BUTTON_FONT, width=BUTTON_WIDTH, height=2, bg=LABEL_COLOR_BG, fg=LABEL_COLOR_FG)
parcial_lbl.grid(column=2, row=1)


btn9 = Button(main_frm, text="9", font=BUTTON_FONT,  width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(9))
btn9.grid(column=0, row=2)
btn8 = Button(main_frm, text="8", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(8))
btn8.grid(column=1, row=2)
btn7 = Button(main_frm, text="7", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(7))
btn7.grid(column=2, row=2)
btn6 = Button(main_frm, text="6", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(6))
btn6.grid(column=0, row=3)
btn5 = Button(main_frm, text="5", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(5))
btn5.grid(column=1, row=3)
btn4 = Button(main_frm, text="4", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(4))
btn4.grid(column=2, row=3)
btn3 = Button(main_frm, text="3", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(3))
btn3.grid(column=0, row=4)
btn2 = Button(main_frm, text="2", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(2))
btn2.grid(column=1, row=4)
btn1 = Button(main_frm, text="1", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(1))
btn1.grid(column=2, row=4)
btn0 = Button(main_frm, text="0", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl(0))
btn0.grid(column=1, row=5)

btnVirg = Button(main_frm, text=".", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_result_lbl("."))
btnVirg.grid(column=2, row=5)
btnMM = Button(main_frm, text="+/-", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_negative_value())
btnMM.grid(column=0, row=5)

btnApagar = Button(main_frm, text="<-", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: remove_last_digit())
btnApagar.grid(column=3, row=2)
btnSom = Button(main_frm, text="+", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_values(btnSom.cget("text"), result_lbl.cget("text")))
btnSom.grid(column=3, row=3)
btnSub = Button(main_frm, text="-", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_values(btnSub.cget("text"), result_lbl.cget("text")))
btnSub.grid(column=3, row=4)
btnDiv = Button(main_frm, text="/", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_values(btnDiv.cget("text"), result_lbl.cget("text")))
btnDiv.grid(column=3, row=5)
btnMult = Button(main_frm, text="*", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: set_values(btnMult.cget("text"), result_lbl.cget("text")))
btnMult.grid(column=3, row=6)
btnExpo = Button(main_frm, text="x²", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: resolve_especial_opr(btnExpo.cget("text"), result_lbl.cget("text")))
btnExpo.grid(column=0, row=6)
btnRaiz = Button(main_frm, text="Raizq", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: resolve_especial_opr(btnRaiz.cget("text"), result_lbl.cget("text")))
btnRaiz.grid(column=1, row=6)
btnIgual = Button(main_frm, text="=", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: resolve_basic_opr(operation, result, result_lbl.cget("text")))
btnIgual.grid(column=2, row=7)
btnLimparTudo = Button(main_frm, text="CE", font=BUTTON_FONT, width=BUTTON_WIDTH, bg=BUTTON_COLOR_BG, command=lambda: clear_all())
btnLimparTudo.grid(column=1, row=7)

main_frm.mainloop()
