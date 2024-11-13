import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(156, 23)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(89, 20)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(29, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(97, 34)
        self._label1.TabIndex = 1
        self._label1.Text = "radius"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Location = System.Drawing.Point(278, 81)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(192, 25)
        self._label3.TabIndex = 3
        self._label3.Text = "Area"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(4, 143)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(76, 45)
        self._button2.TabIndex = 5
        self._button2.Text = "cauculus"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(86, 143)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(76, 45)
        self._button3.TabIndex = 6
        self._button3.Text = "clear"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(170, 144)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(75, 42)
        self._button4.TabIndex = 7
        self._button4.Text = "exit"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(30, 81)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(95, 28)
        self._label2.TabIndex = 8
        self._label2.Text = "pi"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(156, 89)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(90, 20)
        self._textBox2.TabIndex = 9
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.Info
        self._label4.Location = System.Drawing.Point(288, 130)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(181, 147)
        self._label4.TabIndex = 10
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(524, 301)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "prog 54c"
        self.ResumeLayout(False)
        self.PerformLayout()
    


    def Button2Click(self, sender, e):
        radius = float(self.Textbox1._Text)
        pi     = float(self.Textbox2._Text)
        area   = pi * radius**2
        self.label4.Text = str(area)
        # + - * / %     ** pow     // devide & round down
        # int (integer):a whole number,pos/neg
        #float (Floating-Point Number):any number w/ a decimal
        #str (String): a string of text

    def Button3Click(self, sender, e):
        self.textBox1.Text = ""
        self.textBox2.Text = ""
        self.label4.Text = ""

    def Button4Click(self, sender, e):
        Application.Exit()