import Control as ctrl

class Dictionary():
    def __init__(self):
        self.dictionaryCode = {'.-' : 'A',
                              '-...' : 'B',
                              '-.-.' : 'C',
                              '-..' : 'D',
                              '.' : 'E',
                              '..-.' : 'F',
                              '--.' : 'G',
                              '....' : 'H',
                              '..' : 'I',
                              '.---' : 'J',
                              '-.-' :' K',
                              '.-..' : 'L',
                              '--' : 'M',
                              '-.' : 'N',
                              '---' : 'O',
                              '.--.' : 'P',
                              '--.-' : 'Q',
                              '.-.' : 'R',
                              '...' : 'S',
                              '-' : 'T',
                              '..-' : 'U',
                              '...-' : 'V',
                              '.--' : 'W',
                              '-..-' : 'X',
                              '-.--' : 'Y',
                              '--..' : 'Z',
                              '.----' : '1',
                              '..---' : '2',
                              '...--' : '3',
                              '...-' : '4',
                              '.....' : '5',
                              '-....' : '6',
                              '--...' : '7',
                              '---..' : '8',
                              '----.' : '9',
                              '-----' : '0',
                              '@': ' ',                                       
        }

        self.dictionaryText = {'A' : '.-',
                            'B' : '-...',
                            'C' : '-.-.',
                            'D' : '-..',
                            'E' : '.',
                            'F' : '..-.',
                            'G' : '--.',
                            'H' : '....',
                            'I' : '..',
                            'J' : '.---',
                            'K' : '-.-',
                            'L' : '.-..',
                            'M' : '--',
                            'N' : '-.',
                            'O' : '---',
                            'P' : '.--.',
                            'Q' : '--.-',
                            'R' : '.-.',
                            'S' : '...',
                            'T' : '-',
                            'U' : '..-',
                            'V' : '...-',
                            'W' : '.--',
                            'X' : '-..-',
                            'Y' : '-.--',
                            'Z' : '--..',
                            '1' : '.----',
                            '2' : '..---',
                            '3' : '...--',
                            '4' : '...-',
                            '5' : '.....',
                            '6' : '-....',
                            '7' : '--...',
                            '8' : '---..',
                            '9' : '----.',
                            '0' : '-----',
                            ' ' : ''
                                                                   
        }
    
    def getCodeMorse(self):
        return self.dictionaryCode

    def getTextMorse(self):
        return self.dictionaryText

        
class Historic():
    def __init__(self):
        self.listHistoric = []
        

    def addHistoric(self, historicCode):
        self.listHistoric.append(historicCode)
        print('Add')
        print(self.listHistoric)

    def getListHistoric(self):
        str = ''
        for code in self.listHistoric:
            str += code
        return str
        

    

        
