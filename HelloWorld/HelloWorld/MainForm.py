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
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.Info
        self._button1.Location = System.Drawing.Point(80, 144)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(109, 51)
        self._button1.TabIndex = 0
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button2.Location = System.Drawing.Point(238, 127)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(151, 125)
        self._button2.TabIndex = 1
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.Info
        self._button3.Location = System.Drawing.Point(417, 145)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(114, 39)
        self._button3.TabIndex = 2
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(217, 46)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(172, 65)
        self._label1.TabIndex = 3
        self._label1.Click += self.Label1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Violet
        self.ClientSize = System.Drawing.Size(624, 289)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Helloworld"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Hello,world!"
        

    def Button2Click(self, sender, e):
        self._label1.Text = ""
      
    
    def Button3Click(self, sender, e):
        Application.Exit()
