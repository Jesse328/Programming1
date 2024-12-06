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
        self._label1.Location = System.Drawing.Point(44, 86)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(117, 70)
        self._label1.TabIndex = 0
        self._label1.Text = "Annual Salary:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(34, 181)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(127, 70)
        self._label2.TabIndex = 1
        self._label2.Text = "Pay periods per year:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(34, 302)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(127, 70)
        self._label3.TabIndex = 2
        self._label3.Text = "Salary per pay period:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(169, 113)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(125, 21)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(167, 206)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(127, 21)
        self._textBox2.TabIndex = 4
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(167, 311)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(136, 48)
        self._label4.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 407)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(154, 57)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(182, 407)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(140, 57)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(343, 408)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(128, 55)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(487, 482)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Salary calculation"
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button1Click(self, sender, e):
        decAnnualSalary = 0.0
        intPayPeriods = 0
        decSalary = 0.0
     
        decAnnualSalary = float(self._textBox1.Text)
        intpayPeriods = int(self._textBox2.Text)
        
        decSalary = decAnnualSalary / intpayPeriods
        self._label4.Text = str(round(decSalary,2))

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""
        

    def Button3Click(self, sender, e):
        Application.Exit()