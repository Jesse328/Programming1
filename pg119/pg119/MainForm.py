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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 73)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(124, 61)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter your first name:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 182)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(124, 51)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter your last name:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(1, 309)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(144, 50)
        self._label3.TabIndex = 2
        self._label3.Text = "This is your full name:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(150, 94)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(135, 21)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(150, 197)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(135, 21)
        self._textBox2.TabIndex = 4
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(26, 391)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(118, 62)
        self._button1.TabIndex = 5
        self._button1.Text = "Show Name"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(167, 391)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(118, 62)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(315, 391)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(118, 62)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.WhiteSmoke
        self._label4.Location = System.Drawing.Point(141, 326)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(144, 33)
        self._label4.TabIndex = 8
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.White
        self.ClientSize = System.Drawing.Size(508, 471)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Pg119"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._textBox1.Text = str("First name")
        self._textBox2.Text = str("Last name")
        self._label4.Text = str("Full name")
        self._textBox1.Text = "Jesse"
        self._textBox2.Text ="Huang"
        self._label4.Text = "Jesse Huang"

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""
        

    def Button3Click(self, sender, e):
        Application.Exit()