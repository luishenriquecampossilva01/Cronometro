from tkinter import *
import tkinter

# cores
cor1 = "#0a0a0a"
cor2 = "#fafcff"
cor3 = "#21c25c"
cor4 = "#eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"
#configurando a janela
janela = Tk()
janela.title("")
janela.geometry('300x180')
janela.configure(bg = cor1)
janela.resizable(width=FALSE,height=FALSE)
global tempo
global rodar
global contador
global limitador

limitador = 59
tempo = "00:00:00"
rodar = False
contador = -5


def iniciar():
    global tempo
    global rodar
    global contador
    global limitador
    if rodar:
        #antes do cronòmetro começar
        if contador<=-1:
            inicio = 'Comecando em {}'.format(contador)
            label_tempo['text']=inicio
            label_tempo['font'] = 'Arial 10'

        #rodando cronômetro
        else:
                label_tempo['font'] = 'Times 50 bold'
                temporaria = str(tempo)
                h,m,s = map(int,temporaria.split(":"))
                h = int(h)
                m = int(m)
                s = int(contador)

                if (s>=limitador):
                    contador = 0
                    m+=1

                s = str(0)+str(s)
                m = str(0)+str(m)
                h = str(0)+str(h)
                #Atualizando os valores atuais
                temporaria = str(h[-2:])+":"+str(m[-2:])+":"+str(s[-2:])
                label_tempo['text'] = temporaria
                tempo = temporaria
        label_tempo.after(1000,iniciar)
        contador+=1

#função para dar inicio
def start():
    global rodar
    rodar = True
    iniciar()

def stop():
    global rodar
    rodar = False

def restart():
    global tempo
    global contador
    contador = 0
    tempo = "00:00:00"

    label_tempo['text'] = tempo

#CRIANDO LABELS
label_app = Label(janela,text='Cronômtro',font=('Arial 10'),bg = cor1, fg=cor2)
label_app.place(x=20,y=5)

label_tempo = Label(janela,text=tempo,font=('Times 50 bold'),bg = cor1, fg=cor6)
label_tempo.place(x=20,y=30)

#criando botões
botao_iniciar = Button(janela,command=start, text='Iniciar', width = 10, height=2 , bg=cor1,fg=cor2,font=('Ivy 8 bold'),relief='raised',overrelief='ridge')
botao_iniciar.place(x=20,y=130)

botao_pausar = Button(janela,command=stop, text='Pausar', width = 10, height=2 , bg=cor1,fg=cor2,font=('Ivy 8 bold'),relief='raised',overrelief='ridge')
botao_pausar.place(x=110,y=130)

botao_reiniciar = Button(janela,command=restart, text='Reiniciar', width = 10, height=2 , bg=cor1,fg=cor2,font=('Ivy 8 bold'),relief='raised',overrelief='ridge')
botao_reiniciar.place(x=200,y=130)


janela.mainloop()