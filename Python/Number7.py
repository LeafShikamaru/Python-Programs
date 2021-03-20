import wx
from tkinter.filedialog import askopenfile
from tkinter import Tk
import tkinter.messagebox as tkmb
from collections import Counter
import json
import random
import datetime
import faker
import time
import calendar
import numpy as np
from pandas import DataFrame
import arrow
import pandas as pd
import matplotlib.pyplot as plt
import pylab


fake = faker.Faker()
usernames = set()
usernames_no = 1000
while len(usernames) < usernames_no:
    usernames.add(fake.user_name())


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

        openItem  = fileButton.Append(wx.ID_ANY, 'Generate File', 'Generating ...')
        savejsonItem = fileButton.Append(wx.ID_SAVE, 'Save JSON', 'Save as JSON ...')
        savecsvItem = fileButton.Append(wx.ID_SAVE, 'Save CSV', 'Save as CSV ...')
        plotaItem = fileButton.Append(wx.ID_SAVE, 'plot a', 'plot a...')
        plotbItem = fileButton.Append(wx.ID_SAVE, 'plot b', 'plot b...')
        plotcItem = fileButton.Append(wx.ID_SAVE, 'plot c', 'plot c...')
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit ...')

        menuBar.Append(fileButton, 'File')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OpenMode, openItem)
        self.Bind(wx.EVT_MENU, self.OnSaveAsJSON, savejsonItem)
        self.Bind(wx.EVT_MENU, self.OnSaveAsCSV, savecsvItem)
        self.Bind(wx.EVT_MENU, self.plota, plotaItem)
        self.Bind(wx.EVT_MENU, self.plotb, plotbItem)
        self.Bind(wx.EVT_MENU, self.plotc, plotcItem)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText('Waiting To select Choice in File')

        self.SetTitle('Program 7')
        self.Show(True)

    def plota(self, e):
        yesNoBox = wx.MessageDialog(None, 'Are you sure you want to graph of the histogram of the of the outside temperature for the sampled times (every 6 hours)?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        if yesNoAnswer == wx.ID_YES:
            self.Close()
            
    def plotb(self, e):
        yesNoBox = wx.MessageDialog(None, 'Are you sure you want to graph of the outside vs the room temperature?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        if yesNoAnswer == wx.ID_YES:
            self.Close()

    def plotc(self, e):
        yesNoBox = wx.MessageDialog(None, 'Are you sure you want to graph a histogram of all of the room and outside temperature and humidity for the 1000 samples across all users?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        if yesNoAnswer == wx.ID_YES:
            self.Close()

    def Quit(self, e):
        yesNoBox = wx.MessageDialog(None, 'Are you sure you want to Quit?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        if yesNoAnswer == wx.ID_YES:
            self.Close()

    def OnSaveAsJSON(self, e):
        with wx.FileDialog(self, "Save File", wildcard="JSON and CSV files (*.json;*.csv)|*.json;*.csv",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as file:
                    self.doSaveData(file)
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)

    def OnSaveAsCSV(self, e):
        with wx.FileDialog(self, "Save File", wildcard="CSV files (*.csv)|*.csv",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as file:
                    self.doSaveData(file)
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)

    def get_random_name_and_gender():
        skew = .6
        male = random.random() > skew
        if male:
            return fake.name_male(), 'M'
        else:
            return fake.name_female(), 'F'
        
    def get_users(usernames):
        users = []
        for username in usernames:
            name, gender = get_random_name_and_gender()
            user = {
                'name': name,
                'gender': gender,
                'email': fake.email(),
                'age': fake.random_int(min=18, max=90),
                'address': fake.address(),
                 'username': username,
            }
            users.append(json.dumps(user))
        return users
    
    def get_start_end_dates():
        start_date = datetime.datetime(2015, 1, 1, 0, 0)
        end_date = datetime.datetime(2020, 4, 17, 0, 0)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates + datetime.timedelta(hours=6)
        random_date = start_date + days_between_dates
        
        def _format_date(date_):
            return date_.strftime("%Y %m %d %H")
        return _format_date(random_date)
    
    def get_temp():
        outTemp = random.randint(70, 95)
        inTemp = outTemp - random.randint(0, 10)
        return outTemp, inTemp

    def get_hum():
        outHum = random.randint(50, 95)
        inHum = outHum - random.randint(0, 10) 
        return outHum, inHum

    def get_sensor(input_):
        date = get_start_end_dates()
        outTemp, inTemp = get_temp()
        outHum, inHum = get_hum()
        return {
            'outside temp': outTemp,
            'inside temp': inTemp,
            'outside humidity': outHum,
            'inside humidity': inHum,
        }

    def get_data(users):
        data = []
        for user in users:
            hourly_update = []
            input_ = datetime.datetime(2015,1,1,0,0)
            for _ in range(10):
                hourly_update.append(get_sensor(input_))
                input_ = input_ + datetime.timedelta(hours=6)
            data.append({'user': user, 'sensor': hourly_update})
        return

    def OpenMode(self,e):
        Tk().withdraw()
        

def main():
    app = wx.App()
    windowClass(None, 0, size=(500,400))        
    app.MainLoop()

main()

