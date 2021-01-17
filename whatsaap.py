import pyautogui, time

time.sleep(3)
pyautogui.click(x=803, y=51)
pyautogui.typewrite("https://web.whatsapp.com", interval=0.1)
pyautogui.press("enter")
time.sleep(25)

def acha_pessoa(nome):
    pyautogui.click(x=166, y=149)
    nome = pyautogui.typewrite(nome, interval=0.1)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=674, y=711)
def mandar_mensagem(mensagem):
    mensagem = pyautogui.typewrite(mensagem)
    pyautogui.press("enter")


acha_pessoa("alessandro")
mandar_mensagem("salve")
acha_pessoa("luana")
for c in range(2):
    mandar_mensagem("teste")


