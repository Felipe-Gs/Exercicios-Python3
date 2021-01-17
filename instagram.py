# É NECESSARIO TER O NAVEGADOR ABERTO....!
# DEPENDENDO DA SUA INTERNET, TALVEZ SEJA MELHOR VOCE ALTERAR O TEMPO(SLEEP) PARA UM TEMPO MAIOR

import pyautogui, time
time.sleep(2)
'''pyautogui.moveTo(x=818, y=751, duration=0.1)
pyautogui.click(x=818, y=751)
time.sleep(5)
pyautogui.moveTo(x=803, y=51, duration=0.1)
pyautogui.click(x=803, y=51)
pyautogui.typewrite("https://www.instagram.com/_lipe_gs/", interval=0.1)# COLOQUE O LINK DO SEU INSTAGRAM
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=700, y=417) #clica em continuar como lipe Gs
time.sleep(3)
pyautogui.click(x=699, y=420) #clica em direct
time.sleep(3)
pyautogui.moveTo(x=1020, y=86, duration=0.1)#
pyautogui.click(x=1020, y=86)#
time.sleep(3)
pyautogui.click(x=544, y=174) #clica em pesquisa pessoa!
pyautogui.typewrite("_jg.jaqueline")#digita o nome da pessoa QUE VC QUER MANDAR MENSAGEM!
time.sleep(2.2)
pyautogui.doubleClick(x=655, y=362)#clica na pessoa pesquisada
pyautogui.click(x=655, y=362)#clica na pessoa pesquisada
time.sleep(2)
pyautogui.click(x=860, y=255)#clica em avancado(ir para o privado da pessoa)
time.sleep(2)
for c in range(3):
    pyautogui.typewrite('eai') #manda msg pra pessoa
    #pyautogui.press("enter")
time.sleep(2)    
pyautogui.click(x=544, y=174)#clica em pesquisar pessoa
pyautogui.typewrite("luanagomes")
time.sleep(2)
pyautogui.click(x=655, y=362)#clica na pessoa pesquisada
time.sleep(2)
pyautogui.click(x=860, y=255)#clica em avancado(ir para o privado da pessoa)
time.sleep(2)
for c in range(3):
    pyautogui.typewrite('eai') #manda msg pra pessoa
    #pyautogui.press("enter")'''

#enviar(x=1020, y=86)
#digitar pesquisa(x=544, y=174)
#coordenadas para abrir o OperaGx (x=818, y=751)
def procura_pessoa(nome):
    pyautogui.click(x=544, y=174)#clica em pesquisar pessoa
    nome = pyautogui.typewrite(nome)
    time.sleep(2)
    pyautogui.click(x=655, y=362)#clica na pessoa pesquisada
    time.sleep(2)
    pyautogui.click(x=860, y=255)#clica em avancado(ir para o privado da pessoa)
    time.sleep(2)
    for x in range(3):
        pyautogui.typewrite('eai') #manda msg pra pessoa
        pyautogui.press("enter")


procura_pessoa("felipehisoka")
procura_pessoa("luanagomes")
procura_pessoa("_jg.jaqueline")
procura_pessoa("alessandro_fn05")