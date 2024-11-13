import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(234, 7)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(279, 90)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(55, 141)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(150, 83)
        self._button1.TabIndex = 1
        self._button1.Text = "SHOOT"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(276, 141)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(132, 77)
        self._button2.TabIndex = 2
        self._button2.Text = "HIT"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(482, 150)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(146, 73)
        self._button3.TabIndex = 3
        self._button3.Text = "run"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(817, 319)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "GO"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "uhhhh"
        

    def Button2Click(self, sender, e):
        self._label1.Text = "ohhh"

    def Button3Click(self, sender, e):
        Application.Exit()