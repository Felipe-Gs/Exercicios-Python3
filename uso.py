import pyautogui, time
time.sleep(2)
print(pyautogui.position())
lista = []
while True:
    nome = input('diga o nome:')
    if nome == 'sair':
        break
    lista += [nome]
print(lista) 


