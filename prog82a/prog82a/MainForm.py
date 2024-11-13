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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(10, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(84, 38)
        self._label1.TabIndex = 0
        self._label1.Text = " limit"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(10, 80)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(84, 37)
        self._label2.TabIndex = 1
        self._label2.Text = "speed"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Location = System.Drawing.Point(10, 141)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(84, 37)
        self._label3.TabIndex = 2
        self._label3.Text = "Fine"
       
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(110, 28)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(84, 20)
        self._textBox1.TabIndex = 3
       
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(110, 80)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(84, 20)
        self._textBox2.TabIndex = 4
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.Info
        self._label4.Location = System.Drawing.Point(110, 141)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(84, 30)
        self._label4.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(39, 202)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 44)
        self._button1.TabIndex = 6
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(129, 201)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(77, 44)
        self._button2.TabIndex = 7
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(220, 204)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(72, 40)
        self._button3.TabIndex = 8
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(334, 270)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog82a"
        self.ResumeLayout(False)
        self.PerformLayout()


    

    def Button1Click(self, sender, e):
        speed = int(self.textBox1.Text)
        limit = int(self.textBox2.Text)
        if limit > speed:
            fine = 0
        elif limit < speed:
            fine = ((speed - limit) * 5) + 20
            self._label4,Text = str(fine)
    
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text =""

    def Button3Click(self, sender, e):
        Application.Exit()