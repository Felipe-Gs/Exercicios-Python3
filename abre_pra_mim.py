import pyautogui, time
print('--------------------LIPE GS-------------------')
print('Abaixo está as opcões de escolha...')
print('')
print(' 1 = CMD\n',  
'2 = ARQUIVOS\n', 
'3 = OPERA GX\n',
'4 = CALCULADORA\n',
'5 = CAMERA\n',
'6 = Firefox\n',
'7 = Google crome\n',
'8 = Word\n',
'9 = Power point\n',
'10 = calendario\n',
'11 = Excel\n',
'12 = whatsaap\n',
'13 = Instagram\n',
'14 = Paint\n',
'DIGITE 0 PARA SAIR DO PROGRAMA')
print('--------------------LIPE GS-------------------')
lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
while True:
    op = (input('Digite o que voçe deseja abrir:'))
    if op == '1':
        pyautogui.press('win')
        pyautogui.typewrite('CMD')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
    elif op == '2':
        pyautogui.press('win')
        pyautogui.typewrite('arquivos')
        pyautogui.press('enter')
    elif op == '3':
        pyautogui.press('win')
        pyautogui.typewrite('opera gx')
        pyautogui.press('enter')
    elif op == '4':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('calculadora')
        pyautogui.press('enter')
    elif op == '5':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('camera')
        pyautogui.press('enter')
    elif op == '6':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('firefox')
        pyautogui.press('enter')
    elif op == '7':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('google chrome')
        pyautogui.press('enter')
    elif op == '8':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('word')
        pyautogui.press('enter')
    elif op == '9':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('power point')
        pyautogui.press('enter')
    elif op == '10':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('calendario')
        pyautogui.press('enter')
    elif op == '11':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('excel')
        pyautogui.press('enter')
    elif op == '12':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('navegador')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=240, y=52)
        pyautogui.typewrite('https://web.whatsapp.com')
        pyautogui.press('enter')
    elif op == '13':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('navegador')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(x=240, y=52)
        pyautogui.typewrite('https://www.instagram.com/accounts/login/')
        pyautogui.press('enter')
    elif op == '14':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('paint')
        pyautogui.press('enter')     
    elif op == '0':
        print('voce saiu do programa!')
        break
    else:
        print('voce digitou errado.')
        continue
           

    



