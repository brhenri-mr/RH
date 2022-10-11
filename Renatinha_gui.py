import PySimpleGUI as sg
import Renatinha_web as web
import pandas as pd

class Renatinha_gui_R1():

    def __init__(self):
        pass

    def iniciar():

        docs = []
        assinaturas = []
        datas = []
        nomes = []

        cri = 0

        def login():
            sg.theme('DarkAmber')   # Add a touch of color
            # All the stuff inside your window.
            layout = [  [sg.Text('Nome'),sg.InputText()],
                        [sg.Text('Senha'), sg.InputText()],
                        [sg.Button('Ok'), sg.Button('Cancel')] ]
            return sg.Window('login',layout, finalize = True)
        
        def entrou():

            sg.theme('DarkAmber')   # Add a touch of color
            # All the stuff inside your window.
            layout = [  [sg.Text('Nome a ser procurado'),sg.InputText()],
                    [sg.Button('Ok'), sg.Button('Cancel')] ]
            return sg.Window('entrou',layout,finalize = True)

        janela1, janela2 = login(),None

            # Event Loop to process "events" and get the "values" of the inputs
        while True:
            window,event, values = sg.read_all_windows()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            print('You entered ', values[0])
            if janela1 == window and event == "Ok":
                if True: #values[1] == 'breno gostoso' and values[0] == 'Renatinha':
                    janela2 = entrou()
                    janela1.hide()
                    #teria q ficar aqui a abertura da pagina
            elif janela2 == window and event == "Ok":
                #importar o web renatinha
                nome = values[0]
                web.abrir_pagina()
                try:
                    doc , ass, data, name = web.verificar_assinaturas(nome)
                except:
                    web.abrir_pagina()
                    doc , ass, data, name = web.verificar_assinaturas(nome)

                web.procurar_por_usuario(nome)
                doc , ass, data, name = web.verificar_assinaturas(nome)
                docs.append(doc)
                assinaturas.append(ass)
                datas.append(data)
                nomes.append(name)

        web.excel(docs,assinaturas,datas,nomes)     
        window.close()

Renatinha_gui_R1.iniciar()


  