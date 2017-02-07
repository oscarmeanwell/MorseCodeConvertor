from tkinter import *
root = Tk()
class AddWindow():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Morse Code Convertor")
        self.parent.geometry("500x500")
        self.parent.configure(background = "steel blue")
        self.MorseArray = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']
        self.Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.AddFrames()
        self.AddStuff()

    def AddFrames(self):
        self.MainFrm = Frame(self.parent, width = "500", height = "500", background = "steel blue")
        self.MainFrm.grid(row = 0, column = 0)
        self.BtnFrm = Frame(self.parent, width = "500", height = "500", background = "steel blue")
        self.BtnFrm.grid(row = 1, column = 0)
        
    def AddStuff(self):
        self.TextB = Text(self.MainFrm, width = "50", height = "20", bg = "white", wrap = NONE, bd = 4, font = 'Calibri')
        self.MorseBtn = Button(self.BtnFrm, text = "Morse", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = "light blue", command = self.ConvertToMorse)
        self.TextBtn = Button(self.BtnFrm, text = "Text", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = "light blue", command = self.ConvertToText)
        self.TextB.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.MorseBtn.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.TextBtn.grid(row = 0, column = 1, padx = 20, pady = 20)
        

    def ConvertToMorse(self):
        self.Data = self.TextB.get(1.0, END)
        self.TextB.delete(1.0, END)
        self.MorseHolder = ''
        for Char in self.Data:
            if Char == '\n':
                pass
            elif Char.lower() == '' or Char.lower() == ' ':
                self.MorseHolder += '/'

            else:
                self.Place = self.Alphabet.index(Char.lower())
                self.MorseHolder += self.MorseArray[self.Place]
                self.MorseHolder += ' '

        self.TextB.insert(END, self.MorseHolder)
        
    def ConvertToText(self):
        self.Data2 = self.TextB.get(1.0, END)
        self.TextB.delete(1.0, END)
        self.Finished = ''
        self.Holder = ''
        for Chars in self.Data2:
            
            if Chars == ' ' and len(self.Holder) > 0:
                self.Temp = self.MorseArray.index(self.Holder)
                self.Finished += self.Alphabet[self.Temp]
                self.Holder = ''

            elif Chars != '/' and Chars != ' ':
                self.Holder += Chars

            elif Chars == '/':
                self.Finished += '  '
               
        self.TextB.insert(END, self.Finished)
        
addwindow = AddWindow(root)
root.mainloop()
