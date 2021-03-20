import wx
from tkinter.filedialog import askopenfile
from tkinter import Tk
import tkinter.messagebox as tkmb
from collections import Counter


class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.Centre()
        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        menuBar = wx.MenuBar()

        fileButton = wx.Menu()
        editButton = wx.Menu()
        importItem = wx.Menu()
        viewItem   = wx.Menu()

        openItem  = fileButton.Append(wx.ID_ANY, 'Open File', 'Select a file ...')
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit sample ...')

        menuBar.Append(fileButton, 'File')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OpenMode, openItem)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText('Waiting To select Open')

        self.SetTitle('Open a File')
        self.Show(True)

    def Quit(self, e):
        yesNoBox = wx.MessageDialog(None, 'Are you sure you want to Quit?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        if yesNoAnswer == wx.ID_YES:
            self.Close()


    def OpenMode(self,e):
        Tk().withdraw()
        file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
        if file is not None:
            count = Counter(word for line in file
                            for word in line.split())
            words =(count.most_common(3))
        tkmb.showinfo("Common words", words)


def main():
    app = wx.App()
    windowClass(None, 0, size=(500,400))        
    app.MainLoop()

main()

