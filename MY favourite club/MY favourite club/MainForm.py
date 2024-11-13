import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Info
        self._label1.Location = System.Drawing.Point(279, 27)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(145, 58)
        self._label1.TabIndex = 0
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(191, 27)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(89, 30)
        self._label2.TabIndex = 1
        self._label2.Text = "My favourite club"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(29, 168)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(142, 69)
        self._button1.TabIndex = 2
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(214, 166)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(146, 70)
        self._button2.TabIndex = 3
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(408, 169)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(138, 66)
        self._button3.TabIndex = 4
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(610, 294)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "MY favourite club"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "basketball club"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()