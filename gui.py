# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MainWindow
###########################################################################

class MainWindow(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Quiz",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

        self.correct = -1
        self.questions = []
        self.current_question = 0
        self.correct_questions = 0
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_simplebook1 = wx.Simplebook(self, wx.ID_ANY, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_panel1 = wx.Panel(self.m_simplebook1, wx.ID_ANY,
                                 wx.DefaultPosition, wx.DefaultSize,
                                 wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText9 = wx.StaticText(self.m_panel1, wx.ID_ANY,
                                           u"Test name:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        bSizer2.Add(self.m_staticText9, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_inputCtlr = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_CENTER | wx.TE_PROCESS_ENTER)
        self.m_inputCtlr.SetMinSize(wx.Size(200, -1))

        bSizer2.Add(self.m_inputCtlr, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_enterBtn = wx.Button(self.m_panel1, wx.ID_ANY, u"Enter",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_enterBtn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        self.m_simplebook1.AddPage(self.m_panel1, u"a page", False)
        self.m_panel2 = wx.Panel(self.m_simplebook1, wx.ID_ANY,
                                 wx.DefaultPosition, wx.DefaultSize,
                                 wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer3.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_questionText = wx.StaticText(self.m_panel2, wx.ID_ANY,
                                            u"MyLabel", wx.DefaultPosition,
                                            wx.DefaultSize,
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_questionText.Wrap(-1)

        bSizer3.Add(self.m_questionText, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_answerBox0 = wx.CheckBox(self.m_panel2, wx.ID_ANY, u"Check Me!",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_answerBox0, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_answerBox1 = wx.CheckBox(self.m_panel2, wx.ID_ANY, u"Check Me!",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_answerBox1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_answerBox2 = wx.CheckBox(self.m_panel2, wx.ID_ANY, u"Check Me!",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_answerBox2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_answerBox3 = wx.CheckBox(self.m_panel2, wx.ID_ANY, u"Check Me!",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_answerBox3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer3.Add(gSizer1, 1, wx.EXPAND, 5)

        bSizer3.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        self.m_simplebook1.AddPage(self.m_panel2, u"a page", False)
        self.m_panel3 = wx.Panel(self.m_simplebook1, wx.ID_ANY,
                                 wx.DefaultPosition, wx.DefaultSize,
                                 wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer4.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_resultText = wx.StaticText(self.m_panel3, wx.ID_ANY,
                                          u"Your result: 3/5",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_resultText.Wrap(-1)

        bSizer4.Add(self.m_resultText, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button7 = wx.Button(self.m_panel3, wx.ID_ANY, u"Again",
                                   wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        self.m_simplebook1.AddPage(self.m_panel3, u"a page", False)

        bSizer1.Add(self.m_simplebook1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_inputCtlr.Bind(wx.EVT_TEXT, self.on_text)
        self.m_inputCtlr.Bind(wx.EVT_TEXT_ENTER, self.enter)
        self.m_enterBtn.Bind(wx.EVT_BUTTON, self.enter)
        self.m_answerBox0.Bind(wx.EVT_CHECKBOX, self.check)
        self.m_answerBox1.Bind(wx.EVT_CHECKBOX, self.check)
        self.m_answerBox2.Bind(wx.EVT_CHECKBOX, self.check)
        self.m_answerBox3.Bind(wx.EVT_CHECKBOX, self.check)
        self.m_button7.Bind(wx.EVT_BUTTON, self.finish)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    #
    # Technically, it better to follow the above advise and implement
    # business logic in the derived class. Maybe I'll refactor this someday)
    def on_text(self, event):
        self.m_inputCtlr.SetBackgroundColour(wx.WHITE)
        event.Skip()

    def enter(self, event):
        try:
            with open(self.m_inputCtlr.GetValue(), 'r') as file:
                self.questions = file.readlines()
            self.update_question()
            self.m_simplebook1.SetSelection(1)
        except FileNotFoundError:
            self.m_inputCtlr.SetBackgroundColour(wx.RED)
        event.Skip()

    def check(self, event: wx.Event):
        if event.GetEventObject().GetLabel() == self.correct:
            self.correct_questions += 1
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
            self.Update()
        else:
            self.m_resultText.SetLabelText(
                "Your result: {}/{}!".format(self.correct_questions,
                                             self.current_question))
            self.m_simplebook1.ChangeSelection(2)
        event.Skip()

    def finish(self, event):
        self.questions = []
        self.correct_questions = 0
        self.current_question = 0
        self.m_simplebook1.ChangeSelection(0)
        event.Skip()

    def update_question(self):
        data = self.questions[self.current_question].strip().split(';')
        self.m_questionText.SetLabelText(data[0])
        self.correct = data[2 + int(data[1])]
        self.m_answerBox0.SetLabelText(data[2])
        self.m_answerBox1.SetLabelText(data[3])
        self.m_answerBox2.SetLabelText(data[4])
        self.m_answerBox3.SetLabelText(data[5])
        self.m_answerBox0.SetValue(False)
        self.m_answerBox1.SetValue(False)
        self.m_answerBox2.SetValue(False)
        self.m_answerBox3.SetValue(False)
