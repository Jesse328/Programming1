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
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Info
        self._label1.Location = System.Drawing.Point(12, 41)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(110, 46)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter your first name"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Info
        self._label2.Location = System.Drawing.Point(12, 115)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(109, 44)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter your last name"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.Info
        self._label3.Location = System.Drawing.Point(10, 244)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(135, 40)
        self._label3.TabIndex = 2
        self._label3.Text = "This is your full name"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(144, 50)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(123, 20)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(144, 121)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(122, 20)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(170, 253)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(136, 20)
        self._textBox3.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(20, 335)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(124, 67)
        self._button1.TabIndex = 6
        self._button1.Text = "show name"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(168, 337)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(123, 64)
        self._button2.TabIndex = 7
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(309, 337)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(123, 64)
        self._button3.TabIndex = 8
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Yellow
        self.ClientSize = System.Drawing.Size(444, 446)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pg119"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        str(Full Name)= 
        
        
        
        
        self._textBox1.Text = "First Name"
        self._textBox2.Text = "Last Name"
        self._textBox3.Text = "Full Name"
        