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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button5 = System.Windows.Forms.Button()
        self._label11 = System.Windows.Forms.Label()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(12, 18)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(105, 33)
        self._label1.TabIndex = 0
        self._label1.Text = "business"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(12, 67)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(105, 44)
        self._label2.TabIndex = 1
        self._label2.Text = "restaurants"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Location = System.Drawing.Point(12, 126)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(103, 42)
        self._label3.TabIndex = 2
        self._label3.Text = "fast-food palces"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label4.Location = System.Drawing.Point(12, 183)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(103, 38)
        self._label4.TabIndex = 3
        self._label4.Text = "stores"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(149, 22)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(89, 29)
        self._button1.TabIndex = 4
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(149, 67)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(89, 28)
        self._button2.TabIndex = 5
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(149, 126)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(89, 28)
        self._button3.TabIndex = 6
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(149, 189)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(89, 32)
        self._button4.TabIndex = 7
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(154, -1)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(117, 21)
        self._label5.TabIndex = 8
        self._label5.Text = "Click to show"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.Info
        self._label6.Location = System.Drawing.Point(277, 17)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(153, 34)
        self._label6.TabIndex = 9
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.Info
        self._label7.Location = System.Drawing.Point(277, 75)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(154, 27)
        self._label7.TabIndex = 10
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.Info
        self._label8.Location = System.Drawing.Point(276, 126)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(154, 34)
        self._label8.TabIndex = 11
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.Info
        self._label9.Location = System.Drawing.Point(276, 189)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(154, 33)
        self._label9.TabIndex = 12
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label10.Location = System.Drawing.Point(13, 240)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(101, 32)
        self._label10.TabIndex = 13
        self._label10.Text = "Walmart"
        # 
        # button5
        # 
        self._button5.Location = System.Drawing.Point(144, 246)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(94, 27)
        self._button5.TabIndex = 14
        self._button5.UseVisualStyleBackColor = True
        self._button5.Click += self.Button5Click
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.SystemColors.Info
        self._label11.Location = System.Drawing.Point(281, 247)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(148, 34)
        self._label11.TabIndex = 15
        # 
        # button6
        # 
        self._button6.Location = System.Drawing.Point(471, 32)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(87, 35)
        self._button6.TabIndex = 16
        self._button6.Text = "clear"
        self._button6.UseVisualStyleBackColor = True
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.Location = System.Drawing.Point(471, 120)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(86, 33)
        self._button7.TabIndex = 17
        self._button7.Text = "exit"
        self._button7.UseVisualStyleBackColor = True
        self._button7.Click += self.Button7Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(626, 285)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "phone numbers"
        self.ResumeLayout(False)


    

    def Button1Click(self, sender, e):
        self._label6.Text = "718-980-3344"

    def Button2Click(self, sender, e):
        self._label7.Text = "608-321-6859"

    def Button3Click(self, sender, e):
        self._label8.Text = "504-098-8695"

    def Button4Click(self, sender, e):
        self._label9.Text = "328-098-7896"

    

    def Button5Click(self, sender, e):
        self._label11.Text = "407-697-0685"

    def Button6Click(self, sender, e):
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""
        self._label9.Text = ""
        self._label11.Text = ""

    def Button7Click(self, sender, e):
        Application.Exit()