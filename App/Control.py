from tkinter import *
import View as vw
import Model as mod
import ast


class ControlScreens():
    def __init__(self):
        self.telaPrincipal = True
        self.telaMorseToText = False
        self.telaTextToMorse = False
        self.screenResultText = False
        self.screenResultMorse = False
    
    def showMenu(self):
        vw.ScreenMenu()

    def showMorse(self):
        
        vw.MorseToText()

    def showHistoricoMorse(self):
        pass
    
    def showCodesMorse(self):
        pass

    def showText(self):
        vw.TextToMorse()

    def showResultMorse(self, result):
        vw.ResultMorseScreen(result)

    def showResultText(self, result):
        vw.ResultTextScreen(result)


class ControlModel():
    def __init__(self):
        self.historic = []
        self.listCodes = []
        self.listText = []
        
    
class ButtonFunction():
    def __init__(self):
        self.ctrlButtonScreens = ControlScreens()
        self.ctrlButtonDictonary = ControlModel()

    def buttonClear(self, entry):
        entry.delete(0, len(entry.get()))
        
    def buttonMorse(self):
        self.ctrlButtonScreens.showMorse()

    def buttonText(self):
        self.ctrlButtonScreens.showText()

    def buttonConvertMorse(self, code):
        dicMorse = mod.Dictionary().getCodeMorse()
        temp = []
        string = ''
        result = ''

        for i in range(len(code)):
            if code[i] == ' ' and code[i+1] == ' ':
                temp.append('/')
                temp.append('@')
                temp.append('/')
                
            elif code[i] == ' ' and code[i-1] != ' ':
                temp.append('/')
            elif code[i] != ' ':
                temp.append(code[i])

        letter = code.split()
        for let in temp:
            string += let
        string2 = string.split('/')

        for word in string2:
            result += dicMorse[f'{word}']
        return result

    def buttonConvertText(self, code):
        dicText = mod.Dictionary().getTextMorse()
        string = code.upper()
        word = []
        text = []
        for letter in string:
            if letter != ' ':
                word.append(letter)
            else:
                word.append(' ')
        
        for txt in word:
            string2 = dicText[f'{txt}']
            text.append(string2)

        result = ' '.join(text)
        return result
        
            

    
                

        


    
        
        


        
        
        
        
      
                
            

                

            
        
           
    
            
    
            
                    
                

        


                




        

        
        

        
    

    


   

        
   
    
    

        


        
        
        

        
    
        
        