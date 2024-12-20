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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Control
        self._label1.Location = System.Drawing.Point(31, 49)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(123, 51)
        self._label1.TabIndex = 0
        self._label1.Text = "Tickets sold"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(50, 89)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(203, 65)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter the number of tickets sold for each"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(50, 164)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(70, 36)
        self._label3.TabIndex = 2
        self._label3.Text = "Class A:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(50, 265)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(70, 36)
        self._label4.TabIndex = 3
        self._label4.Text = "Class C:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(50, 211)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(70, 36)
        self._label5.TabIndex = 4
        self._label5.Text = "Class B:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(142, 172)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(111, 21)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(142, 224)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(110, 21)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(142, 282)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(109, 21)
        self._textBox3.TabIndex = 7
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(298, 60)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(111, 28)
        self._label6.TabIndex = 8
        self._label6.Text = "Revenue generated"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(291, 138)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(72, 27)
        self._label7.TabIndex = 9
        self._label7.Text = "Class A:"
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(291, 190)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(72, 23)
        self._label8.TabIndex = 10
        self._label8.Text = "Class B:"
        # 
        # label9
        # 
        self._label9.Location = System.Drawing.Point(291, 237)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(72, 21)
        self._label9.TabIndex = 11
        self._label9.Text = "Class C:"
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(372, 138)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(108, 21)
        self._textBox4.TabIndex = 12
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(372, 192)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(108, 21)
        self._textBox5.TabIndex = 13
        # 
        # textBox6
        # 
        self._textBox6.Location = System.Drawing.Point(372, 237)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(107, 21)
        self._textBox6.TabIndex = 14
        # 
        # label10
        # 
        self._label10.Location = System.Drawing.Point(291, 282)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(102, 22)
        self._label10.TabIndex = 15
        self._label10.Text = "Total Revenue:"
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.White
        self._label11.Location = System.Drawing.Point(384, 280)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(111, 23)
        self._label11.TabIndex = 16
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(41, 341)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(129, 59)
        self._button1.TabIndex = 17
        self._button1.Text = "Calculate Revenue"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(222, 342)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(130, 59)
        self._button2.TabIndex = 18
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(412, 341)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(120, 57)
        self._button3.TabIndex = 19
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(627, 458)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg186StadiumSeating"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        decClassSoldA = 0
        decClassSoldB = 0
        decClassSoldC = 0
        decClassGeneA = 0.0
        decClassGeneB = 0.0
        decClassGeneC = 0.0
        decTotalRevenue = 0.0
        
        decClassSoldA = float(self._textBox1.Text)
        decClassSoldB = float(self._textBox2.Text)
        decClassSoldC = float(self._textBox3.Text)
        decClassGeneA = float(self._textBox4.Text)
        decClassGeneB = float(self._textBox5.Text)
        decClassGeneC = float(self._textBox6.Text)
        
        decTotalRevenue = decClassSoldA * decClassGeneA + decClassSoldB * decClassGeneB + decClassSoldC * decClassGeneC
        self._label11.Text = str(round(decTotalRevenue, 2))

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._textBox6.Text = ""
        self._label11.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()