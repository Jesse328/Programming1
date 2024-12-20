import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(23, 32)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(117, 36)
        self._label1.TabIndex = 0
        self._label1.Text = "sales for the month:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(146, 32)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 21)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 87)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(128, 36)
        self._label2.TabIndex = 2
        self._label2.Text = "Advance pay awarded:"
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(146, 87)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 21)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(23, 147)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(117, 30)
        self._label3.TabIndex = 4
        self._label3.Text = "Commission rate:"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(23, 208)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(117, 36)
        self._label4.TabIndex = 6
        self._label4.Text = "Commission:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(127, 208)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(128, 25)
        self._label5.TabIndex = 7
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(23, 276)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(87, 22)
        self._label6.TabIndex = 8
        self._label6.Text = "Net pay:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Location = System.Drawing.Point(127, 274)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(127, 23)
        self._label7.TabIndex = 9
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(14, 335)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(95, 45)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(135, 335)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(92, 44)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(256, 335)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(89, 43)
        self._button3.TabIndex = 12
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Location = System.Drawing.Point(127, 147)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(128, 25)
        self._label8.TabIndex = 13
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(378, 438)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg240Comm"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        decMonthlySale = 0.0
        decAdvancePay = 0.0
        decCommissionRate = 0.0
        decCommissionAmount = 0.0
        decNetPay = 0.0
        
        decMonthlySale = float(self._textBox1.Text)
        decAdvancePay = float(self._textBox2.Text)
      
        decCommissionRate = 0.06
        decCommissionAmount = decMonthlySale * decCommissionRate
        decNetPay = decCommissionAmount - decAdvancePay
        self._label8.Text = str(round(decCommissionRate, 2))
        self._label5.Text = str(round(decCommissionAmount, 2))
        self._label7.Text = str(round(decNetPay, 2))
        
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label8.Text = ""
        self._label7.Text = ""
        self._label5.Text = ""
        
   

    def Button3Click(self, sender, e):
        Application.Exit()