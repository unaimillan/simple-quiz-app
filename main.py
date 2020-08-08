import wx
from gui import MainWindow


class MyWindow(MainWindow):
    def __init__(self, parent):
        super().__init__(parent)

        self.correct = -1
        self.questions = []
        self.current_question = 0
        self.correct_questions = 0

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


app = wx.App()
window = MyWindow(None)
window.Show()
app.MainLoop()
