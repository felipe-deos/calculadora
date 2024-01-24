from tkinter import*

def limparDisplay()-> None:
    display.delete(0,END)

def insert(valor: str)->None:
    display.insert(END,valor)

def calcularResultado()->None:
    textoDisplay=display.get()
    resultado=eval(textoDisplay)
    limparDisplay()
    insert(resultado)

janela=Tk()
janela.title("calculadora")

display=Entry(janela,bg="black", font="Tahoma 24", width=24,fg="white")
display.pack()

frame=Frame(janela)
frame.pack()

gray="#333333"
orange="#ff9500"
btn0=Button(frame, text="0", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6, command= lambda : insert(0))
btn1=Button(frame, text="1", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6, command= lambda : insert(1))
btn2=Button(frame, text="2", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert(2))
btn3=Button(frame, text="3", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert(3))
btn4=Button(frame, text="4", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert(4))
btn5=Button(frame, text="5", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert(5))
btn6=Button(frame, text="6", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert(6))
btn7=Button(frame, text="7", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert(7))
btn8=Button(frame, text="8", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert(8))
btn9=Button(frame, text="9", bg=gray, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert(9))
btnSomar=Button(frame, text="+", bg=orange, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert('+'))
btnSubtrair=Button(frame, text="-", bg=orange, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert('-'))
btnMultiplicar=Button(frame, text="*", bg=orange, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert('*'))
btnDividir=Button(frame, text="/", bg=orange, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert('/'))
btnPonto=Button(frame, text=".", bg=orange, fg="white", font="Tahoma 16 bold",
            height=5, width=6,command= lambda : insert('.'))
btnIgual=Button(frame, text="=", bg=orange, fg="white", font="Tahoma 16 bold",
            height=5, width=6, command=calcularResultado)
btnLimpar=Button(frame, text="C", bg=orange, fg="white", font="Tahoma 16 bold",
            height=5, width=6, command=limparDisplay)


btn7.grid(row=0,column=0)
btn8.grid(row=0,column=1)
btn9.grid(row=0,column=2)
btnSomar.grid(row=0,column=3)

btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btnSubtrair.grid(row=1,column=3)

btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=2,column=2)
btnMultiplicar.grid(row=2,column=3)

btn0.grid(row=3,column=0)
btnPonto.grid(row=3,column=1)
btnLimpar.grid(row=3,column=2)
btnIgual.grid(row=3,column=3)

janela.mainloop()