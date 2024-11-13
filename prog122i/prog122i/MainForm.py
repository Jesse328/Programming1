import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(200, 21)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(185, 160)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(38, 256)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(136, 75)
        self._button1.TabIndex = 1
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(216, 254)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(141, 75)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(392, 256)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(147, 72)
        self._button3.TabIndex = 3
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(607, 427)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122i"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "