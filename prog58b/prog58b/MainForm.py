﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Yellow
        self._label1.Location = System.Drawing.Point(38, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(69, 41)
        self._label1.TabIndex = 0
        self._label1.Text = "a"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Yellow
        self._label2.Location = System.Drawing.Point(38, 88)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(69, 45)
        self._label2.TabIndex = 1
        self._label2.Text = "b"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Yellow
        self._label3.Location = System.Drawing.Point(38, 156)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(71, 42)
        self._label3.TabIndex = 2
        self._label3.Text = "c"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(37, 228)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(88, 46)
        self._button1.TabIndex = 3
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(166, 232)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(78, 41)
        self._button2.TabIndex = 4
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(290, 237)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(81, 36)
        self._button3.TabIndex = 5
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(174, 21)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(96, 20)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(174, 98)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(95, 20)
        self._textBox2.TabIndex = 7
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(174, 178)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(94, 20)
        self._textBox3.TabIndex = 8
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Yellow
        self._label4.Location = System.Drawing.Point(326, 75)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(77, 43)
        self._label4.TabIndex = 9
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Yellow
        self._label5.Location = System.Drawing.Point(326, 135)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(77, 47)
        self._label5.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(553, 296)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()

 

    def Button1Click(self, sender, e):
        A     = int(self.textBox1.Text)
        B     = int(self.textBox2.Text)
        C     = int(self.textBox3.Text)
        root  = (-B + math.sqrt(B** - 4 * A * C))/2 * A
        root2 = (-B - math.sqrt(B** - 4 * A * C))/2 * A
        self._label4.Text = str(root)
        self._label5.Text = str(root2)
       

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textbox3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()