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
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkRed
        self._button1.ForeColor = System.Drawing.Color.DarkBlue
        self._button1.Location = System.Drawing.Point(39, 153)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(162, 99)
        self._button1.TabIndex = 1
        self._button1.Text = "Xi jinping"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button2.Location = System.Drawing.Point(261, 150)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(159, 101)
        self._button2.TabIndex = 2
        self._button2.Text = "Joe Biden"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Tomato
        self._button3.Location = System.Drawing.Point(491, 139)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(164, 111)
        self._button3.TabIndex = 3
        self._button3.Text = "Putin"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Info
        self._label1.Location = System.Drawing.Point(411, 32)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(309, 72)
        self._label1.TabIndex = 4
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(12, 47)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(198, 20)
        self._textBox1.TabIndex = 5
        self._textBox1.Text = "What do every chairperson like to do"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(771, 314)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Me"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    

  

    def Button1Click(self, sender, e):
        self._label1.Text = "Passed unanimously"

    def Button2Click(self, sender, e):
        self._label1.Text = "Democrat"

    def Button3Click(self, sender, e):
        self._label1.Text = "Laugh at Trump"