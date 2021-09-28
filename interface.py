from PySimpleGUI import PySimpleGUI as sg


#layout
sg.theme('Reddit')                        
layout = [
    [sg.Text('Filme'), sg.Input(key='usuario')],
    [sg.Text('Genero'), sg.Input(key='senha', password_char='')],
    [sg.Checkbox('Fazer o cadastro?')],
    [sg.Button('Entrar')],
    
]

#janela 
janela = sg.Window('Tela de Cadastro', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] != '999' and valores['senha'] != '999':
            print('O Filme foi cadastrado com sucesso!')













'''import PySimpleGUI as sg

filename = sg.popup_get_file('Pesquise pela pasta:')
sg.popup('You entered', filename)'''