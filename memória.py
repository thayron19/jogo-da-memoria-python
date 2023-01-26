import tkinter as tk              # para criar a janela
import keyboard as kb             # para usar o ESC para fechar a janela
import random as rd               # para usar números aleatórios
import tkinter.messagebox as tkm  # para mostrar o resultado
# ---------------------------------------------------------------------------------------------------------------------
# variaveis usadas como globais nas funções
lista = list(rd.sample([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 16))  # cria uma lista aleatoria

escolha_1 = 0  # pega a primeira escolha do jogador
posicao_1 = 0  # guarda a primeira posição do user para ser comparada com a segunda
cancel = ''    # variavel controle para evitar que seja criado sobrepostos nos cronometros
cancel2 = ''   # variavel controle para evitar que seja criado sobrepostos nos cronometros
fim = 0        # variavel para parar o cronometro


# ---------------------------------------------------------------------------------------------------------------------
def escolha(escolhido):  # recebe a escolha do jogador, marca o quadrado e desabilita

    global lista

    match escolhido:
        case 1:
            um_btn['text'] = lista[0]      # coloca o número da lista no botão
            um_btn['state'] = tk.DISABLED  # desabilita o botão pressionado
            comparar(lista[0], 1)          # chama a função e envia o número da lista + a posição do botão
        case 2:
            dois_btn['text'] = lista[1]
            dois_btn['state'] = tk.DISABLED
            comparar(lista[1], 2)
        case 3:
            tres_btn['text'] = lista[2]
            tres_btn['state'] = tk.DISABLED
            comparar(lista[2], 3)
        case 4:
            quatro_btn['text'] = lista[3]
            quatro_btn['state'] = tk.DISABLED
            comparar(lista[3], 4)
        case 5:
            cinco_btn['text'] = lista[4]
            cinco_btn['state'] = tk.DISABLED
            comparar(lista[4], 5)
        case 6:
            seis_btn['text'] = lista[5]
            seis_btn['state'] = tk.DISABLED
            comparar(lista[5], 6)
        case 7:
            sete_btn['text'] = lista[6]
            sete_btn['state'] = tk.DISABLED
            comparar(lista[6], 7)
        case 8:
            oito_btn['text'] = lista[7]
            oito_btn['state'] = tk.DISABLED
            comparar(lista[7], 8)
        case 9:
            nove_btn['text'] = lista[8]
            nove_btn['state'] = tk.DISABLED
            comparar(lista[8], 9)
        case 10:
            dez_btn['text'] = lista[9]
            dez_btn['state'] = tk.DISABLED
            comparar(lista[9], 10)
        case 11:
            onze_btn['text'] = lista[10]
            onze_btn['state'] = tk.DISABLED
            comparar(lista[10], 11)
        case 12:
            doze_btn['text'] = lista[11]
            doze_btn['state'] = tk.DISABLED
            comparar(lista[11], 12)
        case 13:
            treze_btn['text'] = lista[12]
            treze_btn['state'] = tk.DISABLED
            comparar(lista[12], 13)
        case 14:
            quatorze_btn['text'] = lista[13]
            quatorze_btn['state'] = tk.DISABLED
            comparar(lista[13], 14)
        case 15:
            quinze_btn['text'] = lista[14]
            quinze_btn['state'] = tk.DISABLED
            comparar(lista[14], 15)
        case 16:
            dezesseis_btn['text'] = lista[15]
            dezesseis_btn['state'] = tk.DISABLED
            comparar(lista[15], 16)


# ---------------------------------------------------------------------------------------------------------------------
def comparar(num, botao):  # é a função que compara os dois quadrados

    global escolha_1
    global posicao_1
    global fim

    if escolha_1 == 0:     # cai nesse if quando é a primeira escolha
        escolha_1 = num    # guardar o primeiro número
        posicao_1 = botao  # guarda a primeira posição
    else:                  # cai aqui quando é a segunda escolha

        if escolha_1 != num:  # compara a primeira escolha com a segunda
            escolha_1 = 0     # quando as escolhas são erradas, zera a variavel

            if cancel != '':                 # esse if evita criar sobrepostos
                janela.after_cancel(cancel)  # se o cancel não estiver vazio, ele cancela o contador

            cronometro(1, posicao_1, botao)  # função que conta 1 segundo depois zera os quadrados

        else:
            escolha_1 = 0  # se acertar os dois valores, só zera a variavel
            fim += 1       # acumula a quantida de jogos certos até oito e para o 'cronometro 2'


# ---------------------------------------------------------------------------------------------------------------------
def cronometro(sec, p1, p2):  # cronometro usado para dar um tempo antes de apagar os valores

    global cancel  # global para controle, ela evita que seja criado sobrepostos

    if sec == 0:        # quando tempo zera ele limpa os dois botões escolhidos erradamente
        limpa_dois(p1)  # envia para a função o botão foi selecionado errado para liberar o quadrado
        limpa_dois(p2)  # envia para a função o botão foi selecionado errado para liberar o quadrado

        if um_btn['text'] == '':         # se a variavel do botão está vazia liberar para jogo novamente
            um_btn['state'] = tk.NORMAL  # muda o estado do botão para normal

        if dois_btn['text'] == '':
            dois_btn['state'] = tk.NORMAL

        if tres_btn['text'] == '':
            tres_btn['state'] = tk.NORMAL

        if quatro_btn['text'] == '':
            quatro_btn['state'] = tk.NORMAL

        if cinco_btn['text'] == '':
            cinco_btn['state'] = tk.NORMAL

        if seis_btn['text'] == '':
            seis_btn['state'] = tk.NORMAL

        if sete_btn['text'] == '':
            sete_btn['state'] = tk.NORMAL

        if oito_btn['text'] == '':
            oito_btn['state'] = tk.NORMAL

        if nove_btn['text'] == '':
            nove_btn['state'] = tk.NORMAL

        if dez_btn['text'] == '':
            dez_btn['state'] = tk.NORMAL

        if onze_btn['text'] == '':
            onze_btn['state'] = tk.NORMAL

        if doze_btn['text'] == '':
            doze_btn['state'] = tk.NORMAL

        if treze_btn['text'] == '':
            treze_btn['state'] = tk.NORMAL

        if quatorze_btn['text'] == '':
            quatorze_btn['state'] = tk.NORMAL

        if quinze_btn['text'] == '':
            quinze_btn['state'] = tk.NORMAL

        if dezesseis_btn['text'] == '':
            dezesseis_btn['state'] = tk.NORMAL

    else:
        sec = sec - 1  # se dois quadrados forem errados, ele conta 1 segundo e desabilita todos os botões
        cancel = janela.after(1000, lambda: cronometro(sec, p1, p2))  # função de espera do tkinter

        um_btn['state'] = tk.DISABLED  # muda o estado do botão para desabilitado
        dois_btn['state'] = tk.DISABLED
        tres_btn['state'] = tk.DISABLED
        quatro_btn['state'] = tk.DISABLED
        cinco_btn['state'] = tk.DISABLED
        seis_btn['state'] = tk.DISABLED
        sete_btn['state'] = tk.DISABLED
        oito_btn['state'] = tk.DISABLED
        nove_btn['state'] = tk.DISABLED
        dez_btn['state'] = tk.DISABLED
        onze_btn['state'] = tk.DISABLED
        doze_btn['state'] = tk.DISABLED
        treze_btn['state'] = tk.DISABLED
        quatorze_btn['state'] = tk.DISABLED
        quinze_btn['state'] = tk.DISABLED
        dezesseis_btn['state'] = tk.DISABLED


# ---------------------------------------------------------------------------------------------------------------------
def cronometro2(sec2):  # cronometro que mostra o tempo na tela

    global cancel2  # global para controle, ela evita que seja criado sobrepostos
    global fim

    if fim == 8:  # variavel acumula até oito e para o cronometro
        janela.after_cancel(cancel2)  # para o cronometro
    else:
        tempo_texto['text'] = 'Tempo: ' + str(sec2) + ' segundo(s)'  # elemento que recebe o resultado na tela
        sec2 = sec2 + 1                                              # acumulador
        cancel2 = janela.after(1000, lambda: cronometro2(sec2))      # função de espera do tkinter


# ---------------------------------------------------------------------------------------------------------------------
def limpa_dois(limpar):  # usada para limpar os dois quadrados escolhidos erradamente

    match limpar:
        case 1:
            um_btn['text'] = ''          # esvazia o quadrado que foi selecionado errado
            um_btn['state'] = tk.NORMAL  # deixa ele normal para poder ser escolhido novamente
        case 2:
            dois_btn['text'] = ''
            dois_btn['state'] = tk.NORMAL
        case 3:
            tres_btn['text'] = ''
            tres_btn['state'] = tk.NORMAL
        case 4:
            quatro_btn['text'] = ''
            quatro_btn['state'] = tk.NORMAL
        case 5:
            cinco_btn['text'] = ''
            cinco_btn['state'] = tk.NORMAL
        case 6:
            seis_btn['text'] = ''
            seis_btn['state'] = tk.NORMAL
        case 7:
            sete_btn['text'] = ''
            sete_btn['state'] = tk.NORMAL
        case 8:
            oito_btn['text'] = ''
            oito_btn['state'] = tk.NORMAL
        case 9:
            nove_btn['text'] = ''
            nove_btn['state'] = tk.NORMAL
        case 10:
            dez_btn['text'] = ''
            dez_btn['state'] = tk.NORMAL
        case 11:
            onze_btn['text'] = ''
            onze_btn['state'] = tk.NORMAL
        case 12:
            doze_btn['text'] = ''
            doze_btn['state'] = tk.NORMAL
        case 13:
            treze_btn['text'] = ''
            treze_btn['state'] = tk.NORMAL
        case 14:
            quatorze_btn['text'] = ''
            quatorze_btn['state'] = tk.NORMAL
        case 15:
            quinze_btn['text'] = ''
            quinze_btn['state'] = tk.NORMAL
        case 16:
            dezesseis_btn['text'] = ''
            dezesseis_btn['state'] = tk.NORMAL


# ---------------------------------------------------------------------------------------------------------------------
def limpa():  # para reiniciar o jogo

    global lista
    global escolha_1
    global posicao_1
    global fim

    # esvazia os quadrados
    um_btn['text'] = ''
    dois_btn['text'] = ''
    tres_btn['text'] = ''
    quatro_btn['text'] = ''
    cinco_btn['text'] = ''
    seis_btn['text'] = ''
    sete_btn['text'] = ''
    oito_btn['text'] = ''
    nove_btn['text'] = ''
    dez_btn['text'] = ''
    onze_btn['text'] = ''
    doze_btn['text'] = ''
    treze_btn['text'] = ''
    quatorze_btn['text'] = ''
    quinze_btn['text'] = ''
    dezesseis_btn['text'] = ''

    # reabilita os botões
    um_btn['state'] = tk.NORMAL
    dois_btn['state'] = tk.NORMAL
    tres_btn['state'] = tk.NORMAL
    quatro_btn['state'] = tk.NORMAL
    cinco_btn['state'] = tk.NORMAL
    seis_btn['state'] = tk.NORMAL
    sete_btn['state'] = tk.NORMAL
    oito_btn['state'] = tk.NORMAL
    nove_btn['state'] = tk.NORMAL
    dez_btn['state'] = tk.NORMAL
    onze_btn['state'] = tk.NORMAL
    doze_btn['state'] = tk.NORMAL
    treze_btn['state'] = tk.NORMAL
    quatorze_btn['state'] = tk.NORMAL
    quinze_btn['state'] = tk.NORMAL
    dezesseis_btn['state'] = tk.NORMAL

    # recria a lista para o novo jogo e zera as variaveis
    lista = rd.sample([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 16)
    escolha_1 = 0
    posicao_1 = 0

    # zera o cronometro
    fim = 0

    if cancel2 != '':                 # esse if evita criar sobrepostos
        janela.after_cancel(cancel2)  # se o cancel não estiver vazio, ele cancela o contador

    cronometro2(0)                    # reinicia o cronometro


# ---------------------------------------------------------------------------------------------------------------------
def mostra():  # função para mostrar a resposta

    matriz = ''  # string para acumular os itens da lista

    for i, x in enumerate(lista):
        matriz += str(x) + ' '           # acumula e da espaço
        if i == 3 or i == 7 or i == 11:  # nas posições ele pula a linha
            matriz += '\n'

    tkm.showinfo('Resposta', matriz)  # mostra num alerta


# ---------------------------------------------------------------------------------------------------------------------
# criação e configuração da janela
janela = tk.Tk()                             # cria o objeto janela
janela.resizable(width=False, height=False)  # desativa a mudança de tamanho
janela.title('Memória')

# tamanho: 325X250, posição: calula e posiciona
janela.geometry("%dx%d%d%d" % (250, 310, float(250 / 2 - janela.winfo_screenwidth() / 2),
                               float(310 / 2 - janela.winfo_screenheight() / 2)))
# ---------------------------------------------------------------------------------------------------------------------
url_texto = tk.Label(janela, text='Jogo da memória', font=('', 10))  # título da janela
url_texto.place(x=10, y=10)                                          # posição do objeto
# ---------------------------------------------------------------------------------------------------------------------
con_txt_btn = tk.Button(janela, text='Limpar', command=lambda: limpa())  # criando objeto botão, reinicia o jogo
con_txt_btn.place(x=130, y=10, width=50)                                 # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
con_txt_btn = tk.Button(janela, text='Mostra', command=lambda: mostra())  # criando objeto botão, mostrar a resposta
con_txt_btn.place(x=190, y=10, width=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
um_btn = tk.Button(janela, text='', command=lambda: escolha(1), font=('', 30))  # criando objeto botão
um_btn.place(x=10, y=40, width=50, height=50)                                   # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
dois_btn = tk.Button(janela, text='', command=lambda: escolha(2), font=('', 30))  # criando objeto botão
dois_btn.place(x=70, y=40, width=50, height=50)                                   # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
tres_btn = tk.Button(janela, text='', command=lambda: escolha(3), font=('', 30))  # criando objeto botão
tres_btn.place(x=130, y=40, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
quatro_btn = tk.Button(janela, text='', command=lambda: escolha(4), font=('', 30))  # criando objeto botão
quatro_btn.place(x=190, y=40, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
cinco_btn = tk.Button(janela, text='', command=lambda: escolha(5), font=('', 30))  # criando objeto botão
cinco_btn.place(x=10, y=100, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
seis_btn = tk.Button(janela, text='', command=lambda: escolha(6), font=('', 30))  # criando objeto botão
seis_btn.place(x=70, y=100, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
sete_btn = tk.Button(janela, text='', command=lambda: escolha(7), font=('', 30))  # criando objeto botão
sete_btn.place(x=130, y=100, width=50, height=50)                                 # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
oito_btn = tk.Button(janela, text='', command=lambda: escolha(8), font=('', 30))  # criando objeto botão
oito_btn.place(x=190, y=100, width=50, height=50)                                 # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
nove_btn = tk.Button(janela, text='', command=lambda: escolha(9), font=('', 30))  # criando objeto botão
nove_btn.place(x=10, y=160, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
dez_btn = tk.Button(janela, text='', command=lambda: escolha(10), font=('', 30))  # criando objeto botão
dez_btn.place(x=70, y=160, width=50, height=50)                                   # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
onze_btn = tk.Button(janela, text='', command=lambda: escolha(11), font=('', 30))  # criando objeto botão
onze_btn.place(x=130, y=160, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
doze_btn = tk.Button(janela, text='', command=lambda: escolha(12), font=('', 30))  # criando objeto botão
doze_btn.place(x=190, y=160, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
treze_btn = tk.Button(janela, text='', command=lambda: escolha(13), font=('', 30))  # criando objeto botão
treze_btn.place(x=10, y=220, width=50, height=50)                                   # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
quatorze_btn = tk.Button(janela, text='', command=lambda: escolha(14), font=('', 30))  # criando objeto botão
quatorze_btn.place(x=70, y=220, width=50, height=50)                                   # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
quinze_btn = tk.Button(janela, text='', command=lambda: escolha(15), font=('', 30))  # criando objeto botão
quinze_btn.place(x=130, y=220, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
dezesseis_btn = tk.Button(janela, text='', command=lambda: escolha(16), font=('', 30))  # criando objeto botão
dezesseis_btn.place(x=190, y=220, width=50, height=50)                                  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
tempo_texto = tk.Label(janela, text='', font=('', 12))  # cronometro na janela
tempo_texto.place(x=10, y=276, width=230)               # posição do objeto
cronometro2(0)                                          # chama a função para contar o tempo do jogo
# ---------------------------------------------------------------------------------------------------------------------
kb.on_press_key('ENTER', lambda _: limpa())         # comando para recomeçar
kb.on_press_key('ESC', lambda _: janela.destroy())  # comando para fechar a janela
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()  # mantem a janela aberta
