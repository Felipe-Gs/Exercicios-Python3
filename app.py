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
        self.hi_there["text"] = " 1 = Abre o Navegador!"
        self.hi_there["command"] = self.opcao1
        self.hi_there.pack(side="left")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "2 = Abre Meus arquivos!"
        self.hi_there["command"] = self.opcao2
        self.hi_there.pack(side="left")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "3 = Abre a Camera!"
        self.hi_there["command"] = self.opcao3
        self.hi_there.pack(side="left")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "4 = abre o Word!"
        self.hi_there["command"] = self.opcao4
        self.hi_there.pack(side="left")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "5 = Abre o Power point!"
        self.hi_there["command"] = self.opcao5
        self.hi_there.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom",)

    def opcao1(self):
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('navegador')
        pyautogui.press('enter')

    def opcao2(self):
        pyautogui.press('win')
        time.sleep(0.2)
        pyautogui.typewrite('explorador de arquivos') 
        pyautogui.press('enter')

    def opcao3(self):
        pyautogui.press('win')
        time.sleep(0.2)
        pyautogui.typewrite('camera')
        pyautogui.press('enter')

    def opcao4(self):
        pyautogui.press('win')
        time.sleep(0.2)
        pyautogui.typewrite('Word')
        pyautogui.press('enter')

    def opcao5(self):
        pyautogui.press('win')
        time.sleep(0.2)     
        pyautogui.typewrite('Power point')
        pyautogui.press('enter')    

root = tk.Tk()
app = Application(master=root)
app.mainloop()