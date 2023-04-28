from tkinter import *

janela = Tk()
janela.title("Calculadora de Juros")

#função para converter os dados para ponto flutuante
def converte_float(n1,n2,n3):
    valor1 = float(n1)
    valor2 = float(n2)
    valor3 = float(n3)
    return valor1, valor2, valor3

#função para calculo de juros simples, usando a função converte_float
def juros_simples(valor, juros, meses):
    i = int(0)
    try:
        valor = converte_float(valor, juros, meses)[0]
        juros = converte_float(valor, juros, meses)[1]
        meses = converte_float(valor, juros, meses)[2]
        valor_ajustado = valor
        while i < meses:
            valor_ajustado += (valor*(juros/100))
            i+=1
        return valor_ajustado
    except (ValueError, TypeError) as erro:
        return str("voce não digitou numeros :(")

#função para calculo de juros compostos, usando a função converte_float
def juros_compostos(valor, juros, meses):
    i = int(0)
    try:
        valor = converte_float(valor, juros, meses)[0]
        juros = converte_float(valor, juros, meses)[1]
        meses = converte_float(valor, juros, meses)[2]
        valor_ajustado = valor
        while i < meses:
            valor_ajustado = valor_ajustado + valor*(juros/100)
            valor = valor + valor*(juros/100)
            i = i+1
        return valor_ajustado
    except (ValueError, TypeError) as erro:
        return str("voce não digitou numeros :(")

#texto e local para o usuário saber onde que deve ser inserido o valor inicial
Label(janela, text="Valor Inicial: ").grid(row=0, column=0)
entrada_valor_inicial = Entry(janela)
entrada_valor_inicial.grid(row=0, column=1)

#texto e local para o usuário saber onde que deve ser inserido a quantidade de juros
Label(janela, text="Juros em %: ").grid(row=1, column=0)
juros_em_porcentagem = Entry(janela)
juros_em_porcentagem.grid(row=1, column=1)

#texto e local para o usuário saber onde que deve ser inserido a quantidade de meses
Label(janela, text="Tempo em meses: ").grid(row=2, column=0)
tempo_em_meses = Entry(janela)
tempo_em_meses.grid(row=2, column=1)

#função que pega os dados da entrada para calculo do juros simples, chamando a função juros_simples
def juros_simples_com_dados():
    valor_fornecido = (entrada_valor_inicial.get())
    juros_fornecidos = (juros_em_porcentagem.get())
    meses_forcenidos = (tempo_em_meses.get())
    retornado = juros_simples(valor_fornecido, juros_fornecidos, meses_forcenidos)

    try:
        resultado = "%.2f" % retornado
        messege = f"Juros Simples: R$ {resultado}"
        mensagem.set(messege)
    except (ValueError, TypeError) as erro:
        mensagem.set(retornado)

#função que pega os dados da entrada para calculo do juros compostos, chamando a função juros_compostos
def juros_compostos_com_dados():
    valor_fornecido = (entrada_valor_inicial.get())
    juros_fornecidos = (juros_em_porcentagem.get())
    meses_forcenidos = (tempo_em_meses.get())
    retornado = juros_simples(valor_fornecido, juros_fornecidos, meses_forcenidos)
    try:
        resultado = "%.2f" % juros_compostos(valor_fornecido, juros_fornecidos, meses_forcenidos)
        messege = f"Juros Compostos: R$ {resultado}"
        mensagem.set(messege)
    except (ValueError, TypeError) as erro:
        mensagem.set(retornado)


#os seguintes botões são para o usuário escolher dentre as duas opções qual ele quer 
botao_simples = Button(janela, text='Calcular Juros Simples', command=juros_simples_com_dados)
botao_simples.grid(row=3, column=0)

botao_compostos = Button(janela, text='Calcular Juros Compostos', command=juros_compostos_com_dados)
botao_compostos.grid(row=3, column=1)

#local centralizado o qual aparece o resultado caso ele digite um número ou a mensagem de erro
mensagem = StringVar()
mensagem.set('')
resultado = Label(janela, textvariable=mensagem)
resultado.grid(row=4, column=0, columnspan=2)

janela.mainloop()
