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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(1, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(182, 30)
        self._label1.TabIndex = 0
        self._label1.Text = "amount of purchase"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(1, 59)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(182, 36)
        self._label2.TabIndex = 1
        self._label2.Text = "amount received from the customer"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(202, 9)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(110, 20)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(202, 59)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(110, 20)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label3.Location = System.Drawing.Point(-2, 110)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(65, 24)
        self._label3.TabIndex = 4
        self._label3.Text = "Dollars"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(-2, 149)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(63, 27)
        self._label4.TabIndex = 5
        self._label4.Text = "Quarters"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(-2, 187)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(63, 29)
        self._label5.TabIndex = 6
        self._label5.Text = "Dimes"
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(0, 225)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(60, 26)
        self._label6.TabIndex = 7
        self._label6.Text = "Nickels"
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(0, 265)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(60, 30)
        self._label7.TabIndex = 8
        self._label7.Text = "Pennies"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.Info
        self._label8.Location = System.Drawing.Point(71, 106)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(99, 28)
        self._label8.TabIndex = 9
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.Info
        self._label9.Location = System.Drawing.Point(72, 148)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(99, 28)
        self._label9.TabIndex = 10
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.Info
        self._label10.Location = System.Drawing.Point(72, 187)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(99, 28)
        self._label10.TabIndex = 11
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.SystemColors.Info
        self._label11.Location = System.Drawing.Point(71, 225)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(99, 28)
        self._label11.TabIndex = 12
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.SystemColors.Info
        self._label12.Location = System.Drawing.Point(72, 265)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(99, 28)
        self._label12.TabIndex = 13
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(199, 129)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(83, 36)
        self._button1.TabIndex = 14
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(203, 181)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(78, 34)
        self._button2.TabIndex = 15
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(207, 231)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(73, 34)
        self._button3.TabIndex = 16
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(385, 304)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pprog58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e): 
    