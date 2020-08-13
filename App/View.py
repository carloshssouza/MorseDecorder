from tkinter import *
from tkinter import messagebox
import Control as ctrl

class ScreenMenu():
    def __init__(self):
       self.root = Tk()
       self.screen()
       self.button()
       self.root.mainloop()

    def screen(self):
        self.root.title("DecoderMorse")
        self.root.configure(background='lightslategray')
        self.root.geometry('400x400')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=900)
        self.root.minsize(width=200, height=200)

    def button(self):
        #Botão MorseToText
        self.buttonMorse = Button(text='MorseToText', command=ctrl.ButtonFunction().buttonMorse)
        self.buttonMorse.place(relx=0.5, rely=0.4, relwidth=0.5, anchor=CENTER)

        self.buttonText = Button(text='TextToMorse', command=ctrl.ButtonFunction().buttonText)
        self.buttonText.place(relx=0.5, rely=0.5, relwidth=0.5, anchor=CENTER)

    def ativarMorse(self):
        print('Morse ativado')

    def ativarText(self):
        print('Texto ativado')


class MorseToText():
    def __init__(self):

        self.window = Tk()
        self.menubar = Menu(self.window)
        self.fileMenu = Menu(self.menubar)
        self.screen()
        self.screenConteudo()
        self.button()
        self.window.mainloop()

    def screen(self):
        self.window.title("MorseToText")
        self.window.configure(background='lightslategray')
        self.window.geometry('400x400')
        self.window.resizable(True, True)
        self.window.maxsize(width=900, height=900)
        self.window.minsize(width=200, height=200)

        self.fileMenu.add_command(label="Historic", \
                    command=self.enterHistoric)
        self.fileMenu.add_command(label="Codes list", \
                    command=self.enterCodesList)
        self.menubar.add_cascade(label="File", \
                    menu=self.fileMenu)
        
        self.window.config(menu=self.menubar)
    
    def screenConteudo(self):
        self.labelMorse = Label(self.window, text='Digite o código morse a ser convertido')
        self.labelMorse.place(relx=0.0, rely=0.1)

        self.entryCodeMorse = Entry(self.window)
        self.entryCodeMorse.place(relx=0.0, rely=0.2, relwidth=0.99)

    def button(self):
        self.buttonConfirm = Button(self.window, text='Confirm', command=self.enterHandler)
        self.buttonConfirm.place(relx=0.0, rely=0.3, relwidth=0.3)

        self.buttonClear = Button(self.window, text='Clear', command=self.clearHandler)
        self.buttonClear.place(relx=0.5, rely=0.3, relwidth=0.3)
    
    def enterHandler(self):
        code = self.entryCodeMorse.get()
        word = ctrl.ButtonFunction().buttonConvertMorse(code)
        resultado = ctrl.ControlScreens().showResultMorse(word)

    def enterCodesList(self):
        str = ctrl.ButtonFunction().buttonCodeList()
        self.mostraJanela('Morse Code - Letters', str)

    def enterHistoric(self):
        pass
        
    def clearHandler(self):
        code = ctrl.ButtonFunction().buttonClear(self.entryCodeMorse)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg) 
        
class TextToMorse():
    def __init__(self):
        self.window = Tk()
        self.menubar = Menu(self.window)
        self.fileMenu = Menu(self.menubar)
        self.screen()
        self.screenConteudo()
        self.button()
        self.window.mainloop()

    def screen(self):
        self.window.title("TextToMorse")
        self.window.configure(background='lightslategray')
        self.window.geometry('400x400')
        self.window.resizable(True, True)
        self.window.maxsize(width=900, height=900)
        self.window.minsize(width=200, height=200)

        self.fileMenu.add_command(label="Historico", \
                    command=ctrl.ControlScreens().showHistoricoMorse)
        self.fileMenu.add_command(label="Lista dos codigos", \
                    command=ctrl.ControlScreens().showCodesMorse)
        self.menubar.add_cascade(label="File", \
                    menu=self.fileMenu)
        
        self.window.config(menu=self.menubar)
        
        
    def screenConteudo(self):
        self.labelText = Label(self.window, text='Digite o texto a ser convertido')
        self.labelText.place(relx=0.0, rely=0.1)

        self.entryText = Entry(self.window)
        self.entryText.place(relx=0.0, rely=0.2, relwidth=0.99)

    def button(self):
        self.buttonConfirm = Button(self.window, text='Confirm', command=self.enterHandler)
        self.buttonConfirm.place(relx=0.0, rely=0.3, relwidth=0.3)
        
        self.buttonClear = Button(self.window, text='Clear')
        self.buttonClear.place(relx=0.5, rely=0.3, relwidth=0.3)

    def enterHandler(self):
        code = self.entryText.get()
        word = ctrl.ButtonFunction().buttonConvertText(code)
        result = ctrl.ControlScreens().showResultText(word)
        
    def clearHandler(self):
        code = ctrl.ButtonFunction().buttonClear(self.entryCodeMorse)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class ResultMorseScreen():
    def __init__(self, result):
        self.result = result
        self.window = Tk()
        self.menubar = Menu(self.window)
        self.fileMenu = Menu(self.menubar)
        self.screen()
        self.screenConteudo(self.result)
        self.window.mainloop()

    def screen(self):
        self.window.title("Result in text")
        self.window.configure(background='lightslategray')
        self.window.geometry('400x400')
        self.window.resizable(True, True)
        self.window.maxsize(width=900, height=900)
        self.window.minsize(width=200, height=200)

        self.fileMenu.add_command(label="Historico", \
                    command=ctrl.ControlScreens().showHistoricMorse)
        self.fileMenu.add_command(label="Lista dos codigos", \
                    command=ctrl.ControlScreens().showCodesMorse)
        self.menubar.add_cascade(label="File", \
                    menu=self.fileMenu)
        
        self.window.config(menu=self.menubar)

    def screenConteudo(self, result):
        self.labelText = Label(self.window, text=result)
        self.labelText.place(relx=0.0, rely=0.1)

class ResultTextScreen():
    def __init__(self, result):
        self.result = result
        self.window = Tk()
        self.menubar = Menu(self.window)
        self.fileMenu = Menu(self.menubar)
        self.screen()
        self.screenConteudo(self.result)
        self.window.mainloop()

    def screen(self):
        self.window.title("Result in morse")
        self.window.configure(background='lightslategray')
        self.window.geometry('400x400')
        self.window.resizable(True, True)
        self.window.maxsize(width=900, height=900)
        self.window.minsize(width=200, height=200)

        self.fileMenu.add_command(label="Historico", \
                    command=ctrl.ControlScreens().showHistoricoMorse)
        self.fileMenu.add_command(label="Lista dos codigos", \
                    command=ctrl.ControlScreens().showCodesMorse)
        self.menubar.add_cascade(label="file", \
                    menu=self.fileMenu)
        
        self.window.config(menu=self.menubar)

    def screenConteudo(self, result):
        self.labelText = Label(self.window, text=result)
        self.labelText.place(relx=0.0, rely=0.1)

    






