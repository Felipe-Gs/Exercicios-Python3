import pyautogui, time
print('--------------------Tabela de opcões-------------------')
print(' 1 = CMD\n', 
'2 = ARQUIVOS\n', 
'3 = OPERA GX\n',
'4 = CALCULADORA\n',
'5 = CAMERA\n',
'DIGITE 0 PARA SAIR DO PROGRAMA')
print('--------------------Tabela de opcões-------------------')
lista = ['1', '2', '3', '4', '5']
while True:
    op = int(input('digite o que voce deseja abrir:')) 
    if op == 1:
        pyautogui.click(x=56, y=745)#clica em pesquisar no computador)
        pyautogui.typewrite('CMD')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
    elif op == 2:
        pyautogui.click(x=592, y=754)
        time.sleep(5)
    elif op == 3:
        pyautogui.click(x=56, y=745)
        pyautogui.typewrite('opera gx')
        pyautogui.press('enter')
    elif op == 4:
        pyautogui.click(x=56, y=745)
        time.sleep(1)
        pyautogui.typewrite('calculadora')
        pyautogui.press('enter')
    elif op == 5:
        pyautogui.click(x=56, y=745)
        time.sleep(1)
        pyautogui.typewrite('camera')
        pyautogui.press('enter')
    elif op == 0:
        print('voce saiu do programa!')
        break
    else:
        print('voce digitou errado.')
        continue
           

    



