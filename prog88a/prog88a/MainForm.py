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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label1.Location = System.Drawing.Point(3, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(78, 30)
        self._label1.TabIndex = 0
        self._label1.Text = "Num1:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label2.Location = System.Drawing.Point(3, 49)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(78, 27)
        self._label2.TabIndex = 1
        self._label2.Text = "Num2:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label3.Location = System.Drawing.Point(3, 279)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(78, 30)
        self._label3.TabIndex = 2
        self._label3.Text = "Max"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label4.Location = System.Drawing.Point(3, 247)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(78, 22)
        self._label4.TabIndex = 3
        self._label4.Text = "Distance"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label5.Location = System.Drawing.Point(3, 212)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(78, 26)
        self._label5.TabIndex = 4
        self._label5.Text = "Average"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label6.Location = System.Drawing.Point(3, 176)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(78, 26)
        self._label6.TabIndex = 5
        self._label6.Text = "Product"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label7.Location = System.Drawing.Point(3, 141)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(78, 25)
        self._label7.TabIndex = 6
        self._label7.Text = "Difference"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label8.Location = System.Drawing.Point(2, 96)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(78, 31)
        self._label8.TabIndex = 7
        self._label8.Text = "Sum"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label9.Location = System.Drawing.Point(3, 321)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(77, 24)
        self._label9.TabIndex = 8
        self._label9.Text = "Min"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(114, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(140, 20)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(114, 53)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(140, 20)
        self._textBox2.TabIndex = 10
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label10.Location = System.Drawing.Point(121, 105)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(167, 28)
        self._label10.TabIndex = 11
        self._label10.Click += self.Label10Click
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label11.Location = System.Drawing.Point(119, 145)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(167, 21)
        self._label11.TabIndex = 12
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label12.Location = System.Drawing.Point(119, 176)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(167, 26)
        self._label12.TabIndex = 13
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label13.Location = System.Drawing.Point(119, 212)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(166, 25)
        self._label13.TabIndex = 14
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label14.Location = System.Drawing.Point(120, 247)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(166, 22)
        self._label14.TabIndex = 15
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label15.Location = System.Drawing.Point(120, 279)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(166, 30)
        self._label15.TabIndex = 16
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label16.Location = System.Drawing.Point(121, 322)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(164, 23)
        self._label16.TabIndex = 17
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Lime
        self._button1.Location = System.Drawing.Point(2, 348)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(77, 42)
        self._button1.TabIndex = 18
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Lime
        self._button2.Location = System.Drawing.Point(102, 350)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(81, 42)
        self._button2.TabIndex = 19
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Lime
        self._button3.Location = System.Drawing.Point(201, 350)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(90, 40)
        self._button3.TabIndex = 20
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(308, 402)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog88a"
        self.ResumeLayout(False)
        self.PerformLayout()


    

    def Button1Click(self, sender, e): 
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        Sum = num1 + num2
        Dif = num1 - num2
        Pro = num1 * num2
        Ave = (num1 + num2) / 2
        Abs = 
        
        if num1 > num2:
            num1 = Max,num2 = Min
        else:num2 = max,num1 = Min
        
            
        self._label10.Text = str(Sum)
        self._label11.Text = str(Dif)
        self._label12.Text = str(Pro)
        self._label13.Text = str(Ave) 
        self._label14.Text = str(Dis)
        self._label15.Text = str(Max)
        self._label16.Text = str(Min)
        
       

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._label13.Text = ""
        self._label14.Text = ""
        self._label15.Text = ""
        self._label16.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()