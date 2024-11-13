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
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Cyan
        self._label1.Location = System.Drawing.Point(24, 20)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(97, 43)
        self._label1.TabIndex = 0
        self._label1.Text = "pounds"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Cyan
        self._label2.Location = System.Drawing.Point(27, 94)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(93, 44)
        self._label2.TabIndex = 1
        self._label2.Text = "shillings"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Cyan
        self._label3.Location = System.Drawing.Point(27, 177)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(93, 43)
        self._label3.TabIndex = 2
        self._label3.Text = "pence"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Cyan
        self._label4.Location = System.Drawing.Point(28, 254)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(93, 44)
        self._label4.TabIndex = 3
        self._label4.Text = "decimal pounds"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(148, 34)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(87, 28)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(148, 107)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(87, 26)
        self._label6.TabIndex = 5
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Location = System.Drawing.Point(149, 268)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(84, 29)
        self._label8.TabIndex = 7
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Location = System.Drawing.Point(149, 192)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(86, 28)
        self._label7.TabIndex = 8
        self._label7.Click += self.Label7Click
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(354, 62)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(82, 36)
        self._button1.TabIndex = 9
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(353, 132)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(83, 33)
        self._button2.TabIndex = 10
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(352, 207)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(83, 34)
        self._button3.TabIndex = 11
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self.ClientSize = System.Drawing.Size(583, 324)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog65h"
        self.ResumeLayout(False)


   

    def Button1Click(self, sender, e):
        