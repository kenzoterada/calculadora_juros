from tkinter import *

janela = Tk()
janela.title("Calculadora de Juros")

def juros_simples(valor, juros, meses):
    valor_ajustado = valor
    i = int(0)
    while i < meses:
        valor_ajustado += valor*(juros/100)
        i+=1
    return valor_ajustado

def juros_compostos(valor, juros, meses):
    i = int(0)
    valor_ajustado = valor
    while i < meses:
        valor_ajustado = valor_ajustado + valor*(juros/100)
        valor = valor + valor*(juros/100)
        i = i+1
    return valor_ajustado

Label(janela, text="Valor Inicial: ").grid(row=0, column=0)
entrada_valor_inicial = Entry(janela)
entrada_valor_inicial.grid(row=0, column=1)

Label(janela, text="Juros em %: ").grid(row=1, column=0)
juros_em_porcentagem = Entry(janela)
juros_em_porcentagem.grid(row=1, column=1)

Label(janela, text="Tempo em meses: ").grid(row=2, column=0)
tempo_em_meses = Entry(janela)
tempo_em_meses.grid(row=2, column=1)

def juros_simples_com_dados():
    valor_fornecido = float(entrada_valor_inicial.get())
    juros_fornecidos = float(juros_em_porcentagem.get())
    meses_forcenidos = float(tempo_em_meses.get())
    try:
        resultado = "%.2f" % juros_simples(valor_fornecido, juros_fornecidos, meses_forcenidos)
        messege = f"Juros Simples: R$ {resultado}"
        mensagem.set(messege)
    except ValueError:
        mensagem.set('você não digitou números :(')

def juros_compostos_com_dados():
    valor_fornecido = float(entrada_valor_inicial.get())
    juros_fornecidos = float(juros_em_porcentagem.get())
    meses_forcenidos = float(tempo_em_meses.get())
    try:
        resultado = "%.2f" % juros_compostos(valor_fornecido, juros_fornecidos, meses_forcenidos)
        messege = f"Juros Compostos: R$ {resultado}"
        mensagem.set(messege)
    except ValueError:
        mensagem.set('você não digitou números :(')


botao_simples = Button(janela, text='Calcular Juros Simples', command=juros_simples_com_dados)
botao_simples.grid(row=3, column=0)

botao_compostos = Button(janela, text='Calcular Juros Compostos', command=juros_compostos_com_dados)
botao_compostos.grid(row=3, column=1)

mensagem = StringVar()
mensagem.set('')
resultado = Label(janela, textvariable=mensagem)
resultado.grid(row=4, column=0, columnspan=2)

janela.mainloop()


