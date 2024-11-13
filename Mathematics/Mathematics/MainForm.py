import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._button5 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(44, 177)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(129, 57)
        self._button1.TabIndex = 0
        self._button1.Text = "1+1="
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(261, 176)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(103, 57)
        self._button2.TabIndex = 1
        self._button2.Text = "2+2="
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(425, 179)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(107, 55)
        self._button3.TabIndex = 2
        self._button3.Text = "5-2="
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(600, 179)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(113, 54)
        self._button4.TabIndex = 3
        self._button4.Text = "8-3="
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(261, 27)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(162, 67)
        self._label1.TabIndex = 4
        # 
        # button5
        # 
        self._button5.Location = System.Drawing.Point(359, 229)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(90, 60)
        self._button5.TabIndex = 5
        self._button5.Text = "exit"
        self._button5.UseVisualStyleBackColor = True
        self._button5.Click += self.Button5Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(828, 294)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Mathematics"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "2"

    def Button2Click(self, sender, e):
        self._label1.Text = "4"

    def Button3Click(self, sender, e):
        self._label1.Text = "3"

    def Button4Click(self, sender, e):
        self._label1.Text = "5"

    def Button5Click(self, sender, e):
        Application.Exit()
        