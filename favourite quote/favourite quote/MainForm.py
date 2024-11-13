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
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(155, 25)
        self._label1.TabIndex = 0
        self._label1.Text = "My favourite quote"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(202, 40)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(183, 89)
        self._label2.TabIndex = 1
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(37, 173)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(129, 43)
        self._button1.TabIndex = 2
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(227, 175)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(121, 40)
        self._button2.TabIndex = 3
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(424, 175)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(99, 39)
        self._button3.TabIndex = 4
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(666, 261)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "favourite quote"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label2.Text = "Nothing is difficult for the man who will try"

    def Button2Click(self, sender, e):
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()