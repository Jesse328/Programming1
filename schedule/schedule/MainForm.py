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
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(71, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(97, 26)
        self._label1.TabIndex = 0
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(71, 45)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(97, 28)
        self._label2.TabIndex = 1
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Location = System.Drawing.Point(72, 85)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(96, 26)
        self._label3.TabIndex = 2
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label4.Location = System.Drawing.Point(72, 123)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(96, 28)
        self._label4.TabIndex = 3
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label5.Location = System.Drawing.Point(71, 168)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(96, 26)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label6.Location = System.Drawing.Point(71, 205)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(96, 31)
        self._label6.TabIndex = 5
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label7.Location = System.Drawing.Point(71, 251)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(96, 29)
        self._label7.TabIndex = 6
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label8.Location = System.Drawing.Point(70, 292)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(97, 33)
        self._label8.TabIndex = 7
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(203, 168)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(98, 51)
        self._button1.TabIndex = 8
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(344, 168)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(98, 49)
        self._button2.TabIndex = 9
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(483, 169)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(99, 47)
        self._button3.TabIndex = 10
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label9
        # 
        self._label9.Location = System.Drawing.Point(9, 8)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(56, 26)
        self._label9.TabIndex = 11
        self._label9.Text = "1st hour"
        # 
        # label10
        # 
        self._label10.Location = System.Drawing.Point(8, 44)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(56, 28)
        self._label10.TabIndex = 12
        self._label10.Text = "2nd hour"
        # 
        # label11
        # 
        self._label11.Location = System.Drawing.Point(8, 85)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(50, 25)
        self._label11.TabIndex = 13
        self._label11.Text = "3rd hour"
        # 
        # label12
        # 
        self._label12.Location = System.Drawing.Point(8, 123)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(55, 30)
        self._label12.TabIndex = 14
        self._label12.Text = "4th hour"
        # 
        # label13
        # 
        self._label13.Location = System.Drawing.Point(7, 169)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(56, 25)
        self._label13.TabIndex = 15
        self._label13.Text = "5th hour"
        # 
        # label14
        # 
        self._label14.Location = System.Drawing.Point(5, 212)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(52, 23)
        self._label14.TabIndex = 16
        self._label14.Text = "6th hour"
        # 
        # label15
        # 
        self._label15.Location = System.Drawing.Point(8, 257)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(49, 22)
        self._label15.TabIndex = 17
        self._label15.Text = "7th hour"
        # 
        # label16
        # 
        self._label16.Location = System.Drawing.Point(5, 292)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(60, 23)
        self._label16.TabIndex = 18
        self._label16.Text = "8th hour"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(689, 334)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "schedule"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "US history"
        self._label2.Text = "Computer programme"
        self._label3.Text = "PE"
        self._label4.Text = "Personal finance"
        self._label5.Text = "English"
        self._label6.Text = "Calculus"
        self._label7.Text = "Construction"
        self._label8.Text = "International seminar"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Allpication.Exit()