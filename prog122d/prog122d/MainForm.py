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
        self._listBox1.Location = System.Drawing.Point(109, 33)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(158, 82)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(28, 175)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(86, 55)
        self._button1.TabIndex = 1
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(131, 174)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(87, 56)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(242, 174)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(87, 51)
        self._button3.TabIndex = 3
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(459, 295)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122d"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
       Application.Exit()