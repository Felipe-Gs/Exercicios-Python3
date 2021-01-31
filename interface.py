from PySimpleGUI import PySimpleGUI as sg


#layout
sg.theme('Reddit')                        
layout = [
    [sg.Text('Usúario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#janela 
janela = sg.Window('Tela de login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Felipe' and valores['senha'] == '123':
            print('bem vindo Felipe.')