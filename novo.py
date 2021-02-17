import tkinter as tk
import pyautogui
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.criar_opcoes()
        
    

    def criar_opcoes(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = " Escolha o número de mensagens que quer enviar:\n Após clicar no numero de mensagens,\nvoce tem 5 segundo para apertar em algum local que tenha 'chat'"
        self.hi_there.pack(side="top")
#criar um botão
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "10 mensagens"
        self.hi_there["command"] = self.opcao1
        self.hi_there.pack(side="top")
#criar um botão
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "20 mensagens"
        self.hi_there["command"] = self.opcao2
        self.hi_there.pack(side="top")
#criar um botão
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "30 mensagens"
        self.hi_there["command"] = self.opcao3
        self.hi_there.pack(side="top")


#botão de sair
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="right")
    
#o que o botão 1 faz:
    def opcao1(self):
        time.sleep(5)
        for c in range(10):
            pyautogui.typewrite('eai')
            pyautogui.press('enter')

#o que o botão 2 faz:
    def opcao2(self):
        time.sleep(5)
        for c in range(20):
            pyautogui.typewrite('eai coisa feia')
            pyautogui.press('enter')

#o que o botão 3 faz:
    def opcao3(self):
        time.sleep(5)
        for c in range(30):
            pyautogui.typewrite('eai')
            pyautogui.press('enter')        

 

root = tk.Tk()
root.title("Felipe Gomes")
root.geometry("352x200")
app = Application(master=root)
app.mainloop()




