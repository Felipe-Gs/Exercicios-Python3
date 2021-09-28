import PySimpleGUI as sg

layout = [[sg.Text("Qual o filme a ser cadastrado?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text("Nome do autor")],
          [sg.Input(key='-INPUT1-')],
          [sg.Text("Duracao do Filme:")],
          [sg.Input(key='-INPUT2-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

window = sg.Window('Cadastro de Filmes', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    window['-OUTPUT-'].update('Filme ' + values['-INPUT-'] + "! Foi cadastrado com sucesso")


window.close()

'''import PySimpleGUI as sg                        

filmes = []
lista = []
layout = [  [sg.Text("Nome do Filme?")], 
            [sg.Input()],
            [sg.Text('Nome do autor?')],
            [sg.Input()],
            [sg.Text('Duração do Filme?')],
            [sg.Input()],
            [sg.Button('Ok')]]

# Create the window
window = sg.Window('Cadastro de Filmes', layout)     


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break 
    print('O nome do Filme é:', values[0])
    print('O autor é:',values[1])
    print('A duraçao do Filme é:', values[2])
    print('-='*30)
    filmes.append(values)
    print(filmes)
    print('Cadastre outro Filme')
    
    

    
window.close()'''

